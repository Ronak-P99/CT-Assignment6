'''
3. Interactive Help Desk Bot
Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). 
If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. 
Print out the category of the issue for the support team.

'''
def issue_help():
    while True:
        user_input = str(input("\nHow can we help with your issue today? Choices include: 'login', 'performance', 'error' ").lower())
        if user_input == 'login':
            print(f"\nThis is a {user_input} issue and we have sent a password recovery email.\n")
            break
        elif user_input == 'performance':
            print(f"\nThis is a {user_input} issue and we will virtually monitor your device.\n")
            break
        elif user_input == 'error':
            print(f"\nThis is an {user_input} issue. Please make sure all information provided is accurate.\n")
            break
        else:
            print("\nInvalid selection! Please try again.\n")



while True:
    user_input = input("Welcome! Please provide what you may need help with. Options include: 'help', 'issue', 'contact support', 'quit' ").lower()
    if user_input == 'help':
        print("\nWelcome to the help menu! We are here 24/7 for any of your needs and have plenty of online resources!\n")
    elif user_input == 'issue':
        issue_help()
    elif user_input == 'contact support':
        input("\nPlease provide your phone number and a customer support representative will contact you shortly!\n")
    elif user_input == 'quit':
        print("\nThanks for your time!\n")
        break
    else:
        print("\nInvalid choice. Try again.\n")

    

