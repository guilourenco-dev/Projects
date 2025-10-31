/**
 * @file aux.c
 * @brief Este ficheiro contém funções auxiliares para o programa de vacinação.
 * @author [ist1114538 - Guilherme Lourenço]
 */
#include "project.h"
#include "aux.h"
#include "comandos.h"

/**
 * @brief Verifica se uma string contém apenas caracteres hexadecimais.
 *
 * @param str A string a ser verificada.
 * @return 1 se a string for um hexadecimal válido, 0 caso contrário.
 */
int hex_valido(const char* str) {
    if (str == 0 || str[0] == '\0') {
        return 0; 
    }

    for (int i = 0; str[i] != '\0'; i++) {
        if (!isxdigit(str[i]) || islower(str[i])) {
            return 0; 
        }
    }
    if (strlen(str) > 20){
        return 0; 
    }
    return 1; 
}

/**
 * @brief Determina o número de dias em Fevereiro para um determinado ano, considerando anos bissextos.
 *
 * @param ano O ano a ser verificado.
 * @return 29 se o ano for bissexto, 28 caso contrário.
 */
int verifica_bissexto(int ano) {
    if (!(ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0))) {
       return 28; 
    }
    return 29;
}

/**
 * @brief Verifica se uma data fornecida é válida e não está no passado.
 *
 * @param dia O dia da data.
 * @param mes O mês da data.
 * @param ano O ano da data.
 * @param dia_atual O dia atual.
 * @param mes_atual O mês atual.
 * @param ano_atual O ano atual.
 * @return 1 se a data for válida e não estiver no passado, 0 caso contrário.
 */
int verifica_data(int dia, int mes, int ano, int dia_atual, 
    int mes_atual, int ano_atual) {
    int dia_max, bissexto;

    bissexto = verifica_bissexto(ano);

    dia_max = mes == 2 ? bissexto : (mes % 2 == 0 ? 30 : 31);
    if (dia < 1 || dia > dia_max || mes < 1 || mes > 12 || ano < 0) {
        return 0;
    }

    if (ano < ano_atual || (ano == ano_atual && mes < mes_atual) 
        || (ano == ano_atual && mes == mes_atual && dia < dia_atual)) {
        return 0;
    }
    return 1;
}  

/**
 * @brief Imprime uma mensagem de erro com base na língua selecionada.
 *
 * @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
 * @param erro A mensagem de erro em Inglês.
 * @param erro_pt A mensagem de erro em Português.
 */
void print_erros(int lingua, char *erro, char *erro_pt){
    if (lingua == 0)    
        puts(erro);
    else{
        puts(erro_pt);
    }
}

/**
 * @brief Imprime uma mensagem de erro com o nome de uma variável, com base na língua selecionada.
 *
 * @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
 * @param var O nome da variável a incluir na mensagem.
 * @param erro A mensagem de erro em Inglês.
 * @param erro_pt A mensagem de erro em Português.
 */
void print_erros_2(int lingua, char *var, char *erro, char *erro_pt){
    if (lingua == 0)    
        printf("%s: %s\n", var, erro);
    else{
        printf("%s: %s\n", var, erro_pt);
    }
}

/**
 * @brief Compara duas datas representadas por estruturas Lote_da_vacina.
 *
 * @param lote1 Ponteiro para a primeira estrutura Lote_da_vacina.
 * @param lote2 Ponteiro para a segunda estrutura Lote_da_vacina.
 * @return -1 se a data de lote1 for anterior, 1 se a data de lote1 for posterior, 0 se as datas forem iguais.
 */
int compara_datas(Lote_da_vacina *lote1, Lote_da_vacina *lote2) {
    int dia1 = lote1->dia, mes1 = lote1->mes, ano1 = lote1->ano;
    int dia2 = lote2->dia, mes2 = lote2->mes, ano2 = lote2->ano;
    
    if (ano1 < ano2 || (ano1 == ano2 && mes1 < mes2) 
        || (ano1 == ano2 && mes1 == mes2 && dia1 < dia2)) 
        return -1;
    else if (ano1 > ano2 || (ano1 == ano2 && mes1 > mes2) 
        || (ano1 == ano2 && mes1 == mes2 && dia1 > dia2)) 
        return 1;
    else    
        return 0;
}

/**
 * @brief Verifica os parâmetros de criação de um lote de vacinas.
 *
 * @param base Um ponteiro para a estrutura Base que contém os dados dos lotes de vacina.
 * @param nome_vac O nome da vacina.
 * @param lote O lote de vacina.
 * @param dia O dia da data de inoculação.
 * @param mes O mês da data de inoculação.
 * @param ano O ano da data de inoculação.
 * @param doses_disponiveis O número de doses disponíveis.
 * @param lingua O indicador de inglês ou português.
 * @return 0 se os parâmetros forem válidos, 1 caso contrário.
 */
int print_erros_lotes(Base *base, char nome_vac[], char lote[], int dia, 
    int mes, int ano, int doses_disponiveis, int lingua) {
    if (!hex_valido(lote)) {
        print_erros(lingua, INVBATCH, INVBATCH_PT);
        return 1;
    }
    if (!verifica_data(dia, mes, ano, base->dia_sistema, base->mes_sistema, 
        base->ano_sistema)) {
        print_erros(lingua, INVDATE, INVDATE_PT);
        return 1;
    }
    if (doses_disponiveis < 0) {
        print_erros(lingua, INVQUANT, INVQUANT_PT);
        return 1;
    }
    if (strlen(nome_vac) == 0 || strlen(nome_vac) > 50) {
        print_erros(lingua, INVNAME, INVNAME_PT);
        return 1;
    }
    for (int i = 0; i < base->cnt; i++) {
        if (!strcmp(lote, base->dados[i].lote)) {
            print_erros(lingua, EDUPBATCH, EDUPBATCH_PT);
            return 1;
        }
    }
    return 0;
}

/**
 * @brief Aloca memória para uma string.
 *  
 * @param str A string a ser alocada.
 * @param lingua O indicador de inglês ou português.
 * @return A string alocada.
 */
char * aloca_memoria(char *str, int lingua) {
    char *str_ptr = strdup(str);
    if (str_ptr == NULL) {
        print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        free(str_ptr);
        return NULL;
    }
    return str_ptr;
}

/**
 * @brief Adiciona um lote de vacina na estrutura Base
 * 
 * @param base Ponteiro para a estrutura Base
 * @param lote_ptr Ponteiro para o lote de vacina   
 * @param nome_vac_ptr Ponteiro para o nome da vacina
 * @param dia Dia da data de inoculação
 * @param mes Mês da data de inoculação
 * @param ano Ano da data de inoculação
 * @param doses_disponiveis Número de doses disponíveis
 * @param doses_aplicadas Número de doses aplicadas
 * @param index Index do lote na estrutura Base
 */
void adic_lote(Base* base, char *lote_ptr, char *nome_vac_ptr, int dia, 
    int mes, int ano, int doses_disponiveis, int doses_aplicadas, int index){
    base->dados[index].lote = lote_ptr;
    base->dados[index].dia = dia;
    base->dados[index].mes = mes;
    base->dados[index].ano = ano;
    base->dados[index].doses_disponiveis = doses_disponiveis;
    base->dados[index].doses_aplicadas = doses_aplicadas;
    base->dados[index].nome_vac = nome_vac_ptr;
    base->cnt++;
}

/**
 * @brief Troca o conteúdo de duas estruturas Lote_da_vacina.
 *
 * @param a Ponteiro para a primeira estrutura Lote_da_vacina.
 * @param b Ponteiro para a segunda estrutura Lote_da_vacina.
 */
void troca(Lote_da_vacina *a, Lote_da_vacina *b) {
    Lote_da_vacina temporario = *a;
    *a = *b;
    *b = temporario;
}

/**
 * @brief Particiona um array de estruturas Lote_da_vacina para o algoritmo de sort.
 *
 * @param lotes O array de estruturas Lote_da_vacina.
 * @param esq O índice inicial da partição.
 * @param dir O índice final da partição.
 * @return O índice do elemento pivot após a partição.
 */
int parte(Lote_da_vacina *lotes, int esq, int dir) {
    Lote_da_vacina pivot = lotes[dir]; 
    int i = esq - 1;

    for (int j = esq; j <= dir - 1; j++) {
        if (compara_datas(&lotes[j], &pivot) < 0) {
            i++;
            troca(&lotes[i], &lotes[j]);
        }
        else if (compara_datas(&lotes[j], &pivot) == 0) {
            if (strcmp(lotes[j].lote, pivot.lote) < 0) {
                i++;
                troca(&lotes[i], &lotes[j]);
            }
        }
        
    }
    troca(&lotes[i + 1], &lotes[dir]);
    return (i + 1);
}

/**
 * @brief Ordena um array de estruturas Lote_da_vacina usando o algoritmo de sort.
 *
 * @param lotes O array de estruturas Lote_da_vacina.
 * @param esq O índice inicial do array.
 * @param dir O índice final do array.
 */
void ordena_lotes(Lote_da_vacina *lotes, int esq, int dir) {
    if (esq < dir) {
        int index_pivot = parte(lotes, esq, dir);
        ordena_lotes(lotes, esq, index_pivot - 1);
        ordena_lotes(lotes, index_pivot + 1, dir);
    }
}

/**
 * @brief Imprime as informações de um lote de vacina.
 *
 * @param base Um ponteiro para a estrutura Base que contém os dados dos lotes de vacina.
 * @param i O índice do lote de vacina a ser impresso.
 */
void print_lista_lotes(Base* base, int i) {
    printf("%s %s %02d-%02d-%04d %d %d\n", base->dados[i].nome_vac,
        base->dados[i].lote, base->dados[i].dia, base->dados[i].mes, 
        base->dados[i].ano, base->dados[i].doses_disponiveis, 
        base->dados[i].doses_aplicadas);
}

/**
* @brief Função auxiliar para imprimir a lista de lotes de vacinas com base em uma linha de entrada.
* 
* @param base Um ponteiro para a estrutura Base que contém os dados dos lotes de vacina.
* @param linha A linha de entrada contendo os nomes das vacinas.
* @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
*/
void aux_lista_lotes(Base* base, char *linha, int lingua) {
    int encontrou = 0;
    char* linha_cp = strdup(linha + 1); 
    char* nova_linha = strchr(linha_cp, '\n');
    if (nova_linha) *nova_linha = '\0';
    char* ptr_temp;
    char* token = strtok_r(linha_cp, " ", &ptr_temp);
    while (token != NULL) {
        encontrou = 0;
        for (int i = 0; i < base->cnt; i++) {
            if (strcmp(base->dados[i].nome_vac, token) == 0) {
                print_lista_lotes(base, i);
                encontrou = 1;
            }
        }
        if (!encontrou) {
            print_erros_2(lingua, token, NOVACCINE, NOVACCINE_PT);  
        }
        token = strtok_r(NULL, " ", &ptr_temp);
    }
    free(linha_cp);
}

/**
 * @brief Obtém o índice de um lote de vacina adequado com base no nome da vacina.
 *
 * @param base Ponteiro para a estrutura Base contendo os dados da vacina.
 * @param nome_vac O nome da vacina.
 * @return O índice do lote adequado, ou -1 se nenhum lote adequado for encontrado.
 */
int obtem_lote(Base* base, char *nome_vac) {
    int iguais = 0, j = 0, dia = base->dia_sistema, mes = base->mes_sistema,
    ano = base->ano_sistema;
    int lotes_iguais[MAXNOMEVAC] = {0};
    ordena_lotes(base->dados, 0, base->cnt - 1);
    for (int i = 0; i < base->cnt; i++) {
        if (strcmp(base->dados[i].nome_vac, nome_vac) == 0) {
            lotes_iguais[j++] = i;
            iguais++;
        }
    }
    if (iguais > 1) {
        int min = lotes_iguais[0];
        for (j = 1; j < iguais; j++) {
            if (lotes_iguais[j] < min) min = lotes_iguais[j];
        }
        for (int cnt = 1; cnt < iguais; cnt++) {
            if (base->dados[min].doses_disponiveis > 0 && 
                verifica_data(base->dados[min].dia, base->dados[min].dia, 
                base->dados[min].dia, dia, mes, ano) == 0) 
                    break;
            min = lotes_iguais[cnt];
        }
        return min;
    } else if (iguais == 1) 
        return lotes_iguais[0];
    return -1;
}

/**
 * @brief Realoca a memória para o nome do utente.
 *
 * @param nome_utente O nome do utente atual.
 * @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
 * @return O novo ponteiro para o nome do utente, ou NULL se a alocação de memória falhar.
 */
char* realloc_utente(char *nome_utente, int lingua) {
    size_t len = strlen(nome_utente);
    char* nome_utente_novo = realloc(nome_utente, (len + 1) * sizeof(char));
    if (nome_utente_novo == NULL) {
        free(nome_utente_novo);
        print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        return NULL;
    }
    return nome_utente_novo;
}

/**
 * @brief Lista as inoculações realizadas
 * 
 * @param base_registos Ponteiro para a estrutura Base_registos
 */
void aux_lista_inoc_1(Base_registos *base_registos) {
     for (int i = base_registos->num_utentes - 1; i >= 0 ; i--) {
            if (base_registos->utentes[i].num_inoculacoes == 0) {
                continue;
            }
            ordena_inoculacoes(base_registos->utentes[i].inoculacoes, 
            base_registos->utentes[i].num_inoculacoes);
            for (int j = base_registos->utentes[i].num_inoculacoes; j >= 0 ; j--){
                if (base_registos->utentes[i].inoculacoes[j].dia == 0){
                    continue;
                }
                else {
                    print_inoculacoes(base_registos, i, j);
                }
            }
        }
}

/**
 * @brief Lista as inoculações realizadas
 * 
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param nome_utente_novo Nome do utente
 * @param iguais Indica se o utente tem inoculações iguais
 * @return int Indica se o utente tem inoculações iguais
 */
int aux_lista_inoc_2(Base_registos *base_registos, char *nome_utente_novo, 
    int iguais) {
    for (int i = base_registos->num_utentes - 1; i >= 0; i--) {
        if (strcmp(base_registos->utentes[i].nome_utente, nome_utente_novo) == 0) {
            if (base_registos->utentes[i].num_inoculacoes == 0) {
                continue;
            }
            else {
                ordena_inoculacoes(base_registos->utentes[i].inoculacoes, 
                base_registos->utentes[i].num_inoculacoes);
                iguais = 1;
                for (int j = base_registos->utentes[i].num_inoculacoes - 1; j >= 0; j--) {
                    print_inoculacoes(base_registos, i, j);
                } 
            }
        }
    }
    return iguais;
}

/**
* @brief Inicializa um novo utente na base de registos.
* 
* @param base_registos Um ponteiro para a estrutura Base_registos que contém os dados dos utentes.
* @param nome_utente O nome do novo utente a ser adicionado.
* @param indice O índice do novo utente na estrutura Base_registos.
* @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
*/
void inic_novo_utente(Base_registos *base_registos, char *nome_utente, 
    int indice, int lingua){
    base_registos->utentes[indice].nome_utente = 
        malloc((strlen(nome_utente) + 1) * sizeof(char));
        if (base_registos->utentes[indice].nome_utente == NULL){
            print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        }
        strcpy(base_registos->utentes[indice].nome_utente, nome_utente);
        base_registos->utentes[indice].limite_inoculacoes = 0;
        base_registos->utentes[indice].num_inoculacoes = 0;
        base_registos->utentes[indice].inoculacoes = NULL;
        base_registos->utentes[indice].limite_inoculacoes = 0;
        base_registos->utentes[indice].limite_inoculacoes = MAXNUMINOCULACOES;
        base_registos->utentes[indice].inoculacoes = 
            malloc(base_registos->utentes[indice].limite_inoculacoes * 
                sizeof(Registo_inoc));
        if (base_registos->utentes[indice].inoculacoes == NULL){
            free(base_registos->utentes[indice].nome_utente);
            print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        }
        base_registos->utentes[indice].num_inoculacoes = 0;
        base_registos->num_utentes++;
}

/**
* @brief Adiciona um novo registro de inoculação a um utente.
* 
* @param base_registos Um ponteiro para a estrutura Base_registos que contém os dados dos utentes.
* @param indice_inoc O índice do novo registro de inoculação a ser adicionado.
* @param lote O número do lote da vacina.
* @param nome_vac O nome da vacina.
* @param dia O dia da inoculação.
* @param mes O mês da inoculação.
* @param ano O ano da inoculação.
* @param indice O índice do utente na estrutura Base_registos.
* @param lingua A língua a ser usada (0 para Inglês, outro valor para Português). 
*/
void adicionar_utente(Base_registos *base_registos, int indice_inoc, 
    char *lote, char *nome_vac, int dia, int mes, int ano, 
    int indice, int lingua){
    if (indice_inoc >= base_registos->utentes[indice].limite_inoculacoes) {
        base_registos->utentes[indice].limite_inoculacoes *= 2;
        base_registos->utentes[indice].inoculacoes = 
            realloc(base_registos->utentes[indice].inoculacoes, 
        base_registos->utentes[indice].limite_inoculacoes * 
            sizeof(Registo_inoc));
        if (base_registos->utentes[indice].inoculacoes == NULL) {
            print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        }
    }
    strcpy(base_registos->utentes[indice].inoculacoes[indice_inoc].lote, lote);
    strcpy(base_registos->utentes[indice].inoculacoes[indice_inoc].nome_vac, 
        nome_vac);
    base_registos->utentes[indice].inoculacoes[indice_inoc].dia = dia;
    base_registos->utentes[indice].inoculacoes[indice_inoc].mes = mes;
    base_registos->utentes[indice].inoculacoes[indice_inoc].ano = ano;
    base_registos->utentes[indice].num_inoculacoes++;
}

/**
 * @brief Adiciona uma nova inoculação à base de registos
 *
 * Esta função adiciona uma nova inoculação para um utente específico. Se o utente
 * não existir, cria um novo registro. Caso contrário, adiciona a inoculação ao
 * utente existente.
 *
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param nome_utente Nome do utente
 * @param lote Número do lote da vacina
 * @param nome_vac Nome da vacina
 * @param dia Dia da inoculação
 * @param mes Mês da inoculação
 * @param ano Ano da inoculação
 * @param lingua Idioma para mensagens de erro
 */
void adicionar_inoculacao(Base_registos *base_registos, 
    const char *nome_utente,char *lote, const char *nome_vac, int dia, 
    int mes, int ano, int lingua) {
    int indice = -1;
    for (int i = 0; i < base_registos->num_utentes; i++) {
        if (strcmp(base_registos->utentes[i].nome_utente, nome_utente) == 0){
            indice = i;
            break;
        }
    }
    if (indice == -1) { // Novo usuario
        // Inicializa novo usuario
        indice = base_registos->num_utentes;
        inic_novo_utente(base_registos, (char *) nome_utente, indice, lingua);
    }
    // Adiciona inoculacao
    if (base_registos->num_utentes >= base_registos->limite_utentes) {
        base_registos->limite_utentes *= 2;
        base_registos->utentes = realloc(base_registos->utentes, 
            base_registos->limite_utentes * sizeof(Usuario));
        if (base_registos->utentes == NULL) {
            print_erros(lingua, NOMEMORY, NOMEMORY_PT);
        }
    }
    int indice_inoc = base_registos->utentes[indice].num_inoculacoes;  
    adicionar_utente(base_registos, indice_inoc,
        (char *) lote, (char *) nome_vac, dia, mes, ano, indice, lingua);
}

/**
 * @brief Verifica se um utente recebeu uma vacina específica em uma data específica
 *
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param nome_utente Nome do utente a ser verificado
 * @param nome_vac Nome da vacina a ser verificada
 * @param dia Dia da inoculação
 * @param mes Mês da inoculação
 * @param ano Ano da inoculação
 * @return 1 se a vacinação for encontrada, 0 caso contrário
 */
int verifica_vacinacao(Base_registos *base_registos, const char *nome_utente, 
    const char *nome_vac, int dia, int mes, int ano) {
    for (int i = 0; i < base_registos->num_utentes; i++) {
        if (strcmp(base_registos->utentes[i].nome_utente, nome_utente) == 0) {
            if (base_registos->utentes[i].num_inoculacoes == 0) {
                return 0;
            }
            for (int j = 0; j < base_registos->utentes[i].num_inoculacoes;
                j++){
                if (strcmp(base_registos->utentes[i].inoculacoes[j].nome_vac, 
                    nome_vac) == 0 &&
                    base_registos->utentes[i].inoculacoes[j].dia == dia &&
                    base_registos->utentes[i].inoculacoes[j].mes == mes &&
                    base_registos->utentes[i].inoculacoes[j].ano == ano) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

/**
 * @brief Compara duas inoculações por data
 *
 * @param a Ponteiro para a primeira inoculação
 * @param b Ponteiro para a segunda inoculação
 * @return Valor negativo se a < b, positivo se a > b, zero se iguais
 */
int compara_inoculacoes(const Registo_inoc *a, 
    const Registo_inoc *b){
    if (a->ano != b->ano) {
        return a->ano - b->ano; 
    }
    if (a->mes != b->mes) {
        return a->mes - b->mes; 
    }
    return a->dia - b->dia; 
}

/**
 * @brief Ordena as inoculações por data
 *
 * Utiliza o algoritmo de ordenação bubble sort para ordenar as inoculações
 * em ordem cronológica.
 *
 * @param inoculacoes Array de inoculações a ser ordenado
 * @param num_inoculacoes Número de inoculações no array
 */
void ordena_inoculacoes(Registo_inoc *inoculacoes, int num_inoculacoes){
    for (int i = 0; i < num_inoculacoes - 1; i++) {
        for (int j = 0; j < num_inoculacoes - i - 1; j++) {
            if (compara_inoculacoes(&inoculacoes[j], 
                &inoculacoes[j + 1]) > 0){
                Registo_inoc temp = inoculacoes[j];
                inoculacoes[j] = inoculacoes[j + 1];
                inoculacoes[j + 1] = temp;
            }
        }
    }
}

/**
 * @brief Imprime os detalhes de uma inoculação
 *
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param i Índice do utente
 * @param j Índice da inoculação
 */
void print_inoculacoes(Base_registos *base_registos, int i, int j) {
    printf("%s %s %02d-%02d-%04d\n", 
        base_registos->utentes[i].nome_utente, 
        base_registos->utentes[i].inoculacoes[j].lote,
        base_registos->utentes[i].inoculacoes[j].dia,
        base_registos->utentes[i].inoculacoes[j].mes,
        base_registos->utentes[i].inoculacoes[j].ano);
}

/**
 * @brief Compara duas datas de inoculação
 *
 * @param dia1 Dia da primeira data
 * @param mes1 Mês da primeira data
 * @param ano1 Ano da primeira data
 * @param dia2 Dia da segunda data
 * @param mes2 Mês da segunda data
 * @param ano2 Ano da segunda data
 * @return int Retorna -1 se a primeira data for anterior, 1 se for posterior, ou 0 se forem iguais
 */
int compara_datas_inoculacao(int dia1, int mes1, int ano1, int dia2, 
    int mes2, int ano2) {
    if (ano1 < ano2 || (ano1 == ano2 && mes1 < mes2) 
        || (ano1 == ano2 && mes1 == mes2 && dia1 < dia2)) 
        return -1;
    else if (ano1 > ano2 || (ano1 == ano2 && mes1 > mes2) 
        || (ano1 == ano2 && mes1 == mes2 && dia1 > dia2)) 
        return 1;
    else    
        return 0;
}

/**
 * @brief Verifica se uma data de inoculação é válida
 *
 * @param dia Dia da data a verificar
 * @param mes Mês da data a verificar
 * @param ano Ano da data a verificar
 * @param dia_atual Dia atual do sistema
 * @param mes_atual Mês atual do sistema
 * @param ano_atual Ano atual do sistema
 * @return int Retorna 1 se a data for válida, 0 caso contrário
 */
int verifica_data_inoculacao(int dia, int mes, int ano, int dia_atual, 
    int mes_atual, int ano_atual) {
    int dia_max, bissexto;

    bissexto = verifica_bissexto(ano);

    dia_max = mes == 2 ? bissexto : (mes % 2 == 0 ? 30 : 31);
    if (dia < 1 || dia > dia_max || mes < 1 || mes > 12 || ano < 0) {
        return 0;
    }

    if (ano > ano_atual) return 0;
    if (ano == ano_atual && mes > mes_atual) return 0;
    if (ano == ano_atual && mes == mes_atual && dia > dia_atual) return 0;
    
    return 1;
}

/**
* @brief Função auxiliar para verificar se o nome de um utente existe na base de registos.
* 
* @param base_registos Um ponteiro para a estrutura Base_registos que contém os dados dos utentes.
* @param nome_utente O nome do utente a ser verificado.
* @param lingua A língua a ser usada (0 para Inglês, outro valor para Português).
* @return 1 se o nome do utente existir, 0 caso contrário.
*/
int aux_variaveis_1(Base_registos *base_registos, char *nome_utente,
    int lingua){
        int iguais = 0;
        if (base_registos->num_utentes == 0) {
            print_erros_2(lingua, nome_utente, NOUSER, NOUSER_PT);
            return 0;
        }
        else {
            for (int i = 0; i < base_registos->num_utentes; i++) {
                if (strcmp(nome_utente, 
                    base_registos->utentes[i].nome_utente) == 0){
                    iguais = 1;
                    i = base_registos->num_utentes;
                }
            } 
            if (iguais == 0){   
                print_erros_2(lingua, nome_utente, NOUSER, NOUSER_PT);
                return 0;
            }
        }
        return 1;
}

/**
 * @brief Verifica a validade das variáveis fornecidas
 *
 * @param base Ponteiro para a estrutura Base
 * @param base_registos Ponteiro para a estrutura Base_registos
 * @param nome_utente Nome do utente a verificar
 * @param dia Dia da data de inoculação
 * @param mes Mês da data de inoculação
 * @param ano Ano da data de inoculação
 * @param lote Número do lote da vacina
 * @param variaveis Número de variáveis a verificar
 * @param lingua Idioma para as mensagens de erro
 * @return int Retorna 1 se todas as variáveis forem válidas, 0 caso contrário
 */
int verifica_variaveis(Base *base, Base_registos *base_registos, 
    char *nome_utente, int dia, int mes, int ano, char *lote, int variaveis, 
    int lingua){
    int dia_sis = base->dia_sistema, mes_sis = base->mes_sistema, 
        ano_sis = base->ano_sistema;
    if (variaveis >= 1) {
        if (!aux_variaveis_1(base_registos, nome_utente, lingua)) {
            return 0;
        }
    }
    if (variaveis >= 4) {
        if (verifica_data_inoculacao(dia, mes, ano, dia_sis, mes_sis, 
            ano_sis) != 1) {
            print_erros(lingua, INVDATE, INVDATE_PT);
            return 0;
        }
    }
    if (variaveis == 5) {
        for (int i = 0; i < base->cnt; i++) {
            if (strcmp(lote, base->dados[i].lote) == 0) {
                return 1;
            }
        }
        print_erros_2(lingua, lote, NOBATCH, NOBATCH_PT);
        return 0;  
    }
    return 1;
}

/**
 * @brief Função auxiliar para apagar todas as inoculações de um utente.
 *
 * Esta função liberta a memória alocada para o array de inoculações de um utente específico
 * e redefine o número de inoculações para 0.
 *
 * @param base_registos Um ponteiro para a estrutura Base_registos que contém a informação dos utentes.
 * @param i O índice do utente na base de registos cujo array de inoculações será apagado.
 * @return O número de inoculações que foram apagadas.
 */
int aux_apaga_1(Base_registos* base_registos, int i){
    int num_inoc_apag;
    num_inoc_apag = base_registos->utentes[i].num_inoculacoes;
    free(base_registos->utentes[i].inoculacoes);
    base_registos->utentes[i].inoculacoes = NULL;
    base_registos->utentes[i].num_inoculacoes = 0; 
    return num_inoc_apag;
}

/**
 * @brief Função auxiliar para deslocar as inoculações de um utente.
 *
 * Esta função desloca as inoculações de um utente para a esquerda, removendo a primeira inoculação
 * e movendo as outras para a frente.
 *
 * @param base_registos Um ponteiro para a estrutura Base_registos que contém a informação dos utentes.
 * @param i O índice do utente na base de registos cujas inoculações serão deslocadas.
 * @param j O índice da primeira inoculação que será removida.
 */
void shift_esq(Base_registos* base_registos, int i, int j){
    for (int k = j; k < base_registos->utentes[i].num_inoculacoes - 1; k++){
        base_registos->utentes[i].inoculacoes[k] = 
            base_registos->utentes[i].inoculacoes[k+1];
    }
}

/**
 * @brief Função auxiliar para apagar inoculações específicas de um utente com base em critérios de data e lote.
 *
 * Esta função itera sobre as inoculações de um utente e remove aquelas que correspondem
 * aos critérios especificados de data e, opcionalmente, lote.
 *
 * @param base_registos Um ponteiro para a estrutura Base_registos que contém a informação dos utentes.
 * @param dia O dia da inoculação a ser apagada.
 * @param mes O mês da inoculação a ser apagada.
 * @param ano O ano da inoculação a ser apagada.
 * @param lote O lote da vacina a ser apagada (pode ser NULL se não for usado como critério).
 * @param variaveis Um inteiro indicando quais critérios de pesquisa estão a ser usados (4 para data, 5 para data e lote).
 * @param i O índice do utente na base de registos cujas inoculações serão verificadas e possivelmente apagadas.
 * @return O número de inoculações que foram apagadas.
 */
int aux_apaga_maior1(Base_registos* base_registos, int dia, int mes, int ano,
    char *lote, int variaveis,int num_inoc_apag, int i){
    for (int j = 0; j < base_registos->utentes[i].num_inoculacoes; j++){
        if (compara_datas_inoculacao(dia, mes, ano, base_registos->utentes[i].
        inoculacoes[j].dia, base_registos->utentes[i].inoculacoes[j].mes, 
        base_registos->utentes[i].inoculacoes[j].ano) == 0){
            if (variaveis == 4) { // nome e data
                num_inoc_apag++;
                shift_esq(base_registos, i, j);
                base_registos->utentes[i].num_inoculacoes--;
                memset(&base_registos->utentes[i].inoculacoes
                    [base_registos->utentes[i].num_inoculacoes], 0, 
                    sizeof(Registo_inoc));
                j--;
            }  
            else if (variaveis == 5){ // nome, data e lote
                if (strcmp(base_registos->utentes[i].inoculacoes[j].lote, 
                    lote) == 0){
                    num_inoc_apag++;
                    shift_esq(base_registos, i, j);
                    base_registos->utentes[i].num_inoculacoes--;
                    memset(&base_registos->utentes[i].inoculacoes[base_registos
                    ->utentes[i].num_inoculacoes], 0, sizeof(Registo_inoc));
                    j--;
                }
            }
    }   }
    return num_inoc_apag;
}

/**
 * Processa os comandos do usuário em um loop até que 'q' seja digitado.
 * 
 * @param base Ponteiro para a estrutura de dados de lotes de vacinas
 * @param base_registros Ponteiro para a estrutura de dados de registros de vacinação
 * @param linha Buffer para armazenar a entrada do usuário
 * @param lingua Inteiro representando a configuração de idioma
 * 
 * Esta função implementa uma estrutura de switch que lê a entrada do usuário e
 * chama a função apropriada com base no primeiro caractere da entrada.
 * O loop continua até que o usuário digite 'q' para sair.
 */
void switch_comandos(Base *base, Base_registos *base_registos, char *linha, 
    int lingua){
    while (fgets(linha, MAXBUFFER, stdin))
		switch (linha[0]) {
			case 'q': return;
			case 'c': 
                criar_lote(base, linha, lingua);
                break;
			case 't':  
                avancar_tempo(base, linha, lingua);
                break;
			case 'l': 
                lista_lotes(base, linha, lingua); 
                break;
			case 'a': 
                aplica_doses(base, base_registos, linha, lingua); 
                break;
			case 'u': 
                lista_inoculacoes(base_registos, linha, lingua);
                break;
			case 'r': 
                retira_lote(base, linha, lingua);
                break;
			case 'd': 
                apaga_inoculacao(base, base_registos, linha, lingua); 
                break;
			default : break;
		}
}

/**
 * @brief Libera a memória alocada para as estruturas Base e Base_registos
 *
 * @param base Ponteiro para a estrutura Base
 * @param base_registos Ponteiro para a estrutura Base_registos
 */
void cleanup(Base *base, Base_registos *base_registos) {
    for (int i = 0; i < base->cnt; i++) {
        if (base->dados[i].lote) {
            free(base->dados[i].lote);
            base->dados[i].lote = NULL;
        }
        if (base->dados[i].nome_vac) {
            free(base->dados[i].nome_vac);
            base->dados[i].nome_vac = NULL;
        }
    }

    for (int i = 0; i < base_registos->num_utentes; i++) {
        if (base_registos->utentes[i].inoculacoes) {
            free(base_registos->utentes[i].inoculacoes);
            base_registos->utentes[i].inoculacoes = NULL;
        }
        if (base_registos->utentes[i].nome_utente) {
            free(base_registos->utentes[i].nome_utente);
            base_registos->utentes[i].nome_utente = NULL;
        }
    }

    if (base_registos->utentes) {
        free(base_registos->utentes);
        base_registos->utentes = NULL;
    }
}
