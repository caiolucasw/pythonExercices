'''Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address. Both user names and company names
are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
In case of input data being supplied to the question, it should be assumed to be a console input.'''


email = input('Digite um email no formato aaaa@empresa.com: ')
email_lista = email.split('@')
nome = email_lista[0]
print(nome)


#exercicio54

'''Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google'''

email = input('Digite um email no formato aaaa@empresa.com: ')
email_lista = email.split('@')
empresa = email_lista[1].split('.')[0]
print(empresa)