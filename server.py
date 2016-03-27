#Define Functions:
#Data Reciever:
def conHandler(con):
	#Code Below:
	return False
	#Code Above:

#Primary Command Interpreter
def interpMain(id, password, command):
	#Credential Checker
	if userAuth(id, userGet()[id]):
		print "Hi"
	else:
        	return "Bad credentials!"
	command = commandSplitter(command)
	print command
	return "Hi"
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
#Command Splitter
def commandSplitter(command):
	i = 0
	c = ""
	retcmd = []
	#Command Splitter Sub Function
	def whileSplitter(i, command, retcmd):
		c = ""
		clen = len(command) - 1
		cmdar = ""
		while c != " " and i <= clen:
			cmdar = cmdar + c
			c = command[i]
			i = i + 1
		retcmd.append(cmdar)
		if i > clen:
			return retcmd
		elif command[i] == " ":
			i = i + 1
			return whileSplitter(i, command, retcmd)
	return whileSplitter(i, command, retcmd)
print interpMain("Treepa", "qwert", "Ima TWee!")
