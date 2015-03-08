from Tkinter import *
from passlib.hash import pbkdf2_sha256

# Program for basic file based username and password storage


USERFILE = "UserPass.txt"
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
			usertaken = True
			break
	# If the username was taken
 	if (userTaken):
 		print "Sorry username is already taken"
		f.close()
	else:
		f.close()
		addUser(login[0],login[1]);

		
def addUser(username, password):
	f = open (USERFILE, 'a')
	f.write(username + " " + pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16))
	f.close()


def login():
	login = getUserPass()



# return the users username and password 
# username in 0, password in 1
def getUserPass():
	return [raw_input("Enter your username: "),
			raw_input("Enter your password: ")]




main()