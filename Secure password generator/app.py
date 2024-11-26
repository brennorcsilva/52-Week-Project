from random import choice
import string


special = [ '!', '@', '#', '$', '%', '&', '*', '_', '<', '>' ]
specialChar = ''.join(special)

password_size = int(input('Input how many characters do u want in your password:'))

include_uppercase = input('Do you want uppercase? (y/n): ').lower() == 'y'
include_numbers = input('Do you want numbers? (y/n): ').lower() == 'y'
include_special = input('Do you want special characters? (y/n): ').lower() == 'y'

chars = string.ascii_lowercase

if include_uppercase:
    chars += string.ascii_uppercase
if include_numbers:
    chars += string.digits
if include_special:
    chars += specialChar

secure_password = ''

if password_size <= 0:
    print('Invalid password size! \nTry again! Remember to set a minimum password length!')
    
for i in range(password_size):
    secure_password += choice(chars)

print(secure_password)