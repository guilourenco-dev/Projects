# TAD posicao
# Construtor
def cria_posicao(col, lin):
    """
    cria_posicao: str × int → tuplo
    Cria uma posição válida no tabuleiro Orbito-n. 
    Recebe uma coluna (letra) e uma linha (inteiro), e devolve um tuplo que representa a posição. 
    Gera um erro se a coluna não estiver entre 'a' e 'j' ou a linha não estiver entre 1 e 10.
    
    Argumentos:
    col -- Letra que representa a coluna da posição ('a' até 'j')
    lin -- Inteiro que representa a linha da posição (1 até 10)
    
    Devolve:
    Um tuplo (coluna, linha) que representa a posição no tabuleiro.
    
    Lança:
    ValueError: Se os argumentos fornecidos forem inválidos.
    """

    # Verifica se a coluna é uma letra válida e se a linha é um inteiro dentro do intervalo permitido
    if type(col) == str and len(col) == 1 and 'a' <= col <= 'j' \
        and type(lin) == int and 1 <= lin <= 10:
            return (col, lin)  # Retorna o tuplo que representa a posição

    # Lança um erro se os argumentos não forem válidos
    raise ValueError('cria_posicao: argumentos invalidos')


# Seletores
def obtem_pos_col(p):
    """
    obtem_pos_col: tuplo → str
    Recebe uma posição e devolve a coluna da posição.
    
    Argumentos:
    p -- Tuplo que representa a posição no tabuleiro.
    
    Devolve:
    A coluna da posição no formato de letra ('a' até 'j').
    """
    
    # Retorna a coluna da posição, que é o primeiro índice do tuplo
    return p[0]

def obtem_pos_lin(p):
    """
    obtem_pos_lin: tuplo → int
    Recebe uma posição e devolve a linha da posição.
    
    Argumentos:
    p -- Tuplo que representa a posição no tabuleiro.
    
    Devolve:
    A linha da posição no formato de inteiro (1 até 10).
    """
    
    # Retorna a linha da posição, que é o segundo índice do tuplo
    return int(p[1])


# Reconhecedor 
def eh_posicao(arg):
    """
    eh_posicao: qualquer → bool
    Verifica se o argumento é uma posição válida no tabuleiro.

    Argumentos:
    arg -- Qualquer valor a ser verificado.

    Devolve:
    True se o argumento for um tuplo que representa uma posição válida (coluna entre 'a' e 'j' e linha entre 1 e 10), False caso contrário.
    """
    
    # Verifica se o argumento é um tuplo e se os valores do tuplo são válidos
    if type(arg) == tuple:
        coluna = arg[0]
        linha = arg[1]
        if type(coluna) == str and type(linha) == int and 'a' <= coluna <= 'j' and 1 <= linha <= 10:
            return True
    return False


# Teste
def posicoes_iguais(p1, p2):
    """
    Verifica se duas posições são iguais.
    
    Argumentos:
    p1 -- Primeira posição no formato de tuplo (coluna, linha)
    p2 -- Segunda posição no formato de tuplo (coluna, linha)
    
    Retorna:
    True se ambas as posições forem válidas e iguais, False caso contrário.
    """
    # Verifica se ambas as posições são válidas
    if eh_posicao(p1) and eh_posicao(p2):
        # Verifica se as posições são iguais
        if p1 == p2:
            return True
    
    # Se as posições não forem válidas ou iguais, retorna False
    return False


# Transformador
def posicao_para_str(p):
    """
    Converte uma posição em formato de tuplo para uma string.

    Argumentos:
    p -- Tuplo que representa a posição no tabuleiro (coluna, linha)

    Devolve:
    Uma string que representa a posição no formato 'coluna' + 'linha'.
    """
    # Obtém a coluna da posição e converte a linha para string
    pos = obtem_pos_col(p) + str(obtem_pos_lin(p))
    return pos

def str_para_posicao(s):
    """
    Converte uma string que representa uma posição no formato 'coluna' + 'linha' para um tuplo.

    Argumentos:
    s -- String que representa a posição no formato 'coluna' + 'linha'

    Devolve:
    Um tuplo que representa a posição no tabuleiro (coluna, linha)
    """
    # Obtém a coluna e a linha da string
    col = s[0]
    lin = int(s[1])
    # Retorna o tuplo que representa a posição
    return (col, lin)


# Funções A.N.
def eh_posicao_valida(p, n):
    """
    Verifica se uma posição é válida num tabuleiro.

    Argumentos:
    p -- Posição no tabuleiro (tuplo (coluna, linha))
    n -- Número de linhas e colunas do tabuleiro

    Devolve:
    Um boleano que indica se a posição é válida ou não.
    """
    # Verifica se a posição é válida
    if eh_posicao(p):
        # Obtém as dimensões do tabuleiro
        colunas = chr(ord('a') + (2 * n - 1))
        linhas = 2 * n 
        # Verifica se a coluna e linha da posição são válidas
        return  obtem_pos_col(p) <= colunas and obtem_pos_lin(p) <= linhas 
    # Caso a posição não seja válida, retorna False
    return False

def obtem_dimensoes_tab(n):
    """
    Obtém as dimensões do tabuleiro.

    Argumentos:
    n -- Número de linhas e colunas do tabuleiro

    Devolve:
    Um tuplo que representa as dimensões do tabuleiro (coluna, linha)
    """
    # Obtém a coluna e a linha do tabuleiro
    col_tab = chr(ord('a') + 2 * n - 1)
    lin_tab = 1 + 2 * n - 1
    # Retorna o tuplo que representa as dimensões do tabuleiro
    return col_tab,lin_tab

def obtem_posicoes_adjacentes(p, n, d):
    """
    Obtém as posições adjacentes a uma dada posição no tabuleiro.
    
    Argumentos:
    p -- Posição no tabuleiro (tuplo (coluna, linha))
    n -- Número de linhas e colunas do tabuleiro
    d -- Booleano que decide se as posições adjacentes são diagonais (True) ou ortogonais (False)
    
    Devolve:
    Um tuplo com as posições adjacentes à posição fornecida.
    """
    
    if d:            # Caso o d seja True, calcular as posições adjacentes diagonais
        adj = ()
        col = obtem_pos_col(p)              # Obter as dimensões da posição dada e do tabuleiro
        lin = obtem_pos_lin(p)
        col_tab, lin_tab = obtem_dimensoes_tab(n) 

        if lin > 1:            # Verifcar as dimensões à volta da posição dada(para cima, direita, baixo, esquerda) \
            if col < col_tab:                # e adicionar as posições adjacentes pela ordem do sentido dos ponteiro dos relógios \
                adj += ((f'{col}{lin - 1}'), (f'{chr(ord(col) + 1)}{lin - 1}'),\
                         (f'{chr(ord(col) + 1)}{lin}'))    # apartir da posição acima à dada
            else:
                adj += ((f'{col}{lin - 1}'),)
        else:
            if col < col_tab:
                adj += ((f'{chr(ord(col) + 1)}{lin}'),)

        if lin < lin_tab:
            if col < col_tab:
                adj += ((f'{chr(ord(col) + 1)}{lin + 1}'), (f'{col}{lin + 1}'))
            else:
                adj += ((f'{col}{lin + 1}'),) 

            if col > 'a':
                if lin > 1:
                    adj += ((f'{chr(ord(col) - 1)}{lin + 1}'),\
                             (f'{chr(ord(col) - 1)}{lin}'),\
                                  (f'{chr(ord(col) - 1)}{lin - 1}')) 
                else:
                    adj += ((f'{chr(ord(col) - 1)}{lin + 1}'),\
                             (f'{chr(ord(col) - 1)}{lin}'))
            else:
                return adj
        else:
            if col > 'a':
                if lin > 1:
                    adj += ((f'{chr(ord(col) - 1)}{lin}'),\
                             (f'{chr(ord(col) + 1)}{lin - 1}')) 
                else:
                    adj += ((f'{chr(ord(col) - 1)}{lin}'),)
            else:
                return adj

        return adj
    
    else:           # Caso o d seja False, calcular as posições adjacentes ortogonais
        adj = ()            
        col = obtem_pos_col(p)              # Obter as dimensões da posição dada e do tabuleiro
        lin = obtem_pos_lin(p)
        col_tab, lin_tab = obtem_dimensoes_tab(n)

        if lin > 1:        # Verificar se a linha anterior existe e adicionar a posição adjacente
            adj += ((f'{col}{lin - 1}'),)
        if col < col_tab:        # Verificar se a coluna seguinte existe e adicionar a posição adjacente
            adj += ((f'{chr(ord(col) + 1)}{lin}'),)
        if lin < lin_tab:        # Verificar se a linha seguinte existe e adicionar a posição adjacente
            adj += ((f'{chr(ord(col))}{lin + 1}'),)
        if col > 'a':        # Verificar se a coluna anterior existe e adicionar a posição adjacente
            adj += ((f'{chr(ord(col) - 1)}{lin}'),)
        return adj
    
def ordena_posicoes(t, n):
    """
    Ordena as posições de um tabuleiro com base na distância do centro.

    Argumentos:
        t (tuple): Um tuplo de posições no tabuleiro.
        n (int): O número de linhas ou colunas do tabuleiro.

    Devolve:
        tuple: Um tuplo com as posições ordenadas pela distância ao centro.
    """
    # Calcula as coordenadas do centro do tabuleiro
    centro = (((2 * n - 1) / 2), ((2 * n - 1) / 2))

    def distancia_entre_posicoes(p):
        """
        Calcula a distância de uma posição ao centro do tabuleiro.

        Argumentos:
            p (str): A posição no formato 'coluna-linha'.

        Devolve:
            tuple: A distância de Chebyshev da posição ao centro, 
                   e as coordenadas da linha e coluna.
        """
        # Obter as dimensões da posição
        col = ord(obtem_pos_col(p)) - ord('a')
        lin = obtem_pos_lin(p) - 1

        # Calcula a distância de Chebyshev até o centro
        return max(abs(centro[0] - col), abs(centro[1] - lin)), lin, col

    # Ordena as posições pela distância ao centro
    return tuple(sorted(t, key=distancia_entre_posicoes))


# TAD pedra
# Construtores
def cria_pedra_branca():
    """
    Cria uma pedra branca para o jogo.

    Devolve:
        str: Um caractere que representa a pedra branca ('O').
    """
    return 'O'

def cria_pedra_preta():
    """
    Cria uma pedra preta para o jogo.

    Devolve:
        str: Um caractere que representa a pedra preta ('X').
    """
    return 'X'

def cria_pedra_neutra():
    """
    Cria uma pedra neutra (vazia) para o jogo.

    Devolve:
        str: Um caractere que representa a pedra neutra (' ').
    """
    return ' '


# Reconhecedor
def eh_pedra(arg):
    """
    Verifica se o argumento é uma pedra válida do jogo (branca, preta ou neutra).

    Argumentos:
        arg -- Um caractere a ser verificado.

    Devolve:
        bool -- True se o argumento for uma pedra válida, False caso contrário.
    """
    return arg in ('X', 'O', ' ')
        
def eh_pedra_branca(p):
    """
    Verifica se o caractere representa uma pedra branca.

    Argumentos:
        p -- Um caractere a ser verificado.

    Devolve:
        bool -- True se o caractere for uma pedra branca ('O'), False caso contrário.
    """
    return eh_pedra(p) and p == 'O'

def eh_pedra_preta(p):
    """
    Verifica se o caractere representa uma pedra preta.

    Argumentos:
        p -- Um caractere a ser verificado.

    Devolve:
        bool -- True se o caractere for uma pedra preta ('X'), False caso contrário.
    """
    return eh_pedra(p) and p == 'X'


# Teste
def pedras_iguais(p1, p2):
    """
    Verifica se duas pedras são iguais.

    Argumentos:
        p1 (str): A primeira pedra a ser comparada.
        p2 (str): A segunda pedra a ser comparada.

    Retorna:
        bool: True se as pedras forem iguais, False caso contrário.
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


# Transformador
def pedra_para_str(p):
    """
    Converte uma pedra para string.

    Argumentos:
        p (str): A pedra a ser convertida.

    Retorna:
        str: A representação em string da pedra.
    """
    return p


# Funções A.N.
def eh_pedra_jogador(p):
    """
    Verifica se uma pedra é um jogador.

    Um jogador pode ser uma pedra branca ('O') ou uma pedra preta ('X').

    Argumentos:
        p (str): A pedra a ser verificada.

    Retorna:
        bool: True se a pedra for um jogador, False caso contrário.
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

def pedra_para_int(p):
    """
    Converte uma pedra para um valor inteiro.

    A representação em inteiro de uma pedra é a seguinte:
    - 1 para uma pedra preta ('X');
    - -1 para uma pedra branca ('O');
    - 0 para uma pedra neutra (' ').

    Argumentos:
        p (str): A pedra a ser convertida.

    Retorna:
        int: O valor inteiro correspondente à pedra.
    """
    return 1 if p == 'X' else -1 if p == 'O' else 0


# TAD tabuleiro
# Construtor
def cria_tabuleiro_vazio(n):
    """
    Cria um tabuleiro de jogo vazio com o tamanho n x n.

    O tabuleiro é representado por uma lista de listas, onde cada lista interna
    representa uma linha do tabuleiro e cada elemento da lista interna representa
    uma coluna do tabuleiro. Cada elemento da lista interna é uma pedra neutra (' ').

    Argumentos:
        n (int): O tamanho do tabuleiro (n x n).

    Retorna:
        list: O tabuleiro de jogo vazio.

    Raises:
        ValueError: Se o argumento fornecido for inválido.
    """
    if type(n) == int and 2 <= n <= 5:
        # Cria uma lista com n listas internas
        tabuleiro = [[] for _ in range(2 * n)]

        # Cria uma string com n espaços em branco
        pos = ' ' * (2 * n)

        # Preenche cada lista interna com n pedras neutras
        for i in range(2 * n):
            for j in range(2 * n):
                tabuleiro[i] += [cria_pedra_neutra()]

        return tabuleiro
    raise ValueError('cria_tabuleiro_vazio: argumento invalido')

def cria_tabuleiro(n, tab_pretas, tab_brancas):
    """
    Cria um tabuleiro de jogo com o tamanho n x n e as posições de pedras pretas e brancas.

    O tabuleiro é representado por uma lista de listas, onde cada lista interna
    representa uma linha do tabuleiro e cada elemento da lista interna representa
    uma coluna do tabuleiro. Cada elemento da lista interna é uma pedra.

    Argumentos:
        n (int): O tamanho do tabuleiro (n x n).
        tab_pretas (tuple): Um tuplo com as posições das pedras pretas.
        tab_brancas (tuple): Um tuplo com as posições das pedras brancas.

    Retorna:
        list: O tabuleiro de jogo.

    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    # Verifica se o tamanho do tabuleiro é válido
    if not type(n) == int or not (2 <= n <= 5):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    # Cria um tabuleiro vazio com o tamanho n x n
    t = cria_tabuleiro_vazio(n)

    # Verifica se os argumentos são tuplos
    if not type(tab_pretas) == tuple or not type(tab_brancas) == tuple:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    # Itera sobre as posições das pedras pretas
    for posicao in tab_pretas:
        print(posicao)
        posicao = str_para_posicao(posicao)
        # Verifica se a posição é válida
        if not type(posicao) == tuple or len(posicao) != 2:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Extrai a coluna e a linha da posição
        coluna = obtem_pos_col(posicao)
        linha = obtem_pos_lin(posicao) 

        # Verifica se a coluna e a linha são válidas
        if not type(coluna) == str or not type(linha) == int:
            raise ValueError( 'cria_tabuleiro: argumentos invalidos')

        # Verifica se a coluna está dentro do intervalo válido
        if not 'a' <= coluna <= 'j':
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Verifica se a linha está dentro do intervalo válido
        if not 1 <= linha <= 10:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Verifica se a posição é válida no tabuleiro
        if not eh_posicao_valida(posicao, n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Converte a coluna e a linha para índices
        col = ord(str(obtem_pos_col(posicao))) - ord('a')
        lin = obtem_pos_lin(posicao) - 1
        
        # Adiciona a pedra preta no tabuleiro
        t[lin][col] = cria_pedra_preta()

    # Itera sobre as posições das pedras brancas
    for posicao in tab_brancas:
        posicao = str_para_posicao(posicao)

        # Verifica se a posição é válida
        if not type(posicao) == tuple or len(posicao) != 2:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Extrai a coluna e a linha da posição
        coluna = obtem_pos_col(posicao)
        linha = obtem_pos_lin(posicao) 

        # Verifica se a coluna e a linha são válidas
        if not type(coluna) == str or not type(linha) == int:
            raise ValueError( 'cria_tabuleiro: argumentos invalidos')

        # Verifica se a coluna está dentro do intervalo válido
        if not 'a' <= coluna <= 'j':
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Verifica se a linha está dentro do intervalo válido
        if not 1 <= linha <= 10:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Verifica se a posição é válida no tabuleiro
        if not eh_posicao_valida(posicao, n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')

        # Converte a coluna e a linha para índices
        col = ord(str(obtem_pos_col(posicao))) - ord('a')
        lin = obtem_pos_lin(posicao) - 1
        
        # Adiciona a pedra branca no tabuleiro
        t[lin][col] = cria_pedra_branca()

    # Retorna o tabuleiro
    return t

def cria_copia_tabuleiro(t):
    """
    Cria uma cópia do tabuleiro de jogo.

    A cópia é uma lista de listas, onde cada lista interna representa uma linha do tabuleiro.
    Cada elemento da lista interna é uma pedra.

    Argumentos:
        t (list): O tabuleiro de jogo original.

    Retorna:
        list: A cópia do tabuleiro de jogo.
    """
    # Cria uma lista vazia para a cópia do tabuleiro
    copia = []
    
    # Itera sobre cada linha do tabuleiro original
    for linha in t:
        # Cria uma cópia da linha atual
        copia += [linha.copy()]
    
    # Retorna a cópia do tabuleiro
    return copia.copy()


# Seletores
def obtem_numero_orbitas(t):
    """
    Calcula o número de órbitas no tabuleiro.

    O número de órbitas é definido como a metade do tamanho do tabuleiro.

    Argumentos:
        t (list): O tabuleiro de jogo.

    Retorna:
        int: O número de órbitas no tabuleiro.
    """
    # Calcula a metade do tamanho do tabuleiro
    n = len(t) // 2
    return n

def obtem_pedra(t, p):
    """
    Obtém a pedra na posição dada no tabuleiro.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').

    Retorna:
        tuple: A pedra na posição dada (ex. ('branca', 'inteira')).
    """
    col = ord(obtem_pos_col(p)) - ord('a')  # Cálculo do índice da coluna
    lin = obtem_pos_lin(p) - 1  # Cálculo do índice da linha
    return t[lin][col]  # Devolver a pedra na posição dada

def obtem_pos(col, lin):
    """
    obtem_pos: int × int → str
    Cria a posição correspondente aos índices dados.

    Recebe uma coluna (inteiro) e uma linha (inteiro), e devolve uma string
    representando a posição.

    Argumentos:
        col (int): O índice da coluna da posição (0 a 9)
        lin (int): O índice da linha da posição (0 a 9)

    Devolve:
        str: Uma string ('{coluna}{linha}') representando a posição no tabuleiro.
    """
    col_pos = chr(ord('a') + col)      # Cálculo da letra correspondente ao índice dado
    lin_pos = lin + 1           # Cálculo do número correspondente ao índice dado
    return f'{col_pos}{lin_pos}'    # Devolver a string da posição

def obtem_linha_horizontal(t, p):
    """
    Obtém a linha horizontal do tabuleiro na posição dada.

    A linha horizontal é um tuplo com as posições e os respetivos valores
    na linha do tabuleiro que inclui a posição dada.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').

    Retorna:
        tuple: A linha horizontal do tabuleiro na posição dada.
    """
    lin = obtem_pos_lin(p)
    horizontal = ()
    for col, valor in enumerate(t[lin - 1]):    # Itera dentro da linha da posição dada
        horizontal += ((obtem_pos(col, lin - 1), valor),)   # Cria o tuplo com a posição e o seu respetivo valor
    return horizontal

def obtem_linha_vertical(t, p):
    """
    Obtém a linha vertical do tabuleiro na posição dada.

    A linha vertical é um tuplo com as posições e os respetivos valores
    na coluna do tabuleiro que inclui a posição dada.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').

    Retorna:
        tuple: A linha vertical do tabuleiro na posição dada.
    """
    col = ord(obtem_pos_col(p)) - ord('a')   # Cálculo do índice da coluna da posição dada
    n = obtem_numero_orbitas(t)
    _ ,lin_tab = obtem_dimensoes_tab(n)
    vertical = ()
    for i in range(lin_tab):
        for valor in t[i][col]:   # Itera em cada linha na coluna da posição dada
            vertical += ((obtem_pos(col, i), valor),)   # Cria o tuplo com a posição e o seu respetivo valor
    return vertical

def obtem_linhas_diagonais(t, p):
    """
    Obtém as linhas diagonais do tabuleiro na posição dada.

    As linhas diagonais são dois tuplos com as posições e os respetivos valores
    nas diagonais do tabuleiro que inclui a posição dada.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').

    Retorna:
        tuple: Os dois tuplos com as linhas diagonais do tabuleiro na posição dada.
    """
    col = ord(obtem_pos_col(p)) - ord('a')   # Cálculo das dimensões da posição dada
    lin = int(obtem_pos_lin(p)) - 1
    n = obtem_numero_orbitas(t)
    col_tab = ord(obtem_dimensoes_tab(n)[0]) - ord('a')    # Cálculo das dimensões do tabuleiro
    lin_tab = obtem_dimensoes_tab(n)[1]
    diag = ()
    anti = ()

    # Função recursiva para encontrar a primeira posição da diagonal
    # que passa pela posição dada
    def obtem_pos_min_diag(col, lin):
        """
        Função recursiva para encontrar a primeira posição da diagonal
        que passa pela posição dada.

        Argumentos:
            col (int): O índice da coluna da posição dada.
            lin (int): O índice da linha da posição dada.

        Retorna:
            str: A primeira posição da diagonal que passa pela posição dada.
        """
        col_x = chr(ord('a') + col)
        lin_y = lin + 1
        if not (col > 0 and lin > 0):       # Enquanto nem a coluna nem a linha chegarem \
            return f'{col_x}{lin_y}'    # às bordas do tabuleiro continuar à procura da posição
        return obtem_pos_min_diag(col - 1, lin - 1)

    col_diag = ord(obtem_pos_min_diag(col, lin)[0]) - ord('a')   # Obter dimensões da menor posiçao pertencente à diagonal
    lin_diag = int(obtem_pos_min_diag(col, lin)[1]) - 1

    # Itera em linha na coluna da posição dada e adiciona os valores à diagonal
    while col_diag <= col_tab and lin_diag <= lin_tab - 1:
        for valor in t[lin_diag][col_diag]:
            diag += ((obtem_pos(col_diag, lin_diag), valor),)
            col_diag += 1
            lin_diag += 1

    # Função recursiva para encontrar a primeira posição da antidiagonal
    # que passa pela posição dada
    def obtem_pos_min_anti(col, lin):
        """
        Função recursiva para encontrar a primeira posição da antidiagonal
        que passa pela posição dada.

        Argumentos:
            col (int): O índice da coluna da posição dada.
            lin (int): O índice da linha da posição dada.

        Retorna:
            str: A primeira posição da antidiagonal que passa pela posição dada.
        """
        col_x = chr(ord('a') + col)
        lin_y = lin + 1
        if not (col > 0 and lin + 1 < lin_tab):  # Enquanto nem a coluna nem a linha chegarem
            return f'{col_x}{lin_y}'  # às bordas do tabuleiro continuar à procura da posição
        return obtem_pos_min_anti(col - 1, lin + 1)

    col_anti = ord(obtem_pos_min_anti(col, lin)[0]) - ord('a')  # Obter dimensões da posiçao mais à esquerda pertencente à diagonal
    lin_anti = int(obtem_pos_min_anti(col, lin)[1]) - 1

    # Itera em cada linha na coluna da posição dada e adiciona os valores à antidiagonal
    while col_anti <= col_tab and lin_anti >= 0:
        for valor in t[lin_anti][col_anti]:
            anti += ((obtem_pos(col_anti, lin_anti), valor),)
            col_anti += 1
            lin_anti -= 1
    return diag, anti

def obtem_posicoes_pedra(t, j):
    """
    Obtém as posições de pedras de um determinado jogador no tabuleiro.

    Argumentos:
        t (list): O tabuleiro de jogo.
        j (qualquer tipo): O valor da pedra do jogador.

    Retorna:
        tuple: Um tuplo com as posições das pedras do jogador, ordenadas pela proximidade ao centro.
    """
    if not (type(t) is list and type(j) is not None):
        raise ValueError('obtem_posicoes_pedra: argumentos invalidos')

    posicoes = ()  # Inicializa o tuplo para armazenar as posições das pedras
    n = obtem_numero_orbitas(t)  # Calcula o número de órbitas no tabuleiro
    for l, linha in enumerate(t):
        if not type(linha) is list:
            raise ValueError('obtem_posicoes_pedra: tabuleiro invalido')
        for c, valor in enumerate(linha):
            if valor == j:  # Verifica se o valor é igual à pedra do jogador
                posicoes += (obtem_pos(c, l),)  # Adiciona a posição da pedra ao tuplo
    return ordena_posicoes(posicoes, n) if posicoes else ()  # Ordena as posições pela proximidade ao centro e retorna

def coloca_pedra(t, p, j):
    """
    Coloca uma pedra no tabuleiro.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').
        j (pedra): A pedra a ser colocada na posição.

    Retorna:
        list: O tabuleiro de jogo modificado.
    """
    col = ord(obtem_pos_col(p)) - ord('a')      # Cálculo do índice da coluna
    lin = obtem_pos_lin(p) - 1                  # Cálculo do índice da linha
    t[lin][col] = j                            # Coloca a pedra na posição dada
    return t

def remove_pedra(t, p):
    """
    Remove uma pedra do tabuleiro.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição no tabuleiro (ex. 'a1').

    Retorna:
        list: O tabuleiro de jogo modificado.
    """
    t = coloca_pedra(t, p, cria_pedra_neutra())  # Coloca a pedra neutra na posição dada
    return t  # Retorna o tabuleiro de jogo modificado


# Reconhecedor
def eh_tabuleiro(t):
    """
    Verifica se um objeto é um tabuleiro de jogo válido.

    Um tabuleiro é uma lista de listas, onde cada lista interna tem o mesmo tamanho,
    e cada elemento da lista interna é uma pedra (ou seja, um objeto criado com
    cria_pedra_neutra, cria_pedra_branca ou cria_pedra_preta).

    Argumentos:
        t (list): O objeto a ser verificado.

    Retorna:
        bool: True se o objeto for um tabuleiro, False caso contrário.
    """
    return isinstance(t, list) and 4 <= len(t) <= 10 and \
        all((isinstance(lin, list) and 4 <= len(lin) <= 10 and \
             len(lin) == (obtem_numero_orbitas(t) * 2) for lin in t)) and \
            all(type(val) == type(cria_pedra_neutra()) and \
                val in (cria_pedra_neutra(), cria_pedra_branca(), cria_pedra_preta()) \
                for lin in t for val in lin)


# Teste    
def tabuleiros_iguais(t1, t2):
    """
    Verifica se dois tabuleiros são iguais.

    Argumentos:
        t1 (list): O primeiro tabuleiro a ser comparado.
        t2 (list): O segundo tabuleiro a ser comparado.

    Retorna:
        bool: True se os tabuleiros forem iguais, False caso contrário.
    """
    return t1 == t2  # Compara os dois tabuleiros e retorna o resultado


# Transformador
def tabuleiro_para_str(t):
    """
    Converte um tabuleiro em uma string formatada para visualização.

    O tabuleiro é representado como uma string com linhas e colunas numeradas,
    e cada elemento da lista interna é representado por uma string que pode ser:
    - "[X]" para uma pedra branca
    - "[O]" para uma pedra preta
    - "[ ]" para uma pedra neutra

    Argumentos:
        t (list): O tabuleiro a ser convertido.

    Retorna:
        str: A string formatada para visualização do tabuleiro.
    """
    r = ' '  # Espaço adicional para alinhar a primeira linha
    n = obtem_numero_orbitas(t)  # Número de colunas do tabuleiro
    for indice in range((n * 2)):
        r += f'   {obtem_pos_col(obtem_pos(indice, 0))}'  # Adiciona o número da coluna
    for i, lin in enumerate(t):
        r += '\n'  # Quebra de linha
        if i == 9:  # Caso especial para a linha 10
            r += f'{i + 1} '
        else:
            r += f'0{i + 1} '  # Adiciona o número da linha
        for j, col in enumerate(lin):
            if col == cria_pedra_preta():
                col = f'[{cria_pedra_preta()}]'
            elif col == cria_pedra_branca():  # Verificar se c pode ser != de 1, se n for poe else
                col = f'[{cria_pedra_branca()}]'
            else:
                col = f'[{cria_pedra_neutra()}]'
            r += str(col)  # Adiciona a pedra formatada
            if j < ((n * 2) - 1):  # Para que não apareça '---' no final
                r += '-'  # Adiciona o traço para separar as colunas
        if i < ((n * 2) - 1):  # Para que não apareça '---' no final
            r += '\n' + ' ' + '   |' * (n * 2)  # Adiciona a linha separadora
    return r


# Funções A.N.
def move_pedra(t, p1, p2):
    """
    Move uma pedra do tabuleiro de uma posição para outra.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p1 (str): A posição atual da pedra.
        p2 (str): A posição destino da pedra.

    Retorna:
        list: O tabuleiro de jogo com a pedra movida.
    """
    pedra = obtem_pedra(t, p1)
    t = remove_pedra(t, p1)
    t = coloca_pedra(t, p2, pedra)
    return t

def obtem_posicao_seguinte(t, p, s):
    """
    Retorna a próxima posição no tabuleiro na direção especificada.

    Argumentos:
        t (list): O tabuleiro de jogo.
        p (str): A posição atual no tabuleiro.
        s (bool): Se True, retorna a próxima posição no sentido horário, 
            caso contrário, retorna a próxima posição no sentido anti-horário.

    Retorna:
        str: A próxima posição no tabuleiro.
    """
    def obtem_dimensoes_orbita(t, p):
        """
        Retorna as dimensões da órbita do tabuleiro.

        Argumentos:
            t (list): O tabuleiro de jogo.
            p (str): A posição do tabuleiro.

        Retorna:
            tuple: A posição inicial e final da órbita.
        """
        n = obtem_numero_orbitas(t)
        # A primeira coluna e linha da órbita
        prim_col = obtem_pos(0, 0)[0] 
        prim_lin = int(obtem_pos(0, 0)[1])
        # A última coluna e linha da órbita
        ult_col = obtem_dimensoes_tab(n)[0]
        ult_lin = int(obtem_dimensoes_tab(n)[1])
        # A coluna e linha da posição atual
        col, lin = obtem_pos_col(p), obtem_pos_lin(p)
        
        # Verifica se a posição atual está na borda da órbita
        for i in range(n):
            if  col == prim_col and prim_lin <= lin <= ult_lin\
                or col == ult_col and prim_lin <= lin <= ult_lin\
                    or lin == prim_lin and prim_col <= col <= ult_col\
                        or lin == ult_lin and prim_col <= col <= ult_col:
                            return (prim_col, prim_lin), (ult_col, ult_lin)
            # Se a posição não estiver na borda, aumenta a distância da borda
            if n + 1 == i:   
                return (prim_col, prim_lin), (ult_col, ult_lin)
            prim_col = chr(ord(prim_col) + 1)
            prim_lin +=1
            ult_col = chr(ord(ult_col) - 1)
            ult_lin -= 1

    col, lin = obtem_pos_col(p), obtem_pos_lin(p)
    pos = posicao_para_str((col, lin))
    prim_pos, ult_pos = obtem_dimensoes_orbita(t, p)
    p = str_para_posicao(p)

    def obtem_vetor(t, p, sentido_horario):
        """
        Retorna o vetor de movimento para a próxima posição.

        Argumentos:
            t (list): O tabuleiro de jogo.
            p (str): A posição do tabuleiro.
            sentido_horario (bool): Se True, retorna o vetor de movimento no sentido horário,
                caso contrário, retorna o vetor de movimento no sentido anti-horário.

        Retorna:
            list: O vetor de movimento.
        """
        vetores = []
        # Obtem as linhas e colunas da órbita do tabuleiro
        prim_vertical = (posicao[0] for posicao in obtem_linha_vertical(t, prim_pos))
        prim_horizontal = (posicao[0] for posicao in obtem_linha_horizontal(t, prim_pos))
        ult_vertical = (posicao[0] for posicao in obtem_linha_vertical(t, ult_pos))
        ult_horizontal = (posicao[0] for posicao in obtem_linha_horizontal(t, ult_pos))

        # Verifica se a posição atual é uma das bordas da órbita
        if sentido_horario:
            if p == prim_pos: 
                vetores = [(1, 0)]  # Vai para a direita
            elif p == (prim_pos[0], ult_pos[1]): 
                vetores = [(0, -1)]  # Vai para cima
            elif p == ult_pos: 
                vetores = [(-1, 0)]  # Vai para a esquerda
            elif p == (ult_pos[0], prim_pos[1]):
                vetores = [(0, 1)]  # Vai para baixo

            # Verifica se a posição atual está em uma das linhas ou colunas da borda
            elif pos in prim_vertical:
                vetores = [(0, -1)]  
            elif pos in prim_horizontal:
                vetores = [(1, 0)]
            elif pos in ult_vertical:
                vetores = [(0, 1)]
            elif pos in ult_horizontal:
                vetores = [(-1, 0)]
        else:
            if p == prim_pos:
                vetores = [(0, 1)]  # Vai para baixo
            elif p == (prim_pos[0], ult_pos[1]): 
                vetores = [(1, 0)]  # Vai para a direita
            elif p == ult_pos: 
                vetores = [(0, -1)]  # Vai para cima
            elif p == (ult_pos[0], prim_pos[1]):
                vetores = [(-1, 0)]  # Vai para a esquerda

            # Verifica se a posição atual está em uma das linhas ou colunas da borda
            elif pos in prim_vertical:
                vetores = [(0, 1)]  
            elif pos in prim_horizontal:
                vetores = [(-1, 0)]
            elif pos in ult_vertical:
                vetores = [(0, -1)]
            elif pos in ult_horizontal:
                vetores = [(1, 0)]

        return vetores
    
    vetor = obtem_vetor(t, p, s)
    for vx, vy in vetor:
            nova_col = chr(ord(col) + vx)
            nova_lin = lin + vy
            nova_pos = cria_posicao(nova_col, nova_lin)
            
            if eh_posicao_valida(nova_pos, obtem_numero_orbitas(t)):
                return nova_pos

    return None

def roda_tabuleiro(t):
    """
    Roda o tabuleiro 90 graus para a esquerda.

    Argumentos:
        t (tuple): O tabuleiro de jogo.

    Retorna:
        tuple: O tabuleiro de jogo rotado.

    Raises:
        ValueError: Se o tabuleiro não for válido.
    """
    if not eh_tabuleiro(t):
        raise ValueError ("roda _tabuleiro: argumentos invalidos")
    
    # Guarda as posições e os valores das peças pretas e brancas no tabuleiro
    pos_anterior = {}
    for posicao in obtem_posicoes_pedra(t, cria_pedra_preta()):
        pos_anterior [posicao] = pedra_para_int(obtem_pedra(t, posicao))
        remove_pedra(t, posicao) 
    for posicao in obtem_posicoes_pedra(t,cria_pedra_branca()):
        pos_anterior [posicao] = pedra_para_int(obtem_pedra(t, posicao))
        remove_pedra(t, posicao)
    
    # Coloca as peças pretas e brancas nas suas novas posições
    for posicao in pos_anterior:
        pedra = cria_pedra_branca() if pos_anterior[posicao] == pedra_para_int(cria_pedra_branca()) else cria_pedra_preta()
        coloca_pedra(t, obtem_posicao_seguinte(t, posicao, False), pedra)
    return t

def verifica_linha_pedras(t, p, j, k): 
    """
    Verifica se o jogador j tem k ou mais posições consecutivas na linha, coluna, diagonal ou antidiagonal do tabuleiro t que contenha a posição p.

    Argumentos:
        t (tuple): O tabuleiro de jogo.
        p (tuple): A posição que se deseja verificar.
        j (int): O jogador, 1 ou -1.
        k (int): O número de posições consecutivas a ser verificado.

    Retorna:
        bool: True se o jogador j tem k ou mais posições consecutivas, False caso contrário.
    """
    coluna = obtem_linha_vertical(t, p)
    linha = obtem_linha_horizontal(t, p)
    diagonal, antidiagonal = obtem_linhas_diagonais(t, p)
    
    def obtem_consecutivos(tuplo):
        """
        Calcula o maior número de posições consecutivas de um jogador em uma tupla.

        Argumentos:
            tuplo (tuple): Tupla de posições no tabuleiro.

        Retorna:
            int: O número máximo de posições consecutivas do jogador.

        """
        posicao_dada = False
        consecutivos = 0  
        max_consecutivos = 0  
        
        for valor in tuplo:
            # Se o valor corresponde à posição do jogador, incrementa a contagem de consecutivos
            if valor[1] == j:
                consecutivos += 1
                max_consecutivos = consecutivos
                # Verifica se a posição atual é a posição dada
                if valor[0] == posicao_para_str(p):
                    posicao_dada = True
            else:
                # Reinicia a contagem de consecutivos se não for a posição do jogador
                consecutivos = 0
        
        # Retorna o máximo de consecutivos se a posição dada foi encontrada
        return max_consecutivos if posicao_dada else 0
        
    if obtem_consecutivos(linha) == k or obtem_consecutivos(coluna) == k\
        or obtem_consecutivos(diagonal) == k\
            or obtem_consecutivos(antidiagonal) == k:
       # Caso o maior número de posições do jogador consecutivas for igual a k devolver True
                return True         
    return False


# Funções Adicionais
def eh_vencedor(t, pedra):
    """
    Verifica se o jogador com a pedra especificada ganhou o jogo.

    Argumentos:
        t (tuple): O tabuleiro de jogo.
        pedra (tuple): A pedra do jogador, branca ou preta.

    Retorna:
        bool: True se o jogador ganhou, False caso contrário.
    """
    k = obtem_numero_orbitas(t) * 2
    # Verifica se o jogador tem uma linha de pedras consecutivas
    for pos in obtem_posicoes_pedra(t, pedra):
        if verifica_linha_pedras(t, pos, pedra, k):
            # Se o jogador tem uma linha de pedras consecutivas, retorna True
            return True

    # Se o jogador não tem uma linha de pedras consecutivas, retorna False
    return False

def eh_fim_jogo(t):
    """
    Verifica se o jogo terminou.

    O jogo termina se houver um vencedor ou se todas as posições do tabuleiro
    estiverem ocupadas.

    Argumentos:
        t (tuple): O tabuleiro de jogo.

    Retorna:
        bool: True se o jogo terminou, False caso contrário.
    """
    # Verifica se o jogo terminou devido a um vencedor
    if eh_vencedor(t, cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()):
        return True

    # Verifica se o jogo terminou devido a todas as posições estarem ocupadas
    total_pedras = len(obtem_posicoes_pedra(t, cria_pedra_branca())) + len(obtem_posicoes_pedra(t, cria_pedra_preta()))
    if total_pedras == (obtem_numero_orbitas(t) * 2) ** 2:
        return True

    # Se não houver vencedor e ainda houver posições livres, o jogo não terminou
    return False

def escolhe_movimento_manual(t):
    """
    Permite ao jogador escolher manualmente uma posição livre no tabuleiro.

    Argumentos:
        t (tuple): O tabuleiro de jogo.

    Retorna:
        str: A posição escolhida pelo jogador.
    """
    while True:
        # Pede ao jogador que escolha uma posição
        posicao = input('Escolha uma posicao livre:')
        # Verifica se a posição escolhida é válida
        posicao = str_para_posicao(posicao)
        if eh_posicao(posicao) and eh_posicao_valida(posicao, obtem_numero_orbitas(t)) \
            and obtem_pedra(t, posicao) == cria_pedra_neutra():
            # Se a posição for válida, retorna a posição escolhida
            return posicao_para_str(posicao)

def desroda_tabuleiro(t):
    """
    Desroda o tabuleiro 90 graus para a direita.

    Argumentos:
        t (tuple): O tabuleiro de jogo.

    Retorna:
        tuple: O tabuleiro de jogo desrodado.

    Raises:
        ValueError: Se o tabuleiro não for válido.
    """
    # Verifica se o tabuleiro é válido
    if not eh_tabuleiro(t):
        raise ValueError ("desroda _tabuleiro: argumentos invalidos")

    # Guarda as posições e os valores das peças pretas e brancas no tabuleiro
    pos_anterior = {}
    for posicao in obtem_posicoes_pedra(t, cria_pedra_preta()):
        pos_anterior [posicao] = pedra_para_int(obtem_pedra(t, posicao))
        remove_pedra(t, posicao) 
    for posicao in obtem_posicoes_pedra(t,cria_pedra_branca()):
        pos_anterior [posicao] = pedra_para_int(obtem_pedra(t, posicao))
        remove_pedra(t, posicao)

    # Coloca as peças pretas e brancas nas suas novas posições
    for posicao in pos_anterior:
        pedra = cria_pedra_branca() if pos_anterior[posicao] == pedra_para_int(cria_pedra_branca()) else cria_pedra_preta()
        coloca_pedra(t, obtem_posicao_seguinte(t, posicao, True), pedra)

    return t
    
    def obtem_consecutivos(tuplo): 
        """
        Calcula o maior número de posições consecutivas de um jogador em uma tupla.

        Argumentos:
            tuplo (tuple): Tupla de posições no tabuleiro.

        Retorna:
            int: O número máximo de posições consecutivas do jogador.

        """
        posicao_dada = False
        consecutivos = 0  
        max_consecutivos = 0  
        for valor in tuplo:
            # Se o valor do tuplo dado for posição do jogador, incrementa a contagem de consecutivos
            if valor[1] == j:
                consecutivos += 1
                max_consecutivos = consecutivos
                # Verifica se a posição atual é a posição dada
                if valor[0] == posicao_para_str(p):
                    posicao_dada = True
            else:
                # Reinicia a contagem de consecutivos se não for a posição do jogador
                consecutivos = 0
    
        # Retorna o máximo de consecutivos se a posição dada foi encontrada
        return max_consecutivos if posicao_dada else 0
        
    if obtem_consecutivos(linha) == k or obtem_consecutivos(coluna) == k:
       # Caso o maior número de posições do jogador consecutivas for igual a k devolver True
                return True         
    return False

def escolhe_movimento_auto(t, pedra, lvl):
    """
    Escolhe automaticamente uma posição no tabuleiro de acordo com a estratégia escolhida.
    
    Argumentos:
        t (tuple): O tabuleiro de jogo.
        pedra (tuple): A pedra a ser jogada.
        lvl (str): O nível de dificuldade da estratégia ('facil' ou 'normal').
    
    Retorna:
        str: A posição escolhida automaticamente.
    """
    
    def estrategia_facil(t, pedra):
        """
        Implementa a estratégia fácil para o computador escolher uma posição.
        
        Argumentos:
            t (tuple): O tabuleiro de jogo.
            pedra (tuple): A pedra a ser jogada.
        
        Retorna:
            str: A posição escolhida automaticamente.
        """
        # Roda o tabuleiro
        roda_tabuleiro(t)
        
        n = obtem_numero_orbitas(t)
        # Obtém as posições possíveis para jogar
        posicoes_possiveis = []
        posicoes_jogador = obtem_posicoes_pedra(t, pedra)
        for pos in posicoes_jogador:
            for adj in obtem_posicoes_adjacentes(pos, n, True):
                if eh_posicao(adj) and eh_posicao_valida(adj, n) and\
                    obtem_pedra(t, adj) == cria_pedra_neutra() and adj not in posicoes_possiveis:
                        posicoes_possiveis += [adj]
        # Desroda o tabuleiro para que a próxima jogada seja feita com o tabuleiro original
        desroda_tabuleiro(t)
        
        # Verifica se há posições possíveis para jogar
        if posicoes_possiveis != []:
            # Obtém a próxima posição para jogar
            resultado = obtem_posicao_seguinte(t, ordena_posicoes(posicoes_possiveis, n)[0], True)
            return resultado
        
        # Caso não haja posições possíveis, escolha a posição mais próxima do centro
        posicoes_livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
        return ordena_posicoes(posicoes_livres, n)[0]


    def estrategia_normal(t, pedra):
        """
        Implementa a estratégia normal para o computador escolher uma posição.

        Argumentos:
            t (tuple): O tabuleiro de jogo.
            pedra (tuple): A pedra a ser jogada.

        Retorna:
            str: A posição escolhida automaticamente.
        """
        dimensao_t = obtem_numero_orbitas(t)
        posicoes_livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
        resultado = None
        max_k = 0

        # Roda o tabuleiro para avaliar as posições
        t_rodado = roda_tabuleiro(cria_copia_tabuleiro(t))
        for pos in posicoes_livres:
            # Obtém a posição seguinte para cada posição livre
            posicao_seguinte = obtem_posicao_seguinte(t, pos, False)
            t_copia = cria_copia_tabuleiro(t_rodado)
            # Coloca a pedra na posição seguinte
            coloca_pedra(t_copia, posicao_seguinte, pedra)
            
            # Verifica a linha de pedras
            for k in range(1, dimensao_t + 1):
                if verifica_linha_pedras(t_copia, posicao_seguinte, pedra, k):
                    if k > max_k:
                        max_k = k
                        resultado = pos

        # Se não encontrar resultado ou a linha máxima é menor que a dimensão
        if resultado is None or max_k < dimensao_t:
            # Determina a pedra do adversário
            pedra_adversario = cria_pedra_branca() if pedras_iguais(pedra, cria_pedra_preta()) else cria_pedra_preta()

            # Roda o tabuleiro do adversário
            t_rodado_adver = roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(t)))
            for pos_adver in posicoes_livres:
                # Obtém a posição seguinte para o adversário
                pos_seguinte_adver = obtem_posicao_seguinte(t, obtem_posicao_seguinte(t, posicao_para_str(pos_adver), False), False)
                t_copia_adver = cria_copia_tabuleiro(t_rodado_adver)
                # Coloca a pedra do adversário na posição seguinte
                coloca_pedra(t_copia_adver, pos_seguinte_adver, pedra_adversario)

                # Verifica a linha de pedras para o adversário
                for k in range(1, dimensao_t + 1):
                    if verifica_linha_pedras(t_copia_adver, pos_seguinte_adver, pedra_adversario, k):
                        if k > max_k:
                            max_k = k
                            resultado = pos_adver

        # Se ainda não há resultado, escolhe a posição mais próxima do centro
        if resultado is None and posicoes_livres:
            resultado = ordena_posicoes(posicoes_livres, dimensao_t)[0]
        return resultado
        
    if lvl == 'facil':
        return estrategia_facil(t, pedra)
    elif lvl == 'normal':
        return estrategia_normal(t, pedra)

def orbito(n, modo, jog):
    """
    Inicia um jogo de ORBITO.
    Argumentos:
        n (int): O tamanho do tabuleiro.
        modo (str): O modo de jogo ('facil', 'normal' ou '2jogadores').
        jog (str): A pedra do jogador ('X' ou 'O').
    Retorna:
        int: 1 se o jogador vencer, -1 se o jogador perder, 0 em caso de empate.
    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
    """
    if not (type(n) == int and 2 <= n <= 5 and type(modo) == str\
            and modo in ['facil', 'normal', '2jogadores']\
                and type(jog) == str and jog in ['X', 'O']):
                    raise ValueError('orbito: argumentos invalidos')
     
    pedra_atual = cria_pedra_preta()

    # Cria um tabuleiro vazio com o tamanho especificado
    t = cria_tabuleiro_vazio(n)
    k = n * 2
    
    # Define a pedra adversária
    if jog == cria_pedra_preta():
        jog_adversario = cria_pedra_branca()   
    else:
        jog_adversario = cria_pedra_preta()

    # Jogo contra o computador
    if modo == 'facil' or modo == 'normal':
        print(f"Bem-vindo ao ORBITO-{n}.")
        print(f"Jogo contra o computador ({modo}).")
        print(f"O jogador joga com '{jog}'.")
        print(tabuleiro_para_str(t))
   
        while not eh_fim_jogo(t):
            if jog == pedra_atual:
                print('Turno do jogador.') 
                pos = escolhe_movimento_manual(t)
            else:
                print(f'Turno do computador ({modo}):')
                pos = escolhe_movimento_auto(t, jog, modo)
                
            coloca_pedra(t, pos, pedra_atual)
            roda_tabuleiro(t)
            print(tabuleiro_para_str(t))


            if eh_fim_jogo(t):
                if eh_vencedor(t, jog):
                    print("VITORIA")
                    if jog == cria_pedra_preta():
                        resultado = 1
                    else:
                        resultado = -1
                elif eh_vencedor(t, jog_adversario):
                    print("DERROTA") 
                    if jog_adversario == cria_pedra_preta():
                        resultado = -1
                    else:
                        resultado = 1   
                else:
                    print("EMPATE")
                    resultado = 0
                break

            if pedra_atual == cria_pedra_preta():
                pedra_atual = cria_pedra_branca()
            else:
                pedra_atual = cria_pedra_preta()
            
    
    # Jogo para dois jogadores
    elif modo == '2jogadores':
        print(f"Bem-vindo ao ORBITO-{n}.")
        print('Jogo para dois jogadores.')
        print(tabuleiro_para_str(t))

        while not eh_fim_jogo(t):
            print(f"Turno do jogador '{pedra_atual}'.")
            pos = escolhe_movimento_manual(t)
            coloca_pedra(t, pos, pedra_atual)
            
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))    

            if eh_fim_jogo(t):
                if eh_vencedor(t, jog):
                    print("VITORIA DO JOGADOR 'X'")
                    resultado = 1
                elif eh_vencedor(t, jog_adversario):
                    print("VITORIA DO JOGADOR 'O'")  
                    resultado = -1  
                else:
                    print("EMPATE")
                    resultado = 0
                break

            if pedra_atual == cria_pedra_preta():
                pedra_atual = cria_pedra_branca()
            else:
                pedra_atual = cria_pedra_preta()
    
    return resultado