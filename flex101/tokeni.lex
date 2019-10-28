%option noyywrap

%{
    #include<stdio.h>
    #include<stdlib.h>

    #define KLJUCNA_REC     (1)
    #define ID              (2)
    #define INTERPUNKCIJA   (3)
    #define DODELA          (6)
    #define I_CONST         (7)
    #define F_CONST         (8)
    #define OP              (9)
    #define ROP             (10)
    #define NN              (11)
    #define ZAGRADE         (12)
%}

DIGIT   [0-9]
ID      [a-z][a-z0-9]*

%%
if|then|begin|var|end|integer   {return KLJUCNA_REC;}
{ID}                            {return ID;}
{DIGIT}+                        {return I_CONST;}
{DIGIT}+\.{DIGIT}*              {return F_CONST;}
[+*/-]                          {return OP;}
[<>=]|">="|"<="                 {return ROP;}
:=                              {return DODELA;}
[.:;,]                          {return INTERPUNKCIJA;}
"("|")"                         {return ZAGRADE;}
[ \t\n]                         { }
.                               {
                                    fprintf(stderr, "Leksicka greska\n %s", yytext);
                                    exit(EXIT_FAILURE);
                                }
%%

int main(int argc, char** argv) 
{
    int token;
    if(argc > 1) {
        yyin = fopne(argv[1], "r");
        if (yyin == NULL) {
            exit(EXIT_FAILURE)
        }
    }
    ... POGLEDATI SA SAJTA
}