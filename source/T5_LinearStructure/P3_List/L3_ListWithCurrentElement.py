#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source.T5_LinearStructure.P3_List.L1_Node import Node
from source.T5_LinearStructure.P3_List.L4_ListIterator import ListIterator


class ListWithCurrent:

    def __init__(self):
        """ Конструктор - створює новий порожній список.
        """
        self.mHead = None  # Перший вузол списку
        self.mPrev = None  # Вузол, що передує поточному елементу списку
        self.mCurr = None  # Поточний вузол списку

    def empty(self):
        """ Перевіряє чи список порожній

        :return: True, якщо список не містить жодного елемента
        """
        return self.mHead is None

    def reset(self):
        """ Зробити поточний елемент першим."""
        self.mCurr = self.mHead
        self.mPrev = None

    def next(self):
        """ Перейти до наступного елемента.

        Породжує виключення StopIteration, якщо наступний елемент порожній
        :return: None
        """
        if self.mCurr is not None:
            self.mPrev = self.mCurr
            self.mCurr = self.mCurr.mNext
        else:
            raise StopIteration

    def current(self):
        """ Отримати поточний елемент

        :return: Навантаження поточного елементу
        """
        if self.mCurr is not None:
            return self.mCurr.mItem
        else:
            return None

    def insert(self, item):
        """ Вставити новий елемент у список перед поточним

        :param item: елемент, що вставляється у спиоск
        :return: None
        """
        node = Node(item)
        node.mNext = self.mCurr

        if self.mCurr == self.mHead:
            self.mHead = node

        if self.mPrev is not None:
            self.mPrev.mNext = node

        self.mPrev = node

    def remove(self):
        """ Видалити поточний елемент у списку

        Видалення переставляє вказівник на поточний елемент на наступний
        """
        pass  # TODO: Implement by yourself

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        """ Спеціальний метод, що повертає ітератор для колекції
        :return: Ітератор колекції
        """
        return ListIterator(self)



l = ListWithCurrent()
l.insert(11)
l.insert(12)
l.insert(13)
l.insert(14)
l.insert(15)
l.insert(16)

# l.reset()
# l.next()
# print(l)

# it = iter(l)
# while True:
#     try:
#         print(next(l))
#     except StopIteration:
#         break


# l.reset()
# print(l)
# l.next()
# l.next()
# l.next()
# print(l)
# l.next()
#
#
# l.insert(555)
# #
for el in l:
    print(el)

