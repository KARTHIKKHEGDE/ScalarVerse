%{
#include "y.tab.h"
%}

%%

"for"      { return FOR; }
"("        { return LPAREN; }
")"        { return RPAREN; }
"{"        { return LF; }
"}"        { return RF; }

"=="       { return EQ; }
"<="       { return LE; }
">="       { return GE; }
"+="       { return ADDEQ; }
"-="       { return SUBEQ; }
"++"       { return INC; }
"--"       { return DEC; }

"="        { return '='; }
">"        { return '>'; }
"<"        { return '<'; }
"+"        { return '+'; }
"-"        { return '-'; }
";"        { return ';'; }

[a-zA-Z]+  { return ALPH; }
[0-9]+     { return NUM; }

[ \t\n]    ;

#          { return 0; }

.          ;

%%

int yywrap(){
    return 1;
}

//3.a.y
%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror();

int depth = 0;
int maxDepth = 0;
int count = 0;
%}

%token FOR LPAREN RPAREN LF RF ALPH NUM EQ LE GE ADDEQ SUBEQ INC DEC

%%

S : FORSTMT {
        if(maxDepth >= 3){
            printf("Valid\n");
            printf("Number of nested FOR's are: %d\n", count);
        } else {
            printf("Invalid\n");
        }
    }
  ;

FORSTMT :
    FOR A LF {
        depth++;
        count++;
        if(depth > maxDepth) maxDepth = depth;
    }
    BODY
    RF {
        depth--;
    }
;

BODY :
    FORSTMT BODY
  | /* empty */
;

A : LPAREN E ';' E ';' E RPAREN ;

E :
    ALPH Z NUM
  | ALPH Z ALPH
  | ALPH U
  | /* empty */
;

Z :
    '=' | '>' | '<' | LE | GE | EQ | ADDEQ | SUBEQ
;

U :
    INC | DEC
;

%%

int main(){
    printf("Enter code (end with #):\n");
    yyparse();
    return 0;
}

void yyerror(){
    printf("Invalid\n");
    exit(0);
}

//3.b.l
%{
#include "y.tab.h"
%}

%%

"int"|"void"|"char"|"float"|"double"   { return TYP; }
"return"                               { return RETURN; }

[a-zA-Z_][a-zA-Z0-9_]*                 { return ID; }
[0-9]+                                 { return NUM; }

"("                                    { return LP; }
")"                                    { return RP; }
"{"                                    { return LB; }
"}"                                    { return RB; }

";"                                    { return SC; }
","                                    { return CM; }

"="                                    { return EQ; }
"+"|"-"|"*"|"/"                        { return OP; }

[ \t\n]                                ;
.                                      ;

%%

int yywrap(void) {
    return 1;
}

//3.b.y

%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);
%}

%token TYP ID LP RP LB RB SC CM EQ OP RETURN NUM

%left OP
%right EQ

%%

prog : func
     ;

func : TYP ID LP params RP LB stmts RB
      { printf("Function is syntactically correct\n"); }
     ;

params : /* empty */
       | param_list
       ;

param_list : param
           | param_list CM param
           ;

param : TYP ID
      ;

stmts : stmt
      | stmts stmt
      ;

stmt : var_decl
     | assign SC
     | RETURN expr SC
     ;

var_decl : TYP ID SC
         | TYP ID EQ expr SC
         ;

assign : ID EQ expr
       ;

expr : expr OP expr
     | LP expr RP
     | ID
     | NUM
     ;

%%

int main() {
    printf("Enter function:\n");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    printf("Invalid function\n");
    exit(0);
}