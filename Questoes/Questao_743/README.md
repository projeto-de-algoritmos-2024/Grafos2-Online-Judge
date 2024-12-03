## 743. Network Delay Time

### Enunciado:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

![ExemploVisal](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/main/Questoes/Questao_743/assets/teste1.png "ExemploVisual")

### Exemplo 1
>**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
>**Output:** 2

### Exemplo 2
>**Input:** times = [[1,2,1]], n = 2, k = 1
>**Output:** 1

### Exemplo 3
>**Input:** times = [[1,2,1]], n = 2, k = 2
>**Output:** -1

Entradas e saídas obtidas:

Codigo de teste:
<br>

![TestesRodados](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/main/Questoes/Questao_743/assets/CodigoTeste.png "TestesRodados")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/main/Questoes/Questao_743/assets/OutputTeste.png "SaidasObtidas")

Foi utilizado um algoritmo de Dijkstra modificado para realizar a busca o menor caminho em um grafo com peso em suas arestas, e em seus vértices. O desafio deste problema consiste em entender como modificar o algoritmo de Dijkstra original para encontrar o menor custo de soma dos vértices mantendo-se dentro de um limite estabelecido de soma dos pesos das arestas.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/main/Questoes/Questao_743/assets/Aceito.png "Exercicio Submetido")


