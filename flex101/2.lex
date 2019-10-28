%option noyywrap


/*gledamo broj  zagrada koje su ostale otvorene*/
%{
    #include <stdio.h>
    #include <stdlib.h>

    int broj_otvorenih = 0;
%}

/*{} ovo ce samo da ignorise takve znakove*/
/*ECHO ce da stampa prepoznate karaktere*/

%%

"(" {broj_otvorenih++;}
")" {broj_otvorenih--;}
\n {ECHO;}
. {ECHO;}
%%
int main()
{
    yylex();
    if(broj_otvorenih == 0) {
        printf("Zagrade su uparene\n");
    }
    else {
        printf("Zagrade nisu uparene\n");
    }
    exit(EXIT_SUCCESS);
}