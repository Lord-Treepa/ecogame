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
		if userData[id] == password:
			return True
		else:
			return False
	except:
		return False
userData = {1 : 'Treepa'}
try:
	id = raw_input("ID: ")
except:
	id = 1
print userAuth(id, raw_input("Password: "))
