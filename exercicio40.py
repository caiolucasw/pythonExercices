'''Write a program which accepts a string as input to print "Yes" if the string is
"yes" or "YES" or "Yes", otherwise print "No".'''


string = input("Digite a palavra: ")

if string == 'Yes' or string == 'YES' or string == 'yes':
    print("Yes")
else:
    print("No")