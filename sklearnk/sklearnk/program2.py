%{
#include <stdio.h>
int nf=0,p=0,n=0,pf=0;
%}

%%

[+]?[0-9]+                     {p++;}
[-][0-9]+                      {n++;}

[+]?[0-9]+\.[0-9]+             {pf++;}
[-][0-9]+\.[0-9]+              {nf++;}

[+]?[0-9]+\/[+]?[0-9]+         {pf++;}
[+]?[0-9]+\/[-][0-9]+          {nf++;}
[-][0-9]+\/[+]?[0-9]+          {nf++;}
[-][0-9]+\/[-][0-9]+           {pf++;}

#                              {return 0;}

[ \t\n]                        ;

.                              ;

%%

int yywrap(){
    return 1;
}

int main(){
    printf("Enter numbers, (use # to end )\n");
    yylex();
    printf("Number of positive integer is= %d\n",p);
    printf("Number of negative integer is= %d\n",n);
    printf("Number of positive fractions is= %d\n",pf);
    printf("Number of negative fractions is= %d\n",nf);
}


//2.b.l
%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+        { yylval = atoi(yytext); return NUM; }
[+\-*/()]     { return yytext[0]; }
\n            { return 0; }
[ \t]         ;
.             { return yytext[0]; }

%%


//2.b.y


%{
#include <stdio.h>
#include <stdlib.h>

void yyerror();
int yylex(void);
%}

%token NUM
%left '+' '-'
%left '*' '/'
%right UMINUS

%type I

%%

S : I { printf("Result is %d\n", $1); }
  ;

I : I '+' I        { $$ = $1 + $3; }
  | I '-' I        { $$ = $1 - $3; }
  | I '*' I        { $$ = $1 * $3; }
  | I '/' I        { if ($3 == 0) yyerror(); else $$ = $1 / $3; }
  | '(' I ')'      { $$ = $2; }
  | NUM            { $$ = $1; }
  | '-' I %prec UMINUS { $$ = -$2; }
  ;

%%

int main() {
    printf("Enter an expression:\n");
    yyparse();
    printf("Valid\n");
    return 0;
}

void yyerror() {
    printf("Invalid\n");
    exit(0);
}