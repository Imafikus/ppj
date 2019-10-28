%option noyywrap

%{
    #include<stdio.h>
    #include<stlib.h>
    #include <string.h>

    int vrednost;
%}


hiljade M+
stotine C+|CD|DC*|CM
desetice X+|XL|LX*| CX
jedinice I+|IV|VI*|IX

%%
{hiljade}   {vrednost += 1000 * yyleng;}
{stotine}   {
                if (strcmp(yytext, "CM") == 0) {
                    vrednost += 900;
                }
                else if (strcmp(yytext, "CD") == 0) {
                    vrednost += 400;
                }
                else {
                    if (yytext[0] == 'D') {
                        vrednost += 500;
                        if (yyleng <= 4) {
                            vrednost += 100 * (yyleng - 1);
                        }
                        else {
                            printf("Pogresan format broja\n");
                            exit(EXIT_SUCCESS);
                        }
                    }
                    else if (yytext[0] == 'C') {
                        if (yyleng <= 3) {
                            vrednost += 100 * yyleng;
                        }
                        else {
                            printf("Pogresan format broja\n");
                            exit(EXIT_SUCCESS);
                        }
                    }
                }
            }

{desetice} {
    c / p ceo kod, pogledati kod njega na sajtu
}
%%