#!/usr/bin/env python
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
print "Content-Type: text/html\n\n"

def isLoggedIn():
	if form.has_key('user') and form['user'].value != '':
		log = open('loggedin.csv', 'r+')
		users = log.readlines()
		user = form['user'].value + '\n'
		if user in users:
			displayBill()		
		else:
			displayError()
	else:
		displayError()

def displayError():
	print "<html>"
	print "<head></head>"
	print "<body><center><p>Error: Please log in to purchase</p>"
	print "<p><a href=\"http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/catalogue.html\">Return to catalogue</a></p></center>"
	print "</body></html>"
	
def displayBill():
	inventory = open('inventory.csv', 'r')
	invList = inventory.readlines()
	costM = 0
	costL = 0
	costF = 0
	
	print "<html>"
	print "<head></head>"
	print "<body bgcolor=\"gray\">"
	print "<b><i>Bill:</i></b>"
	
	if form.has_key('maserati') and form['maserati'].value == 'on':
		quantM = int(form['quantityM'].value)
		maserati = (invList.pop(0)).split(',', 2)  
		price = maserati.pop()		# cost
		price = int(price[:-1])
		left = int(maserati.pop())	# quantity available
		if left == 0 :
			print "<center><i>Sorry, we are out of Maserati Bora 2016 Concept!</i></center>"
		else :
			if quantM > left :
				quantM = left		# can only buy as much as is in stock
				print "<center><i>Sorry, our stock of Maserati Bora 2016 Concept is limited!</i></center>"
			costM = quantM*price		# quantity * cost
			print "<center>%d   Maserati Bora 2016 Concept, $%d</center>" %(quantM,costM)
			left = left - quantM		# update quantity
			maserati.append(str(left))		# restore list
			maserati.append(str(price))
			invList.insert(0, ','.join(maserati)+'\n')	# reform line and restore in csv

	if form.has_key('lamborghini') and form['lamborghini'].value == 'on':
		quantL = int(form['quantityL'].value)
		lamborghini = (invList.pop(1)).split(',', 2)
		price = lamborghini.pop()
		price = int(price[:-1])
		left = int(lamborghini.pop())
		if left == 0 :
			print "<center><i>Sorry, we are out of Lamborghini Veneno 2016 Concept!</i></center>"
		else :
			if quantL > left :
				quantL = left
				print "<center><i>Sorry, our stock of Lamborghini Veneno 2016 Concept is limited!</i></center>"
			costL = quantL*price
			print "<center>%d   Lamborghini Veneno 2016 Concept, $%d</center>" %(quantL,costL)
			left = left - quantL
			lamborghini.append(str(left))
			lamborghini.append(str(price))
			invList.insert(1, ','.join(lamborghini)+'\n')

	if form.has_key('ferrari') and form['ferrari'].value == 'on':
		quantF = int(form['quantityF'].value)
		ferrari = (invList.pop(2)).split(',', 2)
		price = ferrari.pop()
		price = int(price[:-1])
		left = int(ferrari.pop())
		if left == 0 :
			print "<center><i>Sorry, we are out of Ferrari F12 Spyder 2016 Concept!</i></center>"
		else :
			if quantF > left :
				quantF = left
				print "<center><i>Sorry, our stock of Ferrari F12 Spyder 2016 Concept is limited!</i></center>"
			costF = quantF*price
			print "<center>%d   Ferrari F12 Spyder 2016 Concept, $%d</center>" %(quantF,costF)
			left = left - quantF
			ferrari.append(str(left))
			ferrari.append(str(price))
			invList.append(','.join(ferrari)+'\n')
	
	inventory.close()
	inventory = open('inventory.csv', 'w')
	inventory.writelines(invList)		# rewrite invlist as lines
	inventory.close()
	total = costM + costL + costF		# calculate total
	print "<br /><center><i><b>Total: $%d</b></i></center><br />" %(total)
	print "<center><h6><i>*If your item total is less than what you input, we are out of or limited in stock</i></h6></center>"
	print "<center><a href=\"http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/catalogue.html\">Return to catalogue</a></center>"
	print "<center><a href=\"http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/index.html\">Return to homepage</a></center></body>"
	print "</html>"
	
isLoggedIn()
