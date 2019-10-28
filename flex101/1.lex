%option noyywrap 
/*zaustavlja se kad dodje do kraja fajla*/


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
    /* { posle regexa mora da bude u istom redu, ne sme da bude ispod, u {} ide klasican C kod*/
    regex {akcija}

    /* regex koji je prvo definisan je najviseg prioriteta*/

%%