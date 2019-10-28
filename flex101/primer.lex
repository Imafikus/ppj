/*Opcije za konacni automati*/
%option noyywrap


%{
    // deo C koda koji hocemo da kopiramo
    #include<stdio.h>
    #include<stdlib.h>

    int num_chars = 0;
    int num_lines = 0;
%}

/* razdvajamo delove dokumenta sa %% */
/* ovde ide regex %% */
%%
    /* prepoznajemo novi red */
\n {num_chars++; num_lines++;}
. {num_chars++; }

    /* regex koji je prvo definisan je najviseg prioriteta*/
%%

/* ovde je main koji izvrsavamo */
int main() 
{
    yylex(); // jedina stvar koju pravu lex
    printf("Ukupno karaktera: %d\nUkupno linija: %d\n", num_chars, num_lines);
    exit(EXIT_SUCCESS);
}