login.cgi: login.o
	gcc -o login.cgi login.o

login.o: login.c
	gcc -c login.c
