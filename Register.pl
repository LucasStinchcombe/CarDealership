#!/usr/bin/perl
use strict;
use warnings;
use CGI;
my $q = new CGI;
my $firstname = $q->param( 'firstname' );
my $lastname = $q->param( 'lastname' );
my $username = $q->param( 'username' );
my $password = $q->param( 'password' );
my $cpassword = $q->param( 'cpassword' );

open (my $fh, "<", 'members.csv') or die "Cannot open $file: $!";
while (my $row = <$fh>) {
	if (index($row, $username) != -1) 
	{
	#close $fh;
	print $q->header(-location => 'http://cgi.cs.mcgill.ca/~rkucer/RegisterError.html');
	}
}
close $fh;
open($fh, '>>', 'members.csv');
print $fh "$username,$firstname,$lastname,$password,$cpassword\n";
close $fh;
print "Content-type: text/html\n\n";
print <<HTML;
<html>
<head>
<title>Registration Complete</title>
<link href='http://fonts.googleapis.com/css?family=Fjalla+One' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="style.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
</head>
<body background="lambo1.jpg" text="black">
<div class="menu">
<div class="logo">
<h1>Buy Our Cars</h1>
</div>
<div class="links">
<a href="http://cgi.cs.mcgill.ca/~lstinc/CarDealership/#">Home</a>
<a href="http://cgi.cs.mcgill.ca/~lstinc/CarDealership/catalogue.html">Catalogue</a>
<a href="http://cgi.cs.mcgill.ca/~lstinc/CarDealership/login.html">Login</a>
<a href="http://cgi.cs.mcgill.ca/~rkucer/register.html">Register</a>
</div>
</div>
<div style="position: relative">
<h1 style="position: fixed; top: 150; width:100%; text-align: left">Registration Complete</h1>
<p style="position: fixed; top: 200; width:100%; text-align: left">Name: $firstname $lastname</p>
<p style="position: fixed; top: 250; width:100%; text-align: left">Username: $username</p>
</div>
</body>
HTML
exit;

