import networkx as nx

# Заданные значения количества вершин и вероятности появления ребра
num_nodes = 5
prob = 1.0

# Генерация графа с помощью кода из лекции
G = nx.erdos_renyi_graph(num_nodes, prob)

# Вычисление средней степени вершины
total_degree = sum(dict(G.degree()).values())
average_degree = total_degree / num_nodes

# Ожидаемая средняя степень вершины по формуле модели Эрдёша-Реньи
expected_degree = prob * (num_nodes - 1)

# Вывод результатов
print("Средняя степень вершины в графе:", average_degree)
print("Ожидаемая средняя степень вершины по формуле:", expected_degree)