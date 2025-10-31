#ifndef PROJECT_H
#define PROJECT_H
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h> 
#include <string.h>

#define MAXLOTE 21  
#define MAXNUMLOTES 1000
#define MAXNOMEVAC 51
#define MAXBUFFER 65536
#define MAXNUMUTENTES 250
#define MAXNUMINOCULACOES 100


/*ERROS EM INGLÊS*/
#define E2MANYVAC "too many vaccines"
#define EDUPBATCH "duplicate batch number"
#define INVBATCH "invalid batch"
#define INVNAME "invalid name"
#define INVDATE "invalid date"
#define INVQUANT "invalid quantity"
#define NOVACCINE "no such vaccine"
#define NOSTOCK "no stock"
#define ALREADVACC "already vaccinated"
#define NOBATCH "no such batch"
#define NOUSER "no such user"
#define NOMEMORY "no memory"

//ERROS EM PORTUGUÊS
#define E2MANYVAC_PT "demasiadas vacinas"
#define EDUPBATCH_PT "número de lote duplicado"
#define INVBATCH_PT "lote inválido"
#define INVNAME_PT "nome inválido"
#define INVDATE_PT "data inválida"
#define INVQUANT_PT "quantidade inválida"
#define NOVACCINE_PT "vacina inexistente"
#define NOSTOCK_PT "esgotado"
#define ALREADVACC_PT "já vacinado"
#define NOBATCH_PT "lote inexistente"
#define NOUSER_PT "utente inexistente"
#define NOMEMORY_PT "sem memória"

/*ESTRUTURAS*/

/*ESTRUTURA DOS LOTES*/
typedef struct {
    char *lote;
    int dia, mes, ano;
    int doses_disponiveis;
    int doses_aplicadas;
    char *nome_vac; 
} Lote_da_vacina;

/*ESTRUTURA DA BASE DE DADOS*/
typedef struct {
    int cnt;
    Lote_da_vacina dados[MAXNUMLOTES];
    int dia_sistema, mes_sistema, ano_sistema; 
} Base;

/*ESTRUTURA DOS REGISTOS DE INOCULAÇÕES*/
typedef struct {
    char lote[MAXLOTE];
    char nome_vac[MAXNOMEVAC];
    int dia, mes, ano;
} Registo_inoc;

/*ESTRUTURA DOS UTENTES*/
typedef struct {
    char *nome_utente; 
    Registo_inoc *inoculacoes; 
    int limite_inoculacoes;
    int num_inoculacoes; 
} Usuario;

/*ESTRUTURA DA BASE DE REGISTOS*/
typedef struct {
    Usuario *utentes; 
    int limite_utentes;
    int num_utentes;
} Base_registos;

#endif