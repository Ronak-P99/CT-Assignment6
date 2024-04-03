'''
2. User Input Data Processor
Objective:
The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. 
Both should be at least 2 characters long. If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. 
The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. 
If the password does not meet these criteria, print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format
'''

def user_name(first, last):
    if len(first) >= 2 and len(last) >= 2:
        first_len = len(first)
        last_len = len(last)
        print(f"Your first name is a total of: {first_len} characters")
        print(f"Your last name is a total of: {last_len} characters")
    else:
        print("hmmmm... looks like you provided an innacurate name. Try again.")

def pass_check(passwd):
     
    SpecialSym =['$', '@', '#', '%', '!']
    val = True
     
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
         
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
         
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
         
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
         
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
         
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val      

def email_format(email):
    SpecialSym = '@'
    val = True

    if len(email) < 6:
        print('length should be at least 6')
        val = False
   
    if not any(char in SpecialSym for char in email):
        print('Password should have an @ symbol in the middle')
        val = False

    if user_email[-4:] != '.com':
        print('You need to end email with .com')
        val = False
    
    if val:
        return val    





user_first = input("Welcome... Please provide your first name! ")
user_last = input("Now your last name please! ")
user_name(user_first, user_last)

while True:
    user_pass = input("Please enter a complex password ")
    valid = pass_check(user_pass)
    if valid == True:
        print("Great job! Password works!")
        break
    else: 
       print("Password not accepted!")

while True:
    user_email = input("Please provide an email ")
    valid_two = email_format(user_email)
    if valid_two == True:
        print("Great job! email works!")
        break
    else: 
       print("email not accepted!")
