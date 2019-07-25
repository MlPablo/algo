from source.T7_Graphs.P3_Weighted.L1_VertexForAlgorithms import INF
from source.T6_Trees.P2_BinaryTree.L7_PriorityQueue import PriorityQueue
from source.utils.benchmark import benchmark

# Алготитм А* подібний до алгоритму Дейкстри.
# У ньому також для визначення порядку обходу вершин використовується черга з пріоритетом.
# Проте для визначення пріоритет визначається не відстанню від стартової вершини,
# а використовує допоміжну функцію (евристику), аби скеровувати напрям пошуку.

# Таким чином, пріорітет буде визначатися за допомогою функції
#                 f(x) = g(x) + h(x)
# де g(x) - функція, значення якої дорівнюють вартості шляху від початкової вершини до x, (як у алгоритмі Дейкстри)
#    h(x) - евристична функція, яка оцінює вартість шляху від вершини x до кінцевої.



@benchmark
def AStar(graph, start, end):
    """ Функція, що реалізує пошук шляху у графі між двома вершинами використовуючи A* алгоритм

    :param graph: Граф
    :param start: Стартова вершина
    :param end: Кінцева вершина
    :return: Кортеж, що містить список вершин - найкоротший шлях, що сполучає вершини start та end та його вагу
    """

    # Ініціалізуємо додаткову інформацію у графі для роботи алгоритму.
    for vertex in graph:
        vertex.setDistance(INF)  # Відстань для кожної вершини від стартової ставиться як нескінченність
        vertex.setSource(None)   # Вершина з якої прийшли по найкорошому шляху невизначена
        vertex.calculateHeuristic(graph[end])  # Обчислюємо значення еврестичної функції, для кожної вершини

    # Відстань від першої вершини до неї ж визначається як 0
    graph[start].setDistance(0)

    pq = PriorityQueue()       # Створюємо пріоритетну чергу
    pq.insert(start, 0)        # Додаємо у чергу початкову вершину з нульовим пріоритетом

    # Введемо масив, що буде містити ознаку чи відвідали вже вершину.
    # Ініціалізуємо масив значеннями False (не відвідали)
    visited = [False] * len(graph)

    while not pq.empty():                  # Поки черга не порожня
        vertex_key = pq.extractMinimum()  # Беремо індекс вершини з черги з найнижчим пріоритетом
        visited[vertex_key] = True         # та позначаємо її як відвідану
        vertex = graph[vertex_key]         # Беремо поточну вершину за індексом

        if vertex_key == end:              # Якщо поточний елемент є шуканим
            break                          # пошук завершено

        for neighbor_key in vertex.neighbors():      # Для всіх сусідів (за ключами) поточної вершини
            if not visited[neighbor_key]:            # які ще не були відвідані
                neighbour = graph[neighbor_key]      # Беремо вершину-сусіда за ключем

                # Обчислюємо потенційну відстань у вершині-сусіді
                newDist = vertex.distance() + vertex.weight(neighbor_key)   # newDist = g(x) згідно з алгоритмом

                if newDist < neighbour.distance():    # Якщо потенційна відстань у вершині-сусіді менша за її поточне значення
                    neighbour.setDistance(newDist)   # Змінюємо поточне значення відстані у вершині-сусіді обчисленим
                    neighbour.setSource(vertex_key)  # Встановлюємо для сусідньої вершини ідентифікатор звідки ми прийшли у неї

                    h = neighbour.heuristic()         # Беремо значення евристичної функції у вершині-сусіді.
                    f = newDist + h                   # f(x) = g(x) + h(x) - обчилюємо новий пріорітет для вершини-сусіда.

                    if neighbor_key in pq:                    # Якщо вершина сусід міститься у черзі
                        pq.decreasePriority(neighbor_key, f)  # перераховуємо її пріоритет в черзі
                    else:
                        pq.insert(neighbor_key, f)            # або додаємо елемент до черги, якщо його там ще немає.

    return graph.constructWay(start, end)


