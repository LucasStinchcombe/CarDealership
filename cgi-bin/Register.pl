#!/usr/bin/perl
use diagnostics;
use warnings;
use CGI;
my $q = new CGI;
my $firstname = $q->param( 'firstname' );
my $lastname = $q->param( 'lastname' );
my $username = $q->param( 'username' );
my $pass1 = $q->param( 'pass1' );
my $pass2 = $q->param( 'pass2' );

my $file = "members.csv";
open (my $data, '<', $file);
my $status = 'YES';
while (my $line = <$data>) {
	our @split = split (',', $line);
	if ($split[0] eq $username) {
		close $file;
		print $q->header(-location => 'http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/RegisterError.html');
		$status = 'NO';
		last;
	}
}
if ($status eq "YES") {
close $file;						
	if (index($username, ',') != -1 || 
	index($firstname, ',') != -1 ||
	index($lastname, ',') != -1 ||
	index($pass1, ',') != -1 || 
	index($pass2, ',') != -1) {
print $q->header(-location => 'http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/RegisterErrorComma.html');
	}
	else {
		open (my $csv, '>>', $file);
		print $csv "$username,$firstname,$lastname,$pass1,$pass2\n";
		close $file ;
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
	<a href="http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/#">Home</a>
	<a href="http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/catalogue.html">Catalogue</a>
	<a href="http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/login.html">Login</a>
	<a href="http://cgi.cs.mcgill.ca/~jgoxha/cgi-bin/register.html">Register</a>
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
}
}
