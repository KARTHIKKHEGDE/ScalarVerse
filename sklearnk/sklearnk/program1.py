%{
#include <stdio.h>

int lines = 1, spaces = 0, words = 0, characters = 0;
%}

%%

#              { return 0; }

[ ]            { spaces++; characters++; }
[\t]           { spaces++; characters++; }
\n             { lines++; characters++; }

[a-zA-Z]+      { words++; characters += yyleng; }

.              { characters++; }

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a paragraph (end with #):\n");
    yylex();

    printf("\nNumber of lines = %d\n", lines);
    printf("Number of spaces = %d\n", spaces);
    printf("Number of words = %d\n", words);
    printf("Number of characters = %d\n", characters);

    return 0;
}


// 1b.l

%{
#include "y.tab.h"
%}

%%

a        { return 'a'; }
b        { return 'b'; }
c        { return 'c'; }

#        { return 0; }

[ \t\n]  ;

.        { return yytext[0]; }

%%

int yywrap() {
    return 1;
}


//1.b.y

%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

%start S

%%

S : A B ;

A : 'a' A 'b'
  | /* empty */
  ;

B : 'b' B 'c'
  | /* empty */
  ;

%%

int main() {
    printf("Enter string:\n");
    yyparse();
    printf("Valid string\n");
    return 0;
}

void yyerror(const char *s) {
    printf("Invalid string\n");
    exit(0);
}