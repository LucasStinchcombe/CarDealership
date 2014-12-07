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
	print $q->header(-location => 'RegisterError.html');
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
      print $q->header(-location => 'RegisterErrorComma.html');
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
</head>
<body>
  <div class="menu">
    <div class="logo">
      <h1>Buy Our Cars</h1>
    </div>
    <div class="links">
      <a href="index.html">home</a>
      <a href="catalogue.html">catalogue</a>
      <a href="login.html">login</a>
    </div>
  </div>
  <div class="done">
    <div class="registration">
      <h1>Registration Complete!</h1>
      <p>Name:$firstname $lastname</p>
      <p>Username:$username</p>
    </div>
  </div>

</body>
</html>
HTML
exit;
}}
