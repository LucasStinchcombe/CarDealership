#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){

  printf("%s%c%c\n", "Content-Type:text/html;charset=iso-8859-1",13,10);

  char username[26];
  char password[26];
  char buffer[100];
  char memberUser[26];
  char memberPass[26];
  char c;
  int len;
  int valid = 0;
  int a = 0;
  int b = 0;
  int n = atoi(getenv("CONTENT_LENGTH"));


  //get username and password and store in their respective strings
  while((c=getchar()) != '&' && a<n+10){
    if(a<25 && a>4) username[a-5]=c;
    a++;
  }
  username[a-5]='\0';
  n=n-a;
  a=0;
  while((c=getchar()) != EOF && a<n+10){
    if(a<25 && a>4) password[a-5]=c;
    a++;
  }
  password[a-5]='\0';
  a=0;

  //open members.csv
  FILE *ptr=fopen("members.csv", "rt");

  //read line by line, storing each member's username and password and comparing with login input.
  while(fgets(buffer, 100, ptr)!=NULL){
    len=strlen(buffer);
    while(buffer[a] != ','){
      a++;
    }
    a++;
    b=a;
    while(buffer[a] != ','){
      memberUser[a-b]=buffer[a];
      a++;
    } memberUser[a-b]='\0';
    a++;
    b=a;
    while(buffer[a] != '\n'){
      memberPass[a-b]=buffer[a];
      a++;
    } memberPass[a-b]='\0';
    //break if user is verified
    if((strcmp(username, memberUser)==0) && (strcmp(password, memberPass)==0)){
      valid = 1;
      break;
    }
    a=0;
  }
  fclose(ptr);
  a=0;

  //if valid, open catalogue and print to stdout with username in hidden field
  if(valid==1){
    ptr = fopen("catalogue.html", "rt");
    while(fgets(buffer, 100, ptr)!=NULL){
      a++;
      if(a==25) printf("<input type=\"hidden\" name=\"user\" value=\"%s\">", username);
      else if(a==17) printf("<a>Logged In</a>");
      else{
        b=0;
        while(buffer[b] != '\0'){
          c = buffer[b];
          putchar(c);
          b++;
        }
      }
    }
    fclose(ptr);

    //read loggedin.csv and check existence of user
    ptr = fopen("loggedin.csv", "rt");
    while(fgets(buffer, 100, ptr)!=NULL){
      a=0;
      while(buffer[a] != '\n'){
	memberUser[a]=buffer[a];
	a++;
      }
      memberPass[a]='\0';
      //if user exits, skip the append step
      if(strcmp(username, memberUser)==0){
	fclose(ptr);
	goto end;
      }
    }
    fclose(ptr);
    
    //append username to loggedin.csv
    ptr = fopen("loggedin.csv", "a");
    fprintf(ptr, "%s\n", username);
    fclose(ptr);

  }
  
  //else print error page to stdout
  else{
    ptr = fopen("error.html", "rt");
    while(fgets(buffer, 100, ptr)!=NULL){
      b=0;
      while(buffer[b] != '\0'){
	c = buffer[b];
	putchar(c);
	b++;
      }
    }
    fclose(ptr);
  }
  

 end:
  return 0;
}
