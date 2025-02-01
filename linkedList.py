class Node:
    """Класс узлов списка(коробка, где сидит котик)
    #объект - элемент
    #атрибуты - есть следующий, есть предыдущий
    #метод - только инициализация
    """
    def __init__(self, data):
        """Инициализация узла
        Args: data - данные, которые содержатся в узле"""
        self.data = data #типа мои данные - это данные, которые пришли
        self.next = None #сначала никуда не указываем
        self.prev = None #собственно по той же причине


class OneLinkedList:
    """Собственно, класс самого односвязного списка
    #объект - односвязный список
    #атрибут - голова
    #методы
    """
    def __init__(self):
        """Инициализируем пустой список"""
        self.head = None
    
    def is_empty(self):
        """Проверяем список на пустоту
        Args: объект(список)
        Returns: True, если список пуст. False, если список не пуст
        """
        if self.head == None:
            return True
        else:
            return False
        
    def append(self, data):
        """Добавляем узел в начало списка
        Apgs: объект(список), данные(которые надо добавить)
        """
        new_node = Node(data)# новый узел - это у нас объект, который является объектом узла с данными

        if self.is_empty():
            self.head = new_node#то головой списка становится новый узел
            return
        #дальше начинаем с головы:
        last_node = self.head
        while last_node.next:# типа пока у нас идет следующий элемент не None
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        """Добавляем новый узел в начало списка
        Apgs: объект(список), данные(которые надо добавить)
        """
        new_node = Node(data)
        new_node.next = self.head#говорим, что теперь наш узел должен указывать на нашу голову
        self.head = new_node#теперь говорим, что наша новая голова - этот узел
    
    def insert_after_value(self,value, prev_value):
        """Вставляет новое значение после конкретного
        Args: объект, элемент который нужно вставить, элемент после которого нужно вставить
        """
        prev_node =  self.search_value(prev_value)
        if prev_node:
            new_node = Node(value)
            new_node.next = prev_node.next 
            prev_node.next = new_node
        else:
            print(f'Узел со значением {prev_value} в списке не найден')
    
    def print(self):
        """Выводим данные списка
        Args: список(объект)
        """
        i = self.head#начнем сначала
        while i:
            print(f'{i.data}')
            i = i.next
        print('None')# то, что выводим в конце списка
    
    def size(self):
        """Возвращает размер списка
        Args: объект
        Returns: размер
        """
        count = 0
        i = self.head# начало списка
        if self.is_empty():
            return count
        while i:
            count+=1
            i = i.next
        return count
    
    def search_value(self, data):
        """Есть ли этот элемент в списке?
        Args: объект, элемент
        Returns: False, True
        """
        i = self.head
        while i:
            if i.data == data:
                return i
            i = i.next
        return None
    def delete(self, value):
        """Удаляет в списке переданной значение
        Args: объект(список), значение, которое нужно удалить
        """
        if self.head.data == value:
            self.head = self.head.next
            return
        
        i = self.head
        while i.next:
            if i.next.data == value:
                i.next = i.next.next
                return
            i = i.next

class TwoLinkedList:
    def __init__(self):
        """Инициализируем голову и хвост"""
        self.head = None
        self.tail = None

    def is_empty(self):
        """Проверяем список на пустоту
        Args: объект(список)
        Returns: True, если список пуст. False, если список не пуст
        """
        if self.head == None:
            return True
        else:
            return False
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def search_index(self, index):
        node_index = 0
        value = self.head
        while node_index <= index:
            if node_index == index:
                return value.data
            node_index+=1
            value = value.next
        
    
    def print(self):
        i = self.head
        while i:
            print(f'{i.data}')
            i = i.next
        print('None')


twolinkedlist = TwoLinkedList()
twolinkedlist.append(1)
twolinkedlist.append(2)
twolinkedlist.append(3)
twolinkedlist.print()
print(f'{twolinkedlist.search_index(1)}')

# onelinkedkiist = OneLinkedList()

# onelinkedkiist.append(1)
# onelinkedkiist.append(2)
# ins_value = onelinkedkiist.insert_after_value(4,1)
# empty = onelinkedkiist.is_empty()
# onelinkedkiist.prepend(3)
# dele = onelinkedkiist.delete(3)
# print (f'Список пуст? {empty}')
# onelinkedkiist.print()
# size = onelinkedkiist.size()
# print(f'Размер списка равен {size}')
# print(onelinkedkiist.search_value(4))


