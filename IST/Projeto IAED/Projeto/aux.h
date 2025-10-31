#include "project.h"

int hex_valido(const char* str);
int verifica_bissexto(int ano);
int verifica_data(int dia, int mes, int ano, int dia_atual, 
    int mes_atual, int ano_atual);
void print_erros(int lingua, char *erro, char *erro_pt);
void print_erros_2(int lingua, char *var, char *erro, char *erro_pt);
int compara_datas(Lote_da_vacina *lote1, Lote_da_vacina *lote2);
int print_erros_lotes(Base *base, char nome_vac[], char lote[], int dia,
    int mes, int ano, int doses_disponiveis, int lingua);
char * aloca_memoria(char *str, int lingua);
void adic_lote(Base* base, char *lote_ptr, char *nome_vac_ptr, int dia, 
    int mes, int ano, int doses_disponiveis, int doses_aplicadas, int index);
void troca(Lote_da_vacina *a, Lote_da_vacina *b);
int parte(Lote_da_vacina *lotes, int esq, int dir);
void ordena_lotes(Lote_da_vacina *lotes, int esq, int dir);
void print_lista_lotes(Base* base, int i);
void aux_lista_lotes(Base* base, char *linha, int lingua);
int obtem_lote(Base* base, char *nome_vac);
char* realloc_utente(char *nome_utente, int lingua);
void aux_lista_inoc_1(Base_registos *base_registos);
int aux_lista_inoc_2(Base_registos *base_registos, char *nome_utente_novo, 
    int iguais);
void inic_novo_utente(Base_registos *base_registos, char *nome_utente, 
    int indice, int lingua);
void adicionar_utente(Base_registos *base_registos, int indice_inoc, 
    char *lote, char *nome_vac, int dia, int mes, int ano, 
    int indice, int lingua);
void adicionar_inoculacao(Base_registos *base_registos, 
    const char *nome_utente,char *lote, const char *nome_vac, int dia,
    int mes, int ano, int lingua);
int verifica_vacinacao(Base_registos *base_registos, const char *nome_utente, 
    const char *nome_vac, int dia, int mes, int ano);
int compara_inoculacoes(const Registo_inoc *a, 
    const Registo_inoc *b);
void ordena_inoculacoes(Registo_inoc *inoculacoes, int num_inoculacoes);
void print_inoculacoes(Base_registos *base_registos, int i, int j);
int compara_datas_inoculacao(int dia1, int mes1, int ano1, int dia2, 
    int mes2, int ano2);
int verifica_data_inoculacao(int dia, int mes, int ano, int dia_atual, 
    int mes_atual, int ano_atual);
int verifica_variaveis(Base *base, Base_registos *base_registos, 
    char *nome_utente, int dia, int mes, int ano, char *lote, int variaveis, 
    int lingua);
int verifica_variaveis(Base *base, Base_registos *base_registos, 
    char *nome_utente, int dia, int mes, int ano, char *lote, 
    int variaveis, int lingua);
int aux_apaga_1(Base_registos* base_registos, int i);
int aux_apaga_maior1(Base_registos* base_registos, int dia, int mes, int ano,
    char *lote, int variaveis, int num_inoc_apag, int i);
void switch_comandos(Base *base, Base_registos *base_registos, char *linha,
    int lingua);
void cleanup(Base *base, Base_registos *base_registos);
int compara_datas_inversa(Lote_da_vacina *lote1, Lote_da_vacina *lote2);
