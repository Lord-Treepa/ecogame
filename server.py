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
		userAuthV = True
	else:
        	return "Bad credentials!"
	if command != "":
		userAuthV = True
	else:
		return "Bad command!"
	command = commandSplitter(command)
	if command[0] == "stock":
		interpStock(command)
	else:
		return command
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
		clen = len(command) - 1
		cmdar = ""
		j = True
		while j:
			cmdar = cmdar + command[i]
			c = command[i]
			i = i + 1
			try:
				if command[i] != " " and i <= clen:
					j = True
				else:
					j = False
			except:
				j = False
		retcmd.append(cmdar)
		if i > clen:
			return retcmd
		elif command[i] == " ":
			i = i + 1
			return whileSplitter(i, command, retcmd)
	return whileSplitter(i, command, retcmd)

#Stock Command Interpreter
def interpStock(command):
	cmlen = 0
	for cmd in command:
		cmlen = cmlen + 1
	if cmlen != 3 or cmlen != 4:
		return False
	elif comand[1] != "buy" or command[1] != "sell":
		return False

#Main Code
print interpMain("Treepa", "qwert", "stock buy nzx50 6700")
