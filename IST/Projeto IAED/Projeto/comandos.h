#include "project.h"

void criar_lote(Base* base, char *linha, int lingua);
void avancar_tempo(Base* base, char *linha, int lingua);
void lista_lotes(Base* base, char *linha, int lingua);
void aplica_doses(Base* base, Base_registos* base_registos, 
    char *linha, int lingua);
void lista_inoculacoes(Base_registos *base_registos, const char *linha, 
    int lingua);
void retira_lote(Base* base, char *linha, int lingua);
void apaga_inoculacao(Base* base, Base_registos* base_registos, char *linha, 
    int lingua);