#!/usr/local/bin/python
import cgi

form = cgi.FieldStorage()

print "Content-Type: text/html\n\n"

def isLoggedIn():
	#form = cgi.FieldStorage()
	#global form
	if form.has_key('user') and form['user'] != "":
		log = open('LoggedIn.csv', 'r')
		users = log.readlines()
		user = form['user']
		i = users.count(user)		#check if user is "logged in"
		if i == 0:			#if not, display error
			displayError()		
		else:
			displayBill()
	else:
		dispayError()

def displayError():
	print "<html><head></head>"
	print "<body><center><p>Error: Please log in to purchase</p>"
	print "<p><a href=\"http://www.cs.mcgill.ca/~jgoxha/catalogue.html\">Return to catalogue</a></p></center>"
	print "</body></html>"
	#f = open('loginerror.html','w')
	#message = """<html>
	#<head></head>
	#<body><p><center>ERROR: Please log in to purchase</center></p>
	#<center><a href="http://www.cs.mcgill.ca/~jgoxha/catalogue.html">Return to catalogue</a</center></body>
	#</html>"""
	#f.write(message)
	#f.close()
	#print f
	
def displayBill():
	inventory = open('Inventory.csv', 'r')
	invList = inventory.readlines()
	
	#form = cgi.FieldStorage()
	#global form
	
	costM = 0
	costL = 0
	costF = 0
	
	print "<html>"
	print "<head></head>"
	print "<body>"
	
	if form.has_key('maserati') and form['maserati'] == 'on':
		quantM = int(form['quantityM'])
		maserati = invList[0].split(',')
		maserati[1] = int(maserati[1])	# quantity available
		maserati[2] = int(maserati[2])	# cost
		if quantM > maserati[1]
			quantM = maserati[1]	# can only buy as much as is in stock
		costM = quantM*maserati[2]	# quantity * cost
		print "<center>%d Maserati Bora 2016 Concept, $%d</center>" %(quantM,costM)
		maserati[1] = maserati[1] - quantM # update quantity
		invList[0] = ','.join(maserati)		# reform the line

	if form.has_key('lamborghini') and form['lamborghini'] == 'on':
		quantL = int(form['quantityL'])
		lamborghini = invList[1].split(',')
		lamborghini[1] = int(lamborghini[1])
		lamborghini[2] = int(lamborghini[2])
		if quantL > lamborghini[1]
			quantL = lamborghini[1]
		costL = quantL*lamborghini[2]
		print "<center>%d Lamborghini Veneno 2016 Concept, $%d</center>" %(quantL,costL)
		lamborghini[1] = lamborghini[1] - quantL
		invList[1] = ','.join(lamborghini)

	if form.has_key('ferrari') and form['ferrari'] == 'on':
		quantF = int(form['quantityF'])
		ferrari = invList[2].split(',')
		ferrari[1] = int(ferrari[1])
		ferrari[2] = int(ferrari[2])
		if quantF > ferrari[1]
			quantF = ferrari[1]
		costF = quantF*ferrari[2]
		print "<center>%d Ferrari F12 Spyder 2016 Concept, $%d</center>" %(quantF,costF)
		ferrari[1] = ferrari[1] - quantF
		invList[2]= ','.join(ferrari)
	
	inventory.close();
	inventory = open('Inventory.csv', 'w')
	inventory.writelines(invList)		# rewrite invlist as lines
	inventory.close()
	total = costM + costL + costF		# calculate total
	print "<b><i>Bill:</i></b>"
	print "<center><i><b>Total: $%d</b></i></center><br />" %(total)
	print "<center><a href=\"http://www.cs.mcgill.ca/~jgoxha/cagalogue.html\">Return to catalogue</a></center>"
	print "<center><a href=\"http://www.cs.mcgill.ca/~jgoxha/homepage.html\">Return to homepage</a></center></body>"
	print "</html>"
	
isLoggedIn()
