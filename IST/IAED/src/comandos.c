/**
 * @file comandos.c
 * @brief Implementação dos comandos do projeto de gestão de vacinas
 * @author [ist1114538 - Guilherme Lourenço]
 */
#include "project.h"
#include "utils.h"
#include "comandos.h"

/**
 * @brief Cria um novo lote de vacinas
 * 
 * @param base Ponteiro para a estrutura Base
 * @param linha String contendo os dados do lote
 * @param lingua Idioma para mensagens de erro
 */
void criar_lote(Base* base, char *linha, int lingua) {
    char nome_vac[MAXNOMEVAC+1], lote[MAXLOTE+1];
    int dia, mes, ano, doses_disponiveis, doses_aplicadas = 0, 
        index = base->cnt;
    char *lote_ptr = NULL, *nome_vac_ptr = NULL;
    sscanf(linha, "%*c %21s %d-%d-%d %d %51s", lote, &dia, &mes, &ano, 
        &doses_disponiveis, nome_vac);
    if (base->cnt >= MAXNUMLOTES) {
        print_erros(lingua, E2MANYVAC, E2MANYVAC_PT);
        return;
    }
    lote_ptr = aloca_memoria(lote, lingua);
    nome_vac_ptr = aloca_memoria(nome_vac, lingua);
    if (lote_ptr == NULL || nome_vac_ptr == NULL) {
        free(lote_ptr);
        free(nome_vac_ptr);
        return;
    }
    if (print_erros_lotes(base, nome_vac, lote, dia, mes, ano,
        doses_disponiveis, lingua)) {
        free(lote_ptr);
        free(nome_vac_ptr);
        return;
    }
    char *novo_nome_vac_ptr = strchr(nome_vac_ptr, '_');
    if (novo_nome_vac_ptr != NULL) {
        printf("invalid character in vaccine name\n");
        free(lote_ptr);
        free(nome_vac_ptr);
        return;
    }
    printf("%s\n", lote_ptr);
    adic_lote(base, lote_ptr, nome_vac_ptr, dia, mes, ano, doses_disponiveis,
        doses_aplicadas, index);
}

/**
 * @brief Avança a data do sistema
 * 
 * @param base Ponteiro para a estrutura Base
 * @param linha String contendo a nova data
 * @param lingua Idioma para mensagens de erro
 */
void avancar_tempo(Base* base, char *linha, int lingua){
    int dia, mes, ano;
    sscanf(linha, "%*c %02d-%02d-%04d", &dia, &mes, &ano);

    if (!verifica_data(dia, mes, ano, base->dia_sistema, base->mes_sistema, 
        base->ano_sistema)) {
        print_erros(lingua, INVDATE, INVDATE_PT);
        return;
    }
    base->dia_sistema = dia;
    base->mes_sistema = mes;
    base->ano_sistema = ano;
    printf("%02d-%02d-%04d\n", dia, mes, ano);
}

/**
 * @brief Lista os lotes de vacinas
 * 
 * @param base Ponteiro para a estrutura Base
 * @param linha String contendo os parâmetros de listagem
 * @param lingua Idioma para mensagens de erro
 */
void lista_lotes(Base* base, char *linha, int lingua) {  
    if (base->cnt == 0) return;
    else if (strlen(linha) == 2) {
        ordena_lotes(base->dados, 0, base->cnt - 1);
        for (int i = 0; i < base->cnt; i++) {
            print_lista_lotes(base, i);
        }
    }
    else {
        aux_lista_lotes(base, linha, lingua);
    }
}

/**
 * @brief Aplica doses de vacina a um utente
 * 
 * @param base Ponteiro para a estrutura Base
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param linha String contendo os dados da aplicação
 * @param lingua Idioma para mensagens de erro
 */
void aplica_doses(Base* base, Base_registos* base_registos, char *linha, 
    int lingua) {    
    char nome_vac[MAXNOMEVAC], *encontrou;
    char *nome_utente = malloc(65523 * sizeof(char));
    int dia = base->dia_sistema, mes = base->mes_sistema, 
        ano = base->ano_sistema;
    encontrou = strchr(linha, '"');
    if (encontrou == NULL) sscanf(linha, "%*c %s %50s", nome_utente, 
        nome_vac);
    else sscanf(linha, "%*c \"%[^\"]\" %50s", nome_utente, nome_vac);

    char *nome_utente_novo = realloc_utente(nome_utente, lingua);
    int i = obtem_lote(base, nome_vac);
    if (i == -1 || base->dados[i].doses_disponiveis <= 0) {
        free(nome_utente_novo);
        print_erros(lingua, NOSTOCK, NOSTOCK_PT);
        return;
    }
    if (verifica_vacinacao(base_registos, nome_utente_novo, nome_vac, 
        dia, mes, ano)){
        free(nome_utente_novo);
        print_erros(lingua, ALREADVACC, ALREADVACC_PT);
        return;
    }
    adicionar_inoculacao(base_registos, nome_utente_novo, base->dados[i].lote, 
        base->dados[i].nome_vac, dia, mes,ano, lingua);
    base->dados[i].doses_disponiveis--;
    base->dados[i].doses_aplicadas++;
    printf("%s\n", base->dados[i].lote);
    free(nome_utente_novo);
}

/**
 * @brief Lista as inoculações realizadas
 * 
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param linha String contendo os parâmetros de listagem
 * @param lingua Idioma para mensagens de erro
 */
void lista_inoculacoes(Base_registos *base_registos, const char *linha, 
    int lingua) {
    char *nome_utente = malloc(65523 * sizeof(char));
    int iguais = 0;

    if (strlen(linha) == 2) {
        aux_lista_inoc_1(base_registos);
        free(nome_utente); 
        return;
    }
    else {
        if (linha[2] == '"') {
            sscanf(linha, "%*c \"%[^\"]\"", nome_utente);
        }
        else {
            sscanf(linha, "%*c %s", nome_utente);
        }
        if (strlen(nome_utente) == 0) {
            print_erros_2(lingua, nome_utente, NOUSER, NOUSER_PT);
            free(nome_utente);
            return;
        }
        char *nome_utente_novo = realloc_utente(nome_utente, lingua);
        iguais = aux_lista_inoc_2(base_registos, nome_utente_novo, iguais);
        if (iguais == 0){
            print_erros_2(lingua, nome_utente_novo, NOUSER, NOUSER_PT);
        }
        free(nome_utente_novo);
    }
}

/**
 * @brief Retira um lote de vacinas do sistema
 * 
 * @param base Ponteiro para a estrutura Base
 * @param linha String contendo o lote a ser retirado
 * @param lingua Idioma para mensagens de erro
 */
void retira_lote(Base* base, char *linha, int lingua){
    char lote[MAXLOTE];
    int iguais = 0;
    sscanf(linha, "%*s %20s", lote);
    for(int i = 0; i < base->cnt; i++){
        if (!strcmp(lote, base->dados[i].lote)){
            iguais = 1;
            printf("%d\n", base->dados[i].doses_aplicadas);
            if (base->dados[i].doses_aplicadas == 0){
                if (i < base->cnt){
                    for (int j = i; j < base->cnt - 1; j++){
                        troca(&base->dados[j], &base->dados[j + 1]);
                    }
                    base->cnt--;
                }
                else base->cnt--;
            }
            else base->dados[i].doses_disponiveis = 0;
            return;
        }
    }
    if (iguais != 1){
        print_erros_2(lingua, lote, NOBATCH, NOBATCH_PT);
        return;
    }
}

/**
 * @brief Apaga o registo de uma inoculação
 * 
 * @param base Ponteiro para a estrutura Base
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param linha String contendo os dados da inoculação a ser apagada
 * @param lingua Idioma para mensagens de erro
 */
void apaga_inoculacao(Base* base, Base_registos* base_registos, char *linha, 
    int lingua){
    char *nome_utente = malloc(65483 * sizeof(char));
    char lote[MAXLOTE];
    int i = 0, dia = 0, mes, ano, num_inoc_apag  = 0;
    int variaveis = sscanf(linha, "d %s %d-%d-%d %s", nome_utente, &dia, &mes, 
        &ano, lote);
    char *nome_utente_novo = realloc_utente(nome_utente, lingua);
    if (verifica_variaveis(base, base_registos, nome_utente_novo, dia, mes,
        ano, lote, variaveis, lingua) == 1) {
        for (i = 0; i < base_registos->num_utentes; i++) {
            if (strcmp(base_registos->utentes[i].nome_utente, nome_utente_novo) == 0) {
                if (variaveis == 1) { //so nome
                    num_inoc_apag = aux_apaga_1(base_registos, i);  
                }
                else if (variaveis > 1){ // nome e data ou nome, data e lote
                    num_inoc_apag = aux_apaga_maior1(base_registos, dia, mes, 
                    ano, lote, variaveis, num_inoc_apag, i);
                }
            }
        }   
    } 
    else{
        free(nome_utente_novo);
        return;
    }
    free(nome_utente_novo);
    printf("%d\n", num_inoc_apag);
    return;
}

void m_comando(Base_registos* base_registos, char *linha){
    char nome_utente[100];
    char nome_utente_novo[100];
    int encontrei = 0;
    sscanf(linha,"m %s %s", nome_utente, nome_utente_novo);
    for (int i = 0; i < base_registos->num_utentes; i++){
        if (strcmp(nome_utente, base_registos->utentes[i].nome_utente) == 0){
            encontrei = 1;
        }
    }
    if (encontrei == 0){
        printf("nome_utente: no such user");
    }

}
