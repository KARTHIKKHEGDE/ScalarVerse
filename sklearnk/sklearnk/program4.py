%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+        { yylval.sym = yytext[0]; return NUMBER; }
[a-zA-Z]      { yylval.sym = yytext[0]; return LETTER; }

[ \t\n]       ;

.             { return yytext[0]; }

%%

int yywrap() { return 1; }


//4.y

%{
#include <stdio.h>
#include <stdlib.h>

struct quad {
    char op;
    char arg1;
    char arg2;
    char res;
} q[20];

int idx = 0;
char temp = 'A';

char newTemp() {
    return temp++;
}

char gen(char a, char b, char op) {
    char t = newTemp();
    q[idx].op = op;
    q[idx].arg1 = a;
    q[idx].arg2 = b;
    q[idx].res = t;
    idx++;
    return t;
}

void printCode();
void yyerror(const char *s);
int yylex();
%}

%union { char sym; }

%token <sym> LETTER NUMBER
%type <sym> expr

%left '+' '-'
%left '*' '/'

%%

stmt : LETTER '=' expr ';' {
            q[idx].op = '=';
            q[idx].arg1 = $3;
            q[idx].arg2 = '-';
            q[idx].res = $1;
            idx++;
        }
     ;

expr : expr '+' expr { $$ = gen($1,$3,'+'); }
     | expr '-' expr { $$ = gen($1,$3,'-'); }
     | expr '*' expr { $$ = gen($1,$3,'*'); }
     | expr '/' expr { $$ = gen($1,$3,'/'); }
     | '(' expr ')'  { $$ = $2; }
     | LETTER        { $$ = $1; }
     | NUMBER        { $$ = $1; }
     ;

%%

int main() {
    printf("Enter expression:\n");
    yyparse();
    printCode();
    return 0;
}

void printCode() {
    printf("\nQuadruple Code:\n");
    printf("Idx\tOp\tArg1\tArg2\tRes\n");
    for(int i=0;i<idx;i++) {
        printf("%d\t%c\t%c\t%c\t%c\n", i, q[i].op, q[i].arg1, q[i].arg2, q[i].res);
    }

    printf("\nTriple Code:\n");
    printf("Idx\tOp\tArg1\tArg2\n");
    for(int i=0;i<idx;i++) {
        printf("%d\t%c\t%c\t%c\n", i, q[i].op, q[i].arg1, q[i].arg2);
    }

    printf("\nThree Address Code:\n");
    for(int i=0;i<idx;i++) {
        if(q[i].op == '=')
            printf("%c = %c\n", q[i].res, q[i].arg1);
        else
            printf("%c = %c %c %c\n", q[i].res, q[i].arg1, q[i].op, q[i].arg2);
    }
}

void yyerror(const char *s) {
    printf("Invalid\n");
}