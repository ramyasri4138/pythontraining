def passwordstrength(password):
    if len(password)<8:
        return 'enter minimum 8 characters'
    if not any(char.isupper for char in password):
        return 'atleast one upper letter should be there'
    if not any (char.islower for char in password):
        return 'need small letters'
    if not any(char.isdigit for char in password):
        return 'atleast one digit required'
    if not any(char in r'$@!#%^&*|<>"()[]{}.,\;:' for char in password):
        return 'special characters are required'
    else:
        return 'strong password'
password=input("enter the password: ")
result=passwordstrength(password)
print(result)