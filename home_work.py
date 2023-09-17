# Сдаем через Гитхаб в любом ЯП, но обязательно должна быть документация к классам и методам.
# Доработать бинарное дерево с семинара, добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.
# Задача по желанию . Реализовать основной функционал КЧД.

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:
    """Конструктор создания дерева, где root_value значение ноды root"""
    def __init__(self, root_value):
        self.root = Node(root_value)
        """size - количество элементов в дереве"""
        self.size = 1

    def add(self, value):
        """Добавление нового элемента
        ищем ноду по значению value, если такой ноды нет то добывляем новую ноду со значением value
        к родителю (res[1]) и увеличиваем значение size на 1"""
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
                self.size += 1
            else:
                res[1].left = new_node
                self.size += 1
        else:
            print("Хорош")


    def search(self, node, value, parent=None):
        """Поиск ноды по значению от ноды (node), где parent - это родитель ноды (node)
        если нода со значением value найдена или следующей ноды нет, то возвращаем ноду и ее родителя"""
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
        

    def __listValue(self, node, listValue):
        """метод служит для записи значений (value) от текущей ноды (node) в список (listValue)
        через обход дерева в глубину рекурсивно"""
        if node.left != None:
            """пока слудующая нода существует то добавляем ее значение в список и
            рекурсивно вызываем метод __listValue для следующей ноды"""
            listValue.append(node.left.value)
            self.__listValue(node.left, listValue)
        if node.right != None:
            listValue.append(node.right.value)
            self.__listValue(node.right, listValue)


    def delValue(self, value):
        """Удаление элемента.
        Ищем ноду по значению если она существует или выводим сообщение что такого значения нет"""
        res = self.search(self.root, value)
        if res[0] != None:    
            """добавляем все элементы дерева от найденной ноды в список и отнимаем значение размера
            списка от текущего размера (size)"""
            if res[0].value == value:
                listValue = []
                self.__listValue(res[0], listValue)
                self.size -= len(listValue) + 1
                """если найденный элемент является нодой (root), то сортируем список, создаем
                новое дерево и в качестве значения ноды (root) берем средний элемент списка (listValue)"""
                if value == self.root.value:
                    listValue.sort()
                    self.__init__(listValue[len(listValue) // 2])
                    """дабавляем элементы в дерево из списка, исключая средний элемент"""
                    for i in range(len(listValue)):
                        if i != len(listValue) // 2:
                            self.add(listValue[i])         
                else:
                    """есле значение элемента больше значения родителя (res[1]), то удаляем правую
                    ветку от родителя, если меньше то удаляем левую ветку"""
                    if value > res[1].value:
                        res[1].right = None
                    if value < res[1].value:
                        res[1].left = None
                    """добавляем элементы из списка (listValue) в дерево"""
                    for i in listValue:
                        self.add(i)
        else:
            print('такого значения нет')
        

    def printTree(self):
        """добавляем все элементы дерева в список, сортируем и выводим на консоль"""
        listValue = []
        self.__listValue(self.root, listValue)
        listValue.append(self.root.value)
        listValue.sort()
        for i in listValue:
            print(i)


bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)

print(bt.root)
print(bt.root.left)
print(bt.root.right)

# подсчет количества элементов
print('количество элементов', bt.size)
# вывод всего дерева на экран
bt.printTree()
# удаление элемента
bt.delValue(5)
bt.delValue(4)
print('после удаления количество элементов', bt.size)
bt.printTree()
print(bt.root)