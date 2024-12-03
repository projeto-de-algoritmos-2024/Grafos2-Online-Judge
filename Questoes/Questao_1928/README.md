## 1928. Minimum Cost to Reach Destination in Time

### Enunciado:
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.


![ExemploVisal](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/master/Questoes/Questao_1928/assets/teste1.png "ExemploVisual")

### Exemplo 1
>**Input:** maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
>**Output:** 11

![ExemploVisal](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/master/Questoes/Questao_1928/assets/teste1.png "ExemploVisual")

### Exemplo 2
>**Input:** maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
>**Output:** 48

Entradas e saídas obtidas:

Codigo de teste:
<br>

![TestesRodados](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/master/Questoes/Questao_1928/assets/CodigoTeste.png "TestesRodados")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/master/Questoes/Questao_1928/assets/OutputTeste.png "SaidasObtidas")

Foi utilizado um algoritmo de Dijkstra modificado para realizar a busca o menor caminho em um grafo com peso em suas arestas, e em seus vértices. O desafio deste problema consiste em entender como modificar o algoritmo de Dijkstra original para encontrar o menor custo de soma dos vértices mantendo-se dentro de um limite estabelecido de soma dos pesos das arestas.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/Grafos2-Online-Judge/blob/master/Questoes/Questao_1928/assets/Aceito.png "Exercicio Submetido")

