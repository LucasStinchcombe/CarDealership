#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){

  printf("%s%c%c\n", "Content-Type:text/html;charset=iso-8859-1",13,10);

  FILE *catalogue;
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
  FILE *members=fopen("members.csv", "rt");
  while(fgets(buffer, 100, members)!=NULL){
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
    printf("%s %s", memberUser, memberPass);
    if((strcmp(username, memberUser)==0) && (strcmp(password, memberPass)==0)){
      valid = 1;
      break;
    }
    a=0;
  }
  fclose(members);
  a=0;
  if(valid==1){
    catalogue = fopen("catalogue.html", "rt");
    while(fgets(buffer, 100, catalogue)!=NULL){
      a++;
      if(a==25) printf("<input type=\"hidden\" name=\"user\" value=\"%s\">", username);
      else{
        b=0;
        while(buffer[b] != '\0'){
          c = buffer[b];
          putchar(c);
          b++;
        }
      }
    }
    fclose(catalogue);
  }
  return 0;
}
