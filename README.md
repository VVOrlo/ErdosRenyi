## Описание

Данный код генерирует граф в модели Эрдёша-Реньи с заданными характеристиками и вычисляет среднюю степень вершины, сравнивая её со значением, полученным по формуле из материала лекций.

1. Задаются значения `num_nodes` - количество вершин и `prob` - вероятность появления случайного ребра в графе.

2. Граф создается с помощью функции `nx.erdos_renyi_graph(num_nodes, prob)`.

3. Вычисляется суммарная степень всех вершин графа.

4. Вычисляется средняя степень вершины путем деления суммарной степени на количество вершин.

5. Вычисляется ожидаемая средняя степень вершины по формуле модели Эрдёша-Реньи: `expected_degree = prob * (num_nodes - 1)`.

6. Выводятся на экран средняя степень вершины в графе и ожидаемая средняя степень вершины по формуле.

## Результат работы программы

**Исходные данные:**
- n = 9
- p = 0.75

**Результат:**
- Средняя степень вершины в графе: 4.888888888888889
- Ожидаемая средняя степень вершины по формуле: 6.0
