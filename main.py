import networkx as nx

# Заданные значения количества вершин и вероятности появления ребра
num_nodes = 9
prob = 0.75

# Генерация графа с помощью кода из лекции
G = nx.erdos_renyi_graph(num_nodes, prob)

# Вычисление средней степени вершины
total_degree = 0
for node in G.nodes():
    total_degree += G.degree(node)
average_degree = float(total_degree) / len(G.nodes())

# Ожидаемая средняя степень вершины по формуле модели Эрдёша-Реньи
expected_degree = prob * (num_nodes - 1)

# Вывод результатов
print("Средняя степень вершины в графе:", average_degree)
print("Ожидаемая средняя степень вершины по формуле:", expected_degree)