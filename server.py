#Define Functions:
#Data Reciever:
def conHandler(con):
	#Code Below:
	return False
	#Code Above:

#Primary Command Interpreter
def interpMain(id, password, command):
	#Code Below
	return False
	#Code Above

#User Authentication
def userAuth(id, password):
	try:
		if userGet()[id] == password:
			return True
		else:
			return False
	except:
		return False

#User Database
def userGet():
	#Retrieve user stats from files
	f = open("users.txt", "r")
	try:
		userarray = f.readlines()
	finally:
		f.close()
	f = open("passwords.txt", "r")
	try:
		passwordarray = f.readlines()
	finally:
		f.close()
	#Remove \n
	userstats = {}
	i = 0
	for userd in userarray:
		userd = userd.rstrip('\n')
		passd = passwordarray[i].rstrip('\n')
		i = i + 1
		userstats[userd] = passd
	return userstats
