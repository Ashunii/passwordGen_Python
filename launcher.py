import random
import string

letters_of_password = int(input('Enter Number of letters of password: '))
numbers_of_password = int(input('Enter Number of numbers of password: '))

number_list = ''.join(random.choice(string.digits) for i in range(numbers_of_password))
letter_list = ''.join(random.choice(string.ascii_letters) for i in range(letters_of_password))
	
syntax_list = number_list + letter_list + '!@#'
if len(syntax_list) < 6:
    print('Password should be minimum 6 characters')
    exit()
result = random.sample(syntax_list, len(syntax_list)) 
password = ''.join((result))
print('Your pasword is {}'.format(password))

choice = input('Do you want to keep it ? : [Y]es | [N]o ')

if choice.__eq__('Y'):
    login = input('login : ')
    login = login+ " " + password + "\n"
    f = open("password.txt","a")
    f.write(login)
    f.close

