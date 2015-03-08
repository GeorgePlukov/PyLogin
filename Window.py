from Tkinter import *
from passlib.hash import pbkdf2_sha256

# Program for basic file based username and password storage


USERFILE = "UserPass.txt"

current_account = None
def main ():
	inpt = raw_input("r to register, l to login: ")
	if (inpt == "r"):
		# register the user
		register()
	elif (inpt == "l"):
		login()

# Get the users information, hash it and store it for later
def register():
	login = getUserPass()

	#check if that user already exists
	f = open (USERFILE, 'r')

	userTaken = False
	# check the file for that username 
	for line in f:
		words = line.split(" ")
		if (words[0] == login[0]):
			userTaken = True
			break

	# If the username was taken
 	if (userTaken == True):
 		print "Sorry username is already taken"
		f.close()
	else:
		f.close()
		addUser(login[0],login[1])
		print "User, " + login[0] + " has been created"

		
def addUser(username, password):
	f = open (USERFILE, 'a')
	f.write(username + " " + pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16) + "\n")
	f.close()


def login():
	login = getUserPass()
	f = open(USERFILE, "r")
	for line in f:
		words = line.split(" ")
		if (words[0] == login[0]):
		 	if (pbkdf2_sha256.verify(login[1], words[1])):
		 		current_account = login[0]
	print current_account
	f.close()



# return the users username and password 
# username in 0, password in 1
def getUserPass():
	return [raw_input("Enter your username: "),
			raw_input("Enter your password: ")]




main()