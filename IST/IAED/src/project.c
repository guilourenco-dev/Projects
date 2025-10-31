/**
 * @file main.c
 * @brief Este ficheiro contém a função principal do programa de vacinação.
 * @author [ist1114538 - Guilherme Lourenço]
 */
#include "aux.h"
#include "comandos.h"

/**
 * @brief Função principal do programa de vacinação.
 *
 * @param argc O número de argumentos da linha de comando.
 * @param argv Um array de strings contendo os argumentos da linha de comando.
 * @return 0 se o programa for executado com sucesso.
 */
int main(int argc, char *argv[]) {
	// Declaração de variáveis
    char linha[MAXBUFFER] = {0};
    int lingua = 0;
	Base base = {0};
    Base_registos base_registos = {0};

    // Inicialização da base de registos
    base_registos.limite_utentes = MAXNUMUTENTES;
    base_registos.utentes = malloc(base_registos.limite_utentes * 
        sizeof(Usuario));
    base_registos.num_utentes = 0;
    
    // Inicialização da base de dados principal
	base.cnt = 0;
    base.dia_sistema = 1; base.mes_sistema = 1; base.ano_sistema = 2025;
    
    // Verificação de argumentos para definir a língua
    if (argc == 2 && strcmp(argv[1], "pt") == 0){
        lingua = 1;
    }
    switch_comandos(&base, &base_registos, linha, lingua);
    cleanup(&base, &base_registos);
	return 0;
}