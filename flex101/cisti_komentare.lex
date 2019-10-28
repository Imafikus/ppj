%option noyywrap 

%{
    #include <stdio.h>
    #include <stdlib.h>
%}

%%

"{"[^}*]"}" {}
"(*"([^*]|\*+[ˆ)])*\*+")" {}
. {}
\n {}

%%

int main ()
{
    yylex();
    exit(EXIT_SUCCESS);
}