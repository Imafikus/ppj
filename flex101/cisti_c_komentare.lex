%option noyywrap

/*Ime stanja*/
%x comment

%{
    #include <stdio.h>
    #include <stdlib.h>

    int broj_linija = 0;
%}

%%

"/*"    {
            BEGIN(comment);
        }
<comment>[^*\n]* { }
<comment>"*"* { }
<comment>\n { broj_linija++;}

<comment>\*+"/"
        {
            BEGIN(INITIAL);
        }

\n      {broj_linija++;}
.       { }

%%

int main()
{
    yylex();
    exit(EXIT_SUCCESS);
}