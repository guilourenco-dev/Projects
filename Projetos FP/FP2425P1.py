def eh_tabuleiro(tabuleiro):
    """
    Descrição:
    Recebe um tabuleiro (tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto)
    Verifica se é válido
    Devolve um boleano(True or False) 
    """
    if type(tabuleiro) == tuple and 2 <= len(tabuleiro) <= 100:
        for indice in range(len(tabuleiro)):
            if type(tabuleiro[indice]) == tuple and 2 <= len(tabuleiro[indice]) <= 100 and len(tabuleiro[indice - 1]) == len(tabuleiro[indice]):
                for valor in tabuleiro[indice]:
                    if type(valor) == int and (valor == -1 or valor == 0 or valor == 1):
                        continue
                    else:
                        return False
            else:
                return False
    else:
        return False
    return True
    

def eh_posicao(posicao):
    """
    Descrição:
    Recebe uma posição dum tabuleiro (int)
    Verifica se essa posição é um inteiro válido
    Devolve um boleano(True or False)
    """
    if type(posicao) == int and 0 < posicao <= 10000:
        return True
    return False


def obtem_dimensao(tabuleiro):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto)
    Retorna as dimensões do tabuleiro (m, n)
    """
    m = len(tabuleiro)              # Número de linhas do tabuleiro
    n = len(tabuleiro[0])           # Número de colunas do tabuleiro
    return (m, n)


def obtem_dimensoes_pos(tabuleiro, posicao):            # Função auxiliar para obter a linha ou a coluna apartir da posicao
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Retorna as dimensões do tabuleiro(m - linha,n - coluna)
    """

    _,n = obtem_dimensao(tabuleiro)
    linha = (posicao - 1) // n
    coluna = (posicao - 1) % n
    return (linha,coluna)


def obtem_valor(tabuleiro, posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Retorna o valor (1, -1, ou 0) de uma posição específica dada
    """
    linha, coluna = obtem_dimensoes_pos(tabuleiro, posicao)
    return tabuleiro[linha][coluna]


def obtem_coluna(tabuleiro, posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Retorna as posições de uma coluna específicaa no tabuleiro, em relação a uma posição dada.
    """

    m,n = obtem_dimensao(tabuleiro)          # Número de linhas e colunas do tabuleiro
    if posicao > m:                # Verificar se a posição dada pertence à 1º linha. Caso não pertença, passa-la para a 1ª linha
        indice_coluna = posicao - n
    else:
        indice_coluna = posicao

    coluna = (indice_coluna,)
    for valor in range(m - 1):
        coluna += ((coluna[valor] + n),)    

    return coluna


def obtem_linha(tabuleiro, posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Retornam as posições de uma linha específica no tabuleiro, em relação a uma posição dada.
    """

    _,n = obtem_dimensao(tabuleiro)  
    indice_linha = ((posicao - 1) // n)  
    linha = ()
    for indice in range(n):
        linha = linha + ((indice_linha * n) + (indice + 1),)
    return linha


def obtem_diagonais(tabuleiro, posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Retornam as posições de uma diagonal e antidiagonal específicas no tabuleiro, em relação a uma posição dada.
    """

    diagonal = (posicao,)
    antidiagonal = (posicao,)
    m,n = obtem_dimensao(tabuleiro)
    pos_copia_01, pos_copia_02, pos_copia_03, pos_copia_04 = posicao, posicao, posicao, posicao
    
    if not 0 < posicao <= (m * n):
        return ((),())  
    
    while (obtem_dimensoes_pos(tabuleiro, pos_copia_01)[0] and obtem_dimensoes_pos(tabuleiro, pos_copia_01)[1]) > 0:   # Obter os valores da diagonal anteriores à posição 
        pos_copia_01 -= n + 1                                                                                         # Para todos os casos, os valores da diagonal diferenciam uns dos outros pela dimensão das colunas -n mais um (n + 1) 
        diagonal = (pos_copia_01,) + diagonal 
    while obtem_dimensoes_pos(tabuleiro, pos_copia_02)[0] < m - 1 and obtem_dimensoes_pos(tabuleiro, pos_copia_02)[1] < n - 1:    # Obter os valores da diagonal posteriores à posição 
        pos_copia_02 += n + 1
        diagonal += (pos_copia_02,) 

    while obtem_dimensoes_pos(tabuleiro, pos_copia_03)[0] < m - 1 and obtem_dimensoes_pos(tabuleiro, pos_copia_03)[1] > 0:     # Obter os valores da antidiagonal anteriores à posição 
        pos_copia_03 += n - 1                                                                                                 # Para todos os casos, os valores da antidiagonal diferenciam uns dos outros pela dimensão das colunas -n menos um (n - 1) 
        antidiagonal = (pos_copia_03,) + antidiagonal
    while obtem_dimensoes_pos(tabuleiro, pos_copia_04)[0] > 0 and obtem_dimensoes_pos(tabuleiro, pos_copia_04)[1] < n - 1:     # Obter os valores da antidiagonal posteriores à posição 
        pos_copia_04 -= n - 1
        antidiagonal += (pos_copia_04,)
 
    return (diagonal,antidiagonal)


def tabuleiro_para_str(tabuleiro):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto)
    Converte o tabuleiro em uma string formatada para visualização(output)
    Retorna esse output
    """
    
    r = ''
    m,n = obtem_dimensao(tabuleiro)
    for t,l in enumerate(tabuleiro):
        for i,c in enumerate(l):
            if c == -1:
                c = 'O'
            elif c == 0:
                c = '+'
            elif c == 1:   #ver se c pode ser != de 1, se n for poe else
                c = 'X'
            r += str(c) 
            if i < (n - 1):    # Para que não apareça '---' no final 
                r += '---'
        if t < (m - 1):        # Para que não apareça '| | | |' no final
            r += '\n' + '|   ' * (n - 1) + '|\n'
    return r


def eh_posicao_valida(tabuleiro,posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Confirma se a posição está dentro dos limites do tabuleiro
    Retorna um boleano(True or False)
    """

    m,n = obtem_dimensao(tabuleiro)

    if eh_posicao(posicao) and eh_tabuleiro(tabuleiro):  # Verificar se o tabuleiro e a posição são válidos, caso não sejam levantar um erro.
        if posicao <= (m * n):      # Verificar se a posicao pertence ao tabuleiro, caso contrário retornar False.
            return True        
        return False
    raise ValueError('eh_posicao_valida: argumentos invalidos')


def eh_posicao_livre(tabuleiro, posicao):
    """
    Descrição:
    Recebe um tabuleiro(tuplo de tuplos de inteiros entre -1, 0 e 1, e de tamanho correto) e uma posição desse tabuleiro(int)
    Verifica se a posição do tabuleiro está vazia(valor 0)
    Retorna um boleano(True or False)
    """

    m,n = obtem_dimensao(tabuleiro)

    if eh_posicao(posicao) and eh_tabuleiro(tabuleiro) and posicao <= (m * n): # Verificar se o tabuleiro e a posição são válidos e se a posição pertence ao tabuleiro.
        if obtem_valor(tabuleiro,posicao) == 0:    # Para verificarmos se a posição está livre basta vermos se o valor nessa posição é 0.     
            return True
        return False
    raise ValueError('eh_posicao_livre: argumentos invalidos')


def obtem_posicoes_livres(tabuleiro):
    """
    Obtém as posições livres de um tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo, representado como um tuplo de tuplos.
    Returns:
        tuple: Um tuplo com todas as posições livres (valor 0).
    Raises:
        ValueError: Se o argumento fornecido não for um tabuleiro válido.
    """
    
    m,n = obtem_dimensao(tabuleiro)

    pos_livres = ()
    if eh_tabuleiro(tabuleiro):
        for i in range(m * n):
            if obtem_valor(tabuleiro, i + 1) == 0:
                pos_livres += (i + 1,)
    else:
        raise ValueError('obtem_posicoes_livres: argumento invalido')

    return pos_livres


def obtem_pos(tabuleiro,linha, coluna):    # Função auxiliar para obter uma posição apartir da linha e da coluna
    """
    Calcula a posição correspondente a uma dada linha e coluna no tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        linha (int): O índice da linha.
        coluna (int): O índice da coluna.
    Returns:
        int: A posição correspondente no tabuleiro.
    """
   
    _,n = obtem_dimensao(tabuleiro)
    posicao = (linha * n) + coluna + 1
    return posicao 


def obtem_posicoes_jogador(tabuleiro, inteiro):
    """
    Obtém as posições de um jogador específico no tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        inteiro (int): 1 ou -1 para o jogador e o contrário para o jogador adversário.
    Returns:
        tuple: Um tuplo com todas as posições do jogador.
    Raises:
        ValueError: Se o tabuleiro ou o valor do jogador não forem válidos.
    """
    
    pos_jog = ()
    for i, linha in enumerate(tabuleiro):
        for j, coluna in enumerate(linha):
            posicao = obtem_pos(tabuleiro,i,j)
            if eh_tabuleiro(tabuleiro) and (inteiro == 1 or inteiro == -1):   # Verificar se o tabuleiro e se o inteiro recebido são válidos
                if coluna == inteiro:          # Verificar se o valor da tabela é igual ao inteiro dado                                 
                    pos_jog += (posicao,)
            else:
                raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    return pos_jog


def obtem_posicoes_adjacentes(tabuleiro, posicao):
    """
    Obtém as posições adjacentes a uma dada posição no tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        posicao (int): A posição alvo.
    Returns:
        tuple: Um tuplo com as posições adjacentes à posição fornecida.

    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    
    if not (eh_tabuleiro(tabuleiro) and eh_posicao(posicao) and eh_posicao_valida(tabuleiro, posicao)):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')

    pos_adj = ()
    m,n = obtem_dimensao(tabuleiro)
    linha, coluna = obtem_dimensoes_pos(tabuleiro, posicao)
    
    for l in range(linha - 1, linha + 2):       # Percorrer as 3 linhas possíveis adjacentes (linha anterior à posição, a própria linha e a a seguir)
        for c in range(coluna - 1, coluna + 2):        # Percorrer as 3 colunas possíveis adjacentes (coluna anterior à posição, a própria coluna e a a seguir)
            if  0 <= l < m and 0 <= c < n:   # Verificar se a posição é válida, caso não seja, não se adiciona essa posicao ao tuplo
                pos = obtem_pos(tabuleiro, l, c)
                if pos != posicao:         # Não adicionar a própia posição e posições não válidas
                    pos_adj += (pos,)
        
    return pos_adj


def obtem_distancia_entre_pos(tabuleiro,pos_01,pos_02):    
    """ 
    Função auxiliar para calcular a distância entre duas posições
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        pos_01 (int): A primeira posição.
        pos_02 (int): A segunda posição.
    Returns:
        int: A distância entre as duas posições.
    """

    linha_01, col_01 = obtem_dimensoes_pos(tabuleiro, pos_01)
    linha_02, col_02 = obtem_dimensoes_pos(tabuleiro, pos_02)
    distancia = max(abs(linha_01-linha_02), abs(col_01 - col_02))    # Cálculo matemático entre duas coordenadas
    return distancia

def ordena_posicoes_tabuleiro(tabuleiro, tuplo):
    """
    Ordena as posições de um tuplo com base na proximidade ao centro do tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        tuplo (tuple): Um tuplo de posições a ser ordenado.
    Returns:
        tuple: Um tuplo com as posições ordenadas.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (eh_tabuleiro(tabuleiro) and type(tuplo) == tuple):           # Validar os argumentos
       raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    for i in range(len(tuplo)):
        if not (type(tuplo[i]) == int and 0 < tuplo[i] <= 10000):
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')

    m,n = obtem_dimensao(tabuleiro)
    centro = ((m // 2) * n) + (n // 2) + 1          # Calcular o centro do tabuleiro
    linha, coluna = obtem_dimensoes_pos(tabuleiro, centro)
    pos_adj = obtem_posicoes_adjacentes(tabuleiro, centro)
    if centro in tuplo:
        pos_ordenadas = (centro,)
    else:
        pos_ordenadas = ()
    for valor in pos_adj:
        if valor in tuplo:  
            pos_ordenadas += (valor,)
    distancia_lst = ()
    k = -2

    if len(tuplo) == len(pos_ordenadas):
        return tuplo if tuplo == () else pos_ordenadas 

    for valor in tuplo:
        distancia = obtem_distancia_entre_pos(tabuleiro, centro, valor)
        if distancia not in distancia_lst:
            distancia_lst += (obtem_distancia_entre_pos(tabuleiro, centro, valor),)
   
    for i in range(distancia_lst[0]):
        for j in range(m + 1):
            for valor in tuplo:
                if obtem_pos(tabuleiro, linha + k + j, coluna + k + j) < 0:
                    linha_val = obtem_linha(tabuleiro,obtem_pos(tabuleiro, 0, 0))
                else:
                    linha_val = obtem_linha(tabuleiro,obtem_pos(tabuleiro, linha + k + j, coluna + k + j))
                
                if valor in linha_val[0 if (coluna - 2 - i) == 0 else (coluna - 2 - i): coluna + 3 + i] and valor not in pos_ordenadas:
                    pos_ordenadas += (valor,)
        k -= 1
    
    return tuplo if tuplo == () else pos_ordenadas    # No caso do tuplo ser nulo, retornar um tuplo vazio


def marca_posicao(tabuleiro, posicao, inteiro):
    """
    Marca uma posição no tabuleiro com o valor do jogador.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        posicao (int): A posição a ser marcada.
        inteiro (int): O jogador, 1 para o jogador 1 e -1 para o jogador adversário.
    Returns:
        tuple: O tabuleiro atualizado com a nova marcação.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (eh_tabuleiro(tabuleiro) and eh_posicao(posicao) and eh_posicao_valida(tabuleiro, posicao) and eh_posicao_livre(tabuleiro, posicao) and (inteiro == 1 or inteiro == -1)):
        raise ValueError('marca_posicao: argumentos invalidos')
    linha, coluna = obtem_dimensoes_pos(tabuleiro, posicao)
    novo_tabuleiro = ()
    nova_linha = ()
    m,n = obtem_dimensao(tabuleiro)
    for l in range(m):          # Correr as linhas (l) e as colunas (c)
            for c in range(n):
                valor = tabuleiro[l][c]
                if not (l == linha and c == coluna):   # Enquanto a posição não for igual à dada adicionar os valores do tabuleiro dado a uma nova linha. 
                    nova_linha += (valor,)            # Quando as posições forem iguais, substituir o valor antigo (0) pelo inteiro dado (1 ou -1).
                else:                               
                    nova_linha += (inteiro,)
                if c == n - 1:                          # Quando o índice da coluna for igual ao último índice dessa coluna, 
                    novo_tabuleiro += (nova_linha,)    # Fechar a nova linha e adicioná-la ao novo tabuleiro, voltando nova linha ao tuplo vazio para recomeçar o processo
                    nova_linha = ()
    return  novo_tabuleiro

    
def verifica_k_linhas(tabuleiro, posicao, jogador, k):
    """
    Verifica se há k ou mais posições consecutivas de um jogador em linhas, colunas ou diagonais.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        posicao (int): A posição a ser verificada.
        jogador (int): O jogador, 1 ou -1.
        k (int): O número de posições consecutivas a ser verificado.
    Returns:
        bool: True se houver k ou mais posições consecutivas, False caso contrário.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (eh_tabuleiro(tabuleiro) and eh_posicao(posicao) and eh_posicao_valida(tabuleiro, posicao) and (jogador == 1 or jogador == -1) and type(k) == int and 0 < k <= 100):
        raise ValueError('verifica_k_linhas: argumentos invalidos')

    coluna = obtem_coluna(tabuleiro, posicao)
    linha = obtem_linha(tabuleiro, posicao)
    diagonal, antidiagonal = obtem_diagonais(tabuleiro, posicao)
    
    pos_jog = obtem_posicoes_jogador(tabuleiro, jogador)
    def obtem_consecutivos(tuplo):      # Função auxiliar para calcular o maior número de posições consecutivas
        posicao_dada = False
        consecutivos = 0  
        max_consecutivos = 0  
        for valor in tuplo:
            if valor in pos_jog:        # Se o valor do tuplo dado for posição do jogador adicionar 1 às posições consecutivas e atualizar o maior número de posições consecutivas
                consecutivos += 1
                max_consecutivos = consecutivos
                if valor == posicao:   
                    posicao_dada = True                    
            else:       # Reiniciar a contagem de posições consecutivas
                consecutivos = 0
        return max_consecutivos if posicao_dada else 0
    
    if obtem_consecutivos(linha) == k or obtem_consecutivos(coluna) == k or obtem_consecutivos(diagonal) == k or obtem_consecutivos(antidiagonal) == k:
       # Caso o maior número de posições do jogador consecutivas for igual a k devolver True
        return True         
    return False


def eh_fim_jogo(tabuleiro, k):
    """
    Verifica se o jogo terminou, ou seja, se há um vencedor ou se não há mais posições livres.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        k (int): O número de posições consecutivas para vencer.
    Returns:
        bool: True se o jogo terminou, False caso contrário.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (eh_tabuleiro(tabuleiro) and type(k) == int and 0 < k <= 100):
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    
    pos_jog1 = obtem_posicoes_jogador(tabuleiro,1)
    pos_jog2 = obtem_posicoes_jogador(tabuleiro, -1)
    verificação = False
    for posicao1 in pos_jog1:
        if verifica_k_linhas(tabuleiro, posicao1, 1, k):
            verificação = True
    for posicao2 in pos_jog2:
        if verifica_k_linhas(tabuleiro, posicao2, -1, k):
            verificação = True
    if obtem_posicoes_livres(tabuleiro) == ():
        verificação = True
    return verificação  


def escolhe_posicao_manual(tabuleiro):
    """
    Permite ao jogador escolher manualmente uma posição livre no tabuleiro.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
    Returns:
        int: A posição escolhida pelo jogador.
    Raises:
        ValueError: Se o tabuleiro não for válido.
    """
    
    if not eh_tabuleiro(tabuleiro):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    while True:
        posicao = input('Turno do jogador. Escolha uma posicao livre: ')
        if posicao.isdigit():
            posicao = int(posicao)
            if eh_posicao(posicao) and eh_posicao_valida(tabuleiro, posicao) and eh_posicao_livre(tabuleiro, posicao):
                return posicao


def estrategia_facil(tabuleiro, jogador):
    """
    Implementa a estratégia fácil para o computador escolher uma posição.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        jogador (int): O jogador atual (1 ou -1).
    Returns:
        int: A posição escolhida pela estratégia fácil.
    """
    
    posicoes = ()
    for indice_livres in obtem_posicoes_livres(tabuleiro):
        for indice_adj in obtem_posicoes_adjacentes(tabuleiro,indice_livres):
            if obtem_valor(tabuleiro,indice_adj) == jogador:
                posicoes += (indice_livres,)
                break
    if posicoes == ():
        return obtem_posicoes_livres(tabuleiro)[0]
    return (posicoes)[0]
def estrategia_normal(tabuleiro, jogador, k):
    """
    Implementa a estratégia normal para o computador escolher uma posição.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        jogador (int): O jogador atual (1 ou -1).
        k (int): O número de posições consecutivas para vencer.
    Returns:
        int: A posição escolhida pela estratégia normal.
    """
    
    pos_livres = obtem_posicoes_livres(tabuleiro)
    pos_jog = obtem_posicoes_jogador(tabuleiro, jogador)
    pos_k_linhas = ()
    pos_k_linhas_adver = ()
    m,n = obtem_dimensao(tabuleiro)
    centro = ((m // 2) * n) + (n // 2) + 1  
    menor_distancia, menor_distancia_indice = 100, None
    menor_distancia_adver, menor_distancia_indice_adver = 100, None
    L, L_adver = 0, 0

    jogador_adversario = -(jogador)          # Obter o valor do jogador adversário
    pos_adver = obtem_posicoes_jogador(tabuleiro, jogador_adversario)

    for indice in range(k, 1, -1):
        pos_adj_comuns = ()
        for posicao in pos_jog:         
            pos_adj = obtem_posicoes_adjacentes(tabuleiro, posicao)
            for adj in pos_adj:  
                if adj in pos_livres and adj not in pos_adj_comuns:
                    novo_tabuleiro = marca_posicao(tabuleiro,adj,jogador) 
                    if verifica_k_linhas(novo_tabuleiro, adj, jogador, indice):        # Verificar se a posição livre adjacente a uma posição do jogador forma uma linha de comprimento k
                        pos_k_linhas += (adj,)
                        L = indice
                        for j, valor in enumerate(pos_k_linhas):
                            distancia = obtem_distancia_entre_pos(tabuleiro, valor, centro)        # Caso forme e haja mais do que uma posição nessas circunstâncias, verificar qual a posição mais próxima do centro e devolvê-la
                            if distancia < menor_distancia:
                                menor_distancia = distancia
                                menor_distancia_indice = j
                    else:
                        novo_tabuleiro = None
                pos_adj_comuns += (adj,)
               # Encontrado o maior L, parar de tentar encontrar um menor

    for indice_adver in range(k, 1, -1):           
        pos_adj_adver_comuns = ()
        for valor_adver in pos_adver:                                             # O mesmo processo é repetido para as posições do adversário
            pos_adj_adver = obtem_posicoes_adjacentes(tabuleiro, valor_adver)
            for adj_adver in pos_adj_adver:
                if adj_adver in pos_livres and adj_adver not in pos_adj_adver_comuns:
                    novo_tabuleiro_adver = marca_posicao(tabuleiro, adj_adver, jogador_adversario)
                    if verifica_k_linhas(novo_tabuleiro_adver, adj_adver, jogador_adversario, indice_adver):      
                        pos_k_linhas_adver += (adj_adver,)
                        L_adver = indice_adver
                        for l, valor in enumerate(pos_k_linhas_adver):
                            distancia = obtem_distancia_entre_pos(tabuleiro, valor, centro) 
                            if distancia < menor_distancia_adver:
                                menor_distancia_adver = distancia
                                menor_distancia_indice_adver = l
                    else:
                        novo_tabuleiro_adver = tabuleiro
                pos_adj_adver_comuns += (adj_adver,)
    # Verificar qual o maior L e retornar a sua posição, caso não exista um L em ambos os casos, retornar a primeira posição livre
    if pos_k_linhas == () and pos_k_linhas_adver == ():
        return pos_livres[0]
    if L >= L_adver:
        return pos_k_linhas[menor_distancia_indice] if menor_distancia_indice is not None else pos_livres[0]
    else:
        return pos_k_linhas_adver[menor_distancia_indice_adver] if menor_distancia_indice_adver is not None else pos_livres[0]
def estrategia_dificil(tabuleiro, jogador, k):
    """
    Implementa a estratégia difícil para o computador escolher uma posição.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        jogador (int): O jogador atual (1 ou -1).
        k (int): O número de posições consecutivas para vencer.
    Returns:
        int: A posição escolhida pela estratégia difícil.
    """
    
    pos_livres = obtem_posicoes_livres(tabuleiro)
    pos_jog = obtem_posicoes_jogador(tabuleiro, jogador)
    resultado = ''    
    jogador_adversario = -jogador           # Obter o valor do jogador adversário
    pos_adver = obtem_posicoes_jogador(tabuleiro, jogador_adversario)
    indice_resultado = 0
    for posicao in pos_jog:   
            pos_adj = obtem_posicoes_adjacentes(tabuleiro, posicao)
            for adj in pos_adj:  
                if adj in pos_livres:
                    novo_tabuleiro = marca_posicao(tabuleiro,adj,jogador)                                               
                if verifica_k_linhas(novo_tabuleiro, adj, jogador, k):        # Verificar se a posição livre adjacente a uma posição do jogador forma uma linha de comprimento k
                    return adj                                             
                
    for posicao in pos_adver:    
            pos_adj_adver = obtem_posicoes_adjacentes(tabuleiro, posicao)
            for adj_adver in pos_adj_adver: 
                if adj_adver in pos_livres:
                    novo_tabuleiro = marca_posicao(tabuleiro, adj_adver, jogador_adversario) 
                if verifica_k_linhas(novo_tabuleiro, adj_adver, jogador_adversario, k):        # Verificar se a posição livre adjacente a uma posição do jogador forma uma linha de comprimento k
                    return adj_adver
    
    for i, valor in enumerate(pos_livres):
        novo_tabuleiro = marca_posicao(tabuleiro, valor, jogador)
        while len(obtem_posicoes_livres(novo_tabuleiro)) > 0:
            pos_adver = estrategia_normal(novo_tabuleiro, jogador_adversario, k)
            novo_tabuleiro = marca_posicao(novo_tabuleiro, pos_adver, jogador_adversario)
            if eh_fim_jogo(novo_tabuleiro, k): 
                if len(obtem_posicoes_livres(novo_tabuleiro)) == 0:
                    resultado = 'empate'
                    indice_resultado = i
                break
    
            posicao = estrategia_normal(novo_tabuleiro, jogador, k)
            novo_tabuleiro = marca_posicao(novo_tabuleiro, posicao, jogador)
    
            if eh_fim_jogo(novo_tabuleiro, k):
                if len(obtem_posicoes_livres(novo_tabuleiro)) == 0:
                    resultado = 'empate'
                    indice_resultado = i
                return valor

        
    if resultado == 'empate':
        return pos_livres[indice_resultado]
    return pos_livres[0]


def escolhe_posicao_auto(tabuleiro, jogador, k, lvl):
    """
    Escolhe automaticamente uma posição no tabuleiro com base no nível de dificuldade.
    Args:
        tabuleiro (tuple): O tabuleiro de jogo.
        jogador (int): O jogador atual (1 ou -1).
        k (int): O número de posições consecutivas para vencer.
        lvl (str): O nível de dificuldade ('facil', 'normal' ou 'dificil').
    Returns:
        int: A posição escolhida automaticamente.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (eh_tabuleiro(tabuleiro) and type(k) == int and 0 < k <= 100 and not eh_fim_jogo(tabuleiro, k) and (jogador == -1 or jogador == 1) and (lvl == 'facil' or lvl == 'normal' or lvl == 'dificil')):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')

    if lvl == 'facil':
        return estrategia_facil(tabuleiro, jogador)
    elif lvl == 'normal':
        return estrategia_normal(tabuleiro, jogador, k)
    elif lvl == 'dificil':
        return estrategia_dificil(tabuleiro, jogador, k)


def jogo_mnk(cfg, jogador, lvl):
    """
    Inicia um jogo de MNK.
    Args:
        cfg (tuple): Configuração do jogo (m, n, k).
        jogador (int): O jogador inicial (1 ou -1).
        lvl (str): O nível de dificuldade do computador ('facil', 'normal' ou 'dificil').
    Returns:
        int: 1 se o jogador vencer, -1 se o jogador perder, 0 em caso de empate.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    
    if not (type(cfg) == tuple and len(cfg) == 3 and type(cfg[0]) == int and 1 < cfg[0] <= 100 and type(cfg[1]) == int and 1 < cfg[1] <= 100 and type(cfg[2]) == int and 0 < cfg[2] <= 100 and (jogador == -1 or jogador == 1) and (lvl == 'facil' or lvl == 'normal' or lvl == 'dificil')):
            raise ValueError('jogo_mnk: argumentos invalidos')
    m, n, k = cfg
    jog_adversario = -jogador
    def obtem_tabuleiro_livre(m,n):
        return tuple(tuple(0 for _ in range(n)) for _ in range(m))
    tabuleiro = obtem_tabuleiro_livre(m,n)
    print('Bem-vindo ao JOGO MNK.')

    if jogador == 1:
        print("O jogador joga com 'X'.")
        print(tabuleiro_para_str(tabuleiro))
        posicao = escolhe_posicao_manual(tabuleiro)
        tabuleiro = marca_posicao(tabuleiro, posicao, jogador)
        print(tabuleiro_para_str(tabuleiro))
        while not eh_fim_jogo(tabuleiro, k):
            print(f'Turno do computador ({lvl}):')
            posicao = escolhe_posicao_auto(tabuleiro, jog_adversario, k, lvl)
            tabuleiro = marca_posicao(tabuleiro, posicao, jog_adversario)
            print(tabuleiro_para_str(tabuleiro))
            posicao = escolhe_posicao_manual(tabuleiro)
            tabuleiro = marca_posicao(tabuleiro, posicao, jogador)
            print(tabuleiro_para_str(tabuleiro))

    else:
        print("O jogador joga com 'O'.")
        print(tabuleiro_para_str(tabuleiro))
        print(f'Turno do computador ({lvl}):')
        posicao = escolhe_posicao_auto(tabuleiro, jog_adversario, k, lvl)
        tabuleiro = marca_posicao(tabuleiro, posicao, jog_adversario)
        print(tabuleiro_para_str(tabuleiro))
        while not eh_fim_jogo(tabuleiro, k):
            posicao = escolhe_posicao_manual(tabuleiro)
            tabuleiro = marca_posicao(tabuleiro, posicao, jogador)
            print(tabuleiro_para_str(tabuleiro))
            print(f'Turno do computador ({lvl}):')
            posicao = escolhe_posicao_auto(tabuleiro, jog_adversario, k ,lvl)
            tabuleiro = marca_posicao(tabuleiro, posicao, jogador)
            print(tabuleiro_para_str(tabuleiro))

    for indice in obtem_posicoes_jogador(tabuleiro, jogador):
        if verifica_k_linhas(tabuleiro, indice, jogador, k):
            print('VITORIA')
            return jogador
    for indice in obtem_posicoes_jogador(tabuleiro, jog_adversario):
        if verifica_k_linhas(tabuleiro, indice, jog_adversario, k):
            print('DERROTA')
            return jog_adversario

        print('EMPATE')
        return 0