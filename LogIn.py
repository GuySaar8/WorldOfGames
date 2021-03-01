#####################
# import modules
#####################
import subprocess as sp

#####################
# Define functions
#####################
def singin():  # say hello to new user
    print("Hello Rookie and welcome to the World Of Games (WoG)")
    print("Before we begin, the best experience of your life")
    print("You need to create a new account")
    pass


def welcome(logonname):  # say hello to user
    print("Hello " + logonname + " and welcome to the World Of Games (WoG)")
    print("Here you can find many cool games to play")


def loging():
    # Accounts DB will be loeded and saved to JSON file
    accounts = {'USERNAME': ['info'], 'DEVOPS': ['Experts']}

    # get useruame
    tmp = sp.call('clear', shell=True)
    logonname = input("What is your log on name: ")  # Get Logon name
    logonname = logonname.upper()

    # check if username exist
    # need to add check log on name by UPPER
    while True:
        try:
            if accounts[logonname]:
                tmp = sp.call('clear', shell=True)
                welcome(logonname)
                break
        except KeyError:  # if user does not exist user will be created
            tmp = sp.call('clear', shell=True)
            singin()
            account_name = 'null'
            account_name = input("Insert your new account name: ")
            account_name = account_name.upper()
            accounts[account_name] = 'account_info'
            logonname = account_name

    return logonname