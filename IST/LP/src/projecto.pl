% lp24 - ist1114538 - projecto 
:- use_module(library(clpfd)). % para poder usar transpose/2
:- set_prolog_flag(answer_write_options,[max_depth(0)]). % ver listas completas
:- [puzzles]. % Ficheiro dado. A avaliação terá mais puzzles.
:- [codigoAuxiliar]. % Ficheiro dado. Não alterar.
% Atenção: nao deves copiar nunca os puzzles para o teu ficheiro de código
% Nao remover nem modificar as linhas anteriores. Obrigado.
% Segue-se o código
%%%%%%%%%%%%



% 5.1 - Visualização
% visualiza(Lista): Imprime cada elemento de uma lista numa linha separada.
%   Lista: Lista a ser impressa.

visualiza([]) :- !.     % Caso base, lista vazia
visualiza([H|T]) :- 
    writeln(H),        % Imprime um elemento da lista numa linha
    visualiza(T).      % Recursão para o resto da lista



% visualizaLinha(Lista): Imprime cada elemento de uma lista, precedido pelo índice da linha.
%   Lista: Lista a ser impressa.

visualizaLinha([], _):- !.      % Caso base, lista vazia
visualizaLinha([H|T], Indice) :- 
    write(Indice), write(": "),     % Imprime o índice da linha
    writeln(H),                     % Imprime o elemento da lista
    Indice1 is Indice + 1,         % Incrementa o índice
    visualizaLinha(T, Indice1).     % Recursão para o resto da lista

visualizaLinha(Lista) :- 
    visualizaLinha(Lista, 1).     % Aumento da aridade da função para poder guardar o índice



% 5.2 - Inserção de estrelas e pontos
% insereObjecto((L,C), Tabuleiro, Obj): Insere o objecto dado na coordenada dada do Tabuleiro, se a posição estiver vazia.
%   Tabuleiro: Tabuleiro a ser modificado.
%   (L,C): Coordenada a ser modificada.
%   Obj: Objecto a ser inserido.

% FUNÇÃO AUXILIAR para obter o objecto de uma coordenada
obtemObjecto((L, C), Tabuleiro, Pos) :-        
    verificaCoordenada(Tabuleiro, (L, C)),   % Verifica se a coordenada pertence ao Tabuleiro para nth1/3 não falhar
    nth1(L, Tabuleiro, Linha),
    nth1(C, Linha, Pos).

% FUNÇÃO AUXILIAR para verificar se uma linha pertence ao Tabuleiro
verificaLinha(Tabuleiro, L) :-                  
    length(Tabuleiro, LenLinha), 
    L =< LenLinha, L > 0.

% FUNÇÃO AUXILIAR para verificar se uma coluna pertence ao Tabuleiro
verificaColuna([H|_], C) :-                     
    length(H, LenColuna), 
    C =< LenColuna, C > 0.

% FUNÇÃO AUXILIAR para verificar se uma coordenada pertence ao Tabuleiro
verificaCoordenada(Tabuleiro, (L, C)):-        
    verificaColuna(Tabuleiro, C),         % Verifica a linha
    verificaLinha(Tabuleiro,L).           % Verifica a coluna


% FUNÇÃO PRINCIPAL
insereObjecto((L,C), Tabuleiro, Obj) :- 
    obtemObjecto((L, C), Tabuleiro, Pos),
    Pos = Obj,!.                       % Se a coordenada estiver vazia, unifica inserindo o objecto

insereObjecto((L,C), Tabuleiro, _) :-       % Caso a coordenada não esteja vazia, insereObjecto falha
    \+(verificaCoordenada(Tabuleiro, (L,C))), !; 
    nth1(L, Tabuleiro, Linha1), 
    nth1(C, Linha1, Pos), 
    \+(var(Pos)), !.



% insereVariosObjectos(ListaCoords, Tabuleiro, ListaObjs): Insere os objectos dados nas coordenadas dadas.
%   ListaCoords: Lista de coordenadas a serem modificadas.
%   Tabuleiro: Tabuleiro a ser modificado.
%   ListaObjs: Lista de objectos a serem inseridos.

% FUNÇÃO AUXILIAR para verificar se duas listas tem o mesmo comprimento
verificaComprimento(ListaCoords, ListaObjs) :-          
    length(ListaCoords, LenCoor), 
    length(ListaObjs, LenObjs), 
    LenCoor =:= LenObjs.

% FUNÇÃO PRINCIPAL
insereVariosObjectos([], _, []):- !.         % Caso base, listas vazias
insereVariosObjectos([H|T], Tabuleiro, [C|M]) :- 
    verificaComprimento([H|T], [C|M]),!,
    insereObjecto(H, Tabuleiro, C),       % Insere o objecto na coordenada através da função insereObjecto
    insereVariosObjectos(T, Tabuleiro, M).       % Recursão para o resto da lista



% inserePontosVolta(Tabuleiro, (L, C)): Insere os pontos à volta da coordenada dada no Tabuleiro.
%   Tabuleiro: Tabuleiro a ser modificado.
%   (L, C): Coordenada a ser modificada.

% FUNÇÃO AUXILIAR para inserir pontos nas coordenadas adjacentes
insereAdjacentes(Tabuleiro, (L, C)) :-                            
    Cima is L - 1, insereObjecto((Cima, C), Tabuleiro, p),
    Baixo is L + 1, insereObjecto((Baixo, C), Tabuleiro, p),
    Dir is C + 1, insereObjecto((L, Dir), Tabuleiro, p),       % Insere os pontos em todas as direções adjacentes
    Esq is C - 1, insereObjecto((L, Esq), Tabuleiro, p).      % (cima, baixo, esquerda e direita)

% FUNÇÃO AUXILIAR para inserir pontos nas diagonais    
insereDiagonais(Tabuleiro, (L, C)) :-                             
    Cima is L - 1, Esq is C - 1, insereObjecto((Cima, Esq), Tabuleiro, p), 
    Dir is C + 1, insereObjecto((Cima, Dir), Tabuleiro, p), 
    Baixo is L + 1, insereObjecto((Baixo, Esq), Tabuleiro, p),   % Insere os pontos nas direções restantes 
    insereObjecto((Baixo, Dir), Tabuleiro, p).     % (cima-esquerda, cima-direita, baixo-esquerda e baixo-direita)

% FUNÇÃO PRINCIPAL para inserir pontos à volta da coordenada dada, utilizando as funções auxiliares
inserePontosVolta(Tabuleiro, (L, C)) :-             
    insereAdjacentes(Tabuleiro, (L, C)),           
    insereDiagonais(Tabuleiro, (L, C)).



% inserePontos(Tabuleiro, ListaCoord): Insere pontos em todas as coordenadas dadas no Tabuleiro.
%   Tabuleiro: Tabuleiro a ser modificado.
%   ListaCoord: Lista de coordenadas a serem modificadas.

inserePontos(_, []):- !.              % Caso base, lista vazia
inserePontos(Tabuleiro, [H|T]) :-             
    insereObjecto(H, Tabuleiro, p),       % Utiliza função anterior para inserir o ponto
    inserePontos(Tabuleiro, T).           % Recursão para o resto da lista



% 5.3 - Consultas
% objectosEmCoordenadas(ListaCoords, Tabuleiro, ListaObjs): Obtem os objectos de todas as coordenadas dadas.
%   ListaCoords: Lista de coordenadas a serem consultadas.
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaObjs: Lista de objectos obtidos.

objectosEmCoordenadas([], _, []):- !.              % Caso base, listas vazias
objectosEmCoordenadas([(L,C)|T], Tabuleiro, [Pos|ListaObjs]) :- 
    obtemObjecto((L, C), Tabuleiro, Pos),     % Recursão que adiciona o objecto de cada coordenada à ListaObjs
    objectosEmCoordenadas(T, Tabuleiro, ListaObjs), !.
    
objectosEmCoordenadas([(L,C)|_], Tabuleiro, _) :-     % Caso a coordenada não seja válida, a função falha
    \+verificaCoordenada(Tabuleiro, (L,C)), !, fail.



% coordObjectos(Objecto, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos):
% Obtem todas as coordenadas que contém o objecto pedido, retornando também o número de ocorrências desse objecto no tabuleiro.
%   
%   Objecto: Objecto a ser consultado.
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaCoords: Lista de coordenadas a serem consultadas.
%   ListaCoordObjs: Lista de coordenadas devolvida que contém o objecto pedido.
%   NumObjectos: Número de ocorrências do objecto pedido.

% FUNÇÃO PRINCIPAL que utiliza as funções auxiliares seguintes tendo em conta o objecto pedido
coordObjectos(Objecto, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-    
    (var(Objecto) -> coordObjectosVariaveis(_, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos);   
    Objecto == e -> coordObjectosEstrelas(e, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos);     
    Objecto == p -> coordObjectosPontos(p, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos)).

% FUNÇÃO AUXILIAR para obter as coordenadas que contenham variáveis
coordObjectosVariaveis(_, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-   
    findall(Coordenada,                                                         
        (member(Coordenada, ListaCoords),       % Encontra todas as coordenadas que sejam membro da ListaCoords
        obtemObjecto(Coordenada, Tabuleiro, Pos),     % e que contenham variáveis
        var(Pos)),                                   
        ListaCoordObjs),
    length(ListaCoordObjs, NumObjectos).
    
% FUNÇÃO AUXILIAR para obter as coordenadas que contenham variáveis
coordObjectosEstrelas(e, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-  
    findall(Coordenada,                                                        
        (member(Coordenada, ListaCoords),       % Encontra todas as coordenadas que sejam membro da ListaCoords            
        obtemObjecto(Coordenada, Tabuleiro, Pos),      % e que contenham estrelas(e)    
        Pos == e),                                          
        ListaCoordObjs),
    length(ListaCoordObjs, NumObjectos).

% FUNÇÃO AUXILIAR para obter as coordenadas que contenham pontos
coordObjectosPontos(p, Tabuleiro, ListaCoords, ListaCoordObjs, NumObjectos) :-    
    findall(Coordenada,                                                                           
        (member(Coordenada, ListaCoords),       % Encontra todas as coordenadas que sejam membro da ListaCoords         
        obtemObjecto(Coordenada, Tabuleiro, Pos),      % e que contenham pontos(p)   
        Pos == p),                                          
        ListaCoordObjs),
    length(ListaCoordObjs, NumObjectos).



% coordenadasVars(Tabuleiro, ListaVariaveis): Obtem todas as coordenadas que contenham variáveis.
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaVariaaveis: Lista das coordenadas que contém variáveis devolvida.

% FUNÇÃO PRINCIPAL
coordenadasVars(Tabuleiro, ListaVariaveis) :-
    length(Tabuleiro, LenTabuleiro),
    coordLinhas(LenTabuleiro, CoordLinhas),     % Obtem todas as coordenadas do tabuleiro
    flatten(CoordLinhas, ListaCoords),         % e coloca todas numa lista só
    findall((L,C), (
        member((L,C), ListaCoords),
        nth1(L, Tabuleiro, Linha),    % Encontra todas as coordenadas que contenham variáveis
        nth1(C, Linha, Pos),
        var(Pos)
    ), ListaVariaveis).



% 5.4 Estratégias
% 5.4.1 Fechar linhas, colunas ou estruturas
% fechaListaCoordenadas(Tabuleiro, ListaCoord): Caso o nº de estrelas e variáveis seja o pretendido, 
% utiliza estratégias para fechar a lista fornecida.
%
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaCoord: Lista de coordenadas a serem fechadas.

% FUNÇÃO AUXILIAR que verifica se uma lista é sublista doutra
ehSubLista([], _, []):- !.                    % Caso base da função auxiliar, listas vazias
ehSubLista([H|T], Lista, [H|MembIguais]) :-     
    member(H, Lista),                        % Caso o elemento seja membro da lista, adiciona-o a MembIguais
    ehSubLista(T, Lista, MembIguais).
ehSubLista([H|T], Lista, MembIguais) :-             
    \+member(H, Lista),                     % Caso o elemento não seja membro da lista, continua a recursão
    ehSubLista(T, Lista, MembIguais).

% h1 - 1ª Estratégia: Fecha a lista dada com pontos
fechaListaCoordenadas_h1(Tabuleiro, ListaCoord) :-    % Utiliza funções anteriores para fechar a lista  
    coordenadasVars(Tabuleiro, ListaVars),             
    ehSubLista(ListaCoord, ListaVars, MembIguais), !,  % Obtem as coordenadas de todas as variáveis, 
    inserePontos(Tabuleiro, MembIguais).     % verifica se é sublista e insere pontos em todas elas

% h2 - 2ª Estratégia: Insere uma estrela e pontos à sua volta
fechaListaCoordenadas_h2(Tabuleiro, [H|_]) :-
    insereObjecto(H, Tabuleiro, e),                   % Insere uma estrela na primeira coordenada
    inserePontosVolta(Tabuleiro, H).                  % Insere pontos à volta da estrela

% h3 - 3ª Estratégia: Insere duas estrelas e pontos à sua volta
fechaListaCoordenadas_h3(Tabuleiro, [(L,C),(L1,C1)]) :-
    insereVariosObjectos([(L,C), (L1,C1)], Tabuleiro, [e,e]),   % Insere as duas estrelas
    inserePontosVolta(Tabuleiro, (L,C)),                        % Insere pontos à volta das estrelas
    inserePontosVolta(Tabuleiro, (L1,C1)).

% Verifica se algum dos casos é possível, caso não seja retorna o tabuleiro original
fechaListaCoordenadas(Tabuleiro, ListaCoord) :-
    coordObjectos(e, Tabuleiro, ListaCoord, _, NumEstrelas),
    coordObjectos(_, Tabuleiro, ListaCoord, ListaCoordsVars, NumVariaveis),
    ((NumEstrelas =:= 2)    % Caso o nº de estrelas seja 2, utiliza a 1ª estratégia
    -> fechaListaCoordenadas_h1(Tabuleiro, ListaCoord);     
    (NumEstrelas =:= 1, NumVariaveis =:= 1)     % Caso tenha 1 estrela e 1 variável, utiliza a 2ª estratégia
    -> fechaListaCoordenadas_h2(Tabuleiro, ListaCoordsVars);   
    (NumEstrelas =:= 0, NumVariaveis =:= 2)     % Caso não tenha estrelas e tenha 2 variáveis, utiliza a 3ª estratégia
    -> fechaListaCoordenadas_h3(Tabuleiro, ListaCoordsVars);    
    true).    % o true faz com que a função não falhe e retorne o tabuleiro inalterado



% fecha(Tabuleiro, ListaListasCoord): Aplica fechaListaCoordenadas para todas as listas de coordenadas dadas.
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaListasCoord: Lista de listas de coordenadas a serem fechadas.

fecha(_,[]) :- !.        % Caso base, lista vazia
fecha(Tabuleiro, [H|T]) :- 
    fechaListaCoordenadas(Tabuleiro, H),    % Aplica a função fechaListaCoordenadas para fechar cada lista
    fecha(Tabuleiro, T), !.                  



% 5.4.2 Encontrar padrões
% encontraSequencia(Tabuleiro, N, ListaCoords, Seq): Encontra uma sequência de N coordenadas com variáveis.
%   Tabuleiro: Tabuleiro a ser consultado.
%   N: Número de variáveis da sequência pretendido.
%   ListaCoords: Lista de coordenadas a serem verificadas.
%   Seq: Lista de coordenadas que formam a sequência encontrada.

% FUNÇÃO AUXILIAR iterativa para obter o nº máximo de elementos seguidos
obtemSequencia([], _, NovoMax, NovoMax) :- !.    % Caso base, lista vazia, retorna o nº máximo de elementos seguidos
obtemSequencia([H|T], Tabuleiro, Acc, MaxSeq) :-   
    objectosEmCoordenadas([H], Tabuleiro, [Var]),       
    var(Var),                               
    NovoAcc is Acc + 1,             % Caso o objecto seja uma variável incrementa a contagem
    obtemSequencia(T, Tabuleiro, NovoAcc, MaxSeq). 
obtemSequencia([_|T], Tabuleiro, Acc, MaxSeq) :-
    NovoMax is max(Acc, MaxSeq),       % Acabou a sequência, verifica qual o nº maior de elementos seguidos
    obtemSequencia(T, Tabuleiro, 0, NovoMax).    % Atualiza o nº de elementos seguidos máximo, recomeça a recursão e reinicia a contagem


% FUNÇÃO AUXILIAR que cerifica se a sequência encontrada tem o nº pedido de elementos seguidos
sequencia(ListaCoords, Tabuleiro, N, Resultado) :-      
    sort(ListaCoords, ListaCoordsOrd),                     
    obtemSequencia(ListaCoordsOrd, Tabuleiro, 0, NumElemSeguidos),
    N =:= NumElemSeguidos, !,
    Resultado = ListaCoords.        % Retorna a sequência encontrada(Resultado)

% FUNÇÃO PRINCIPAL que utiliza as funções auxiliares
encontraSequencia(Tabuleiro, N, ListaCoords, Seq) :-        
    coordObjectos(_, Tabuleiro, ListaCoords, ListaCoordVars, NumVars),
    N =:= NumVars,    % Verifica se o nº de variáveis(N) é igual ao nº de variáveis da lista de coordenadas(NumVars)
    coordObjectos(e, Tabuleiro, ListaCoords, _, NumEstrelas),
    NumEstrelas =:= 0,     % Verifica que o nº de estrelas é 0   
    sequencia(ListaCoordVars, Tabuleiro, N, Seq).    % Caso a sequência seja encontrada, retorna essa sequência (Seq)



% aplicaPadraoI(Tabuleiro, [(L1, C1), (L2, C2), (L3, C3)]): Aplica o padrão I às coordenadas dadas.
%   Tabuleiro: Tabuleiro a ser consultado.
%   [(L1, C1), (L2, C2), (L3, C3)]: Lista de coordenadas a serem modificadas.

% Padrão I: Coloca 1 estrela na 1ª coordenada e outra na 3ª caso a lista seja uma sequência de 3 variáveis.
aplicaPadraoI(Tabuleiro, [(L1, C1), (L2, C2), (L3, C3)]) :-     
    encontraSequencia(Tabuleiro, 3, [(L1, C1), (L2, C2), (L3, C3)], _),   % Verifica se é sequência de 3 variáveis
    insereVariosObjectos([(L1, C1), (L3, C3)], Tabuleiro, [e, e]),
    inserePontosVolta(Tabuleiro, (L1, C1)),       % Insere as estrelas, e pontos à sua volta
    inserePontosVolta(Tabuleiro, (L3, C3)), !.



% aplicaPadroes(Tabuleiro, ListaListaCoords): Aplica os padrões I e T aos conjuntos de coordenadas dadas.
%   Tabuleiro: Tabuleiro a ser consultado.
%   ListaListasCoord: Lista de listas de coordenadas a serem fechadas.

aplicaPadroes(_, []) :- !.      % Caso base, lista vazia
aplicaPadroes(Tabuleiro, [H|T]) :- 
    length(H, N),
    ((N =:= 3 -> aplicaPadraoI(Tabuleiro, H));          % Caso o nº de coordenadas seja 3, aplica o padrão I
    (N =:= 4 -> aplicaPadraoT(Tabuleiro, H))),      % Caso o nº de coordenadas seja 4, aplica o padrão T
    aplicaPadroes(Tabuleiro, T), !.              % Depois de aplicar um dos padrões, continua a recursão
aplicaPadroes(Tabuleiro, [_|T]) :-          
    aplicaPadroes(Tabuleiro, T), !.   % Caso nenhum padrão seja aplicado, continua a recursão



% resolve(Estruturas, Tabuleiro): Resolve o tabuleiro com as estratégias desenvolvidas.
%   Estruturas: Lista de estruturas a serem aplicadas(Regiões).
%   Tabuleiro: Tabuleiro a ser consultado.

% FUNÇÃO AUXILIAR que compara elementos
comparaElementos(A, B) :- var(A), var(B).   % Caso ambos sejam variáveis(v), são iguais,   
comparaElementos(A, B) :- A == B.     % caso contrário, compara as constantes(e ou p)

% FUNÇÃO AUXILIAR que compara linhas
comparaLinhas([], []).             % Caso base, linhas vazias
comparaLinhas([H1| T1], [H2|T2]) :-
    comparaElementos(H1, H2),      % Compara cada elemento da linha
    comparaLinhas(T1, T2).          

% FUNÇÃO AUXILIAR que compara tabuleiros
comparaTabuleiro([], []).         % Caso base, tabuleiros vazios
comparaTabuleiro([H1| T1], [H2|T2]) :-
    comparaLinhas(H1, H2),        % Compara cada linha
    comparaTabuleiro(T1, T2).

% FUNÇÃO AUXILIAR que aplica as estratégias aplicaPadroes e fecha
aplicaEstrategias(Tabuleiro, CoordsRegiao):-
    aplicaPadroes(Tabuleiro, CoordsRegiao),
    fecha(Tabuleiro, CoordsRegiao).

% FUNÇÃO AUXILIAR que verifica se o tabuleiro está completo
tabuleiroCompleto(Tabuleiro, CoordsRegioes):-
    copy_term(Tabuleiro, NovoTabuleiro),        % Copia o tabuleiro (função built-in)
    aplicaEstrategias(NovoTabuleiro, CoordsRegioes),    % Aplica as estratégias ao tabuleiro copiado
    comparaTabuleiro(Tabuleiro, NovoTabuleiro).    % Compara o tabuleiro original com o copiado após as estratégias

% FUNÇÃO PRINCIPAL que aplica as estratégias ao tabuleiro
resolve(Estruturas, Tabuleiro):-
    coordTodas(Estruturas, CoordsRegioes),      % Obtem as coordenadas de todas as regioes
    aplicaEstrategias(Tabuleiro, CoordsRegioes),    % Aplica as estratégias
    ((\+tabuleiroCompleto(Tabuleiro, CoordsRegioes)   % Caso o tabuleiro ainda não esteja completo, 
    -> resolve(CoordsRegioes, Tabuleiro));           % continuar a recursão
    true).    % Caso já esteja completo, retorna o tabuleiro