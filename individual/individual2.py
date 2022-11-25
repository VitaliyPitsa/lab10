#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    file_name = input("Введите имя файла: ")
    os.rename("ind2.txt", file_name)
    f = open(file_name, 'r')  # cчитываю файл
    line = f.readline().lower()
    while line:
        line = line.split()
        s = {}
        i1 = 0
        i2 = ''
        q = 0
        t = []
        min1 = 0
        for i in line:  # ввожу слова в словарь
            if i not in s:  # проверяю есть ли слово в словаре,если есть,то добавляю1
                s[i] = 1
            else:
                s[i] += 1
        for values in s.values():  # нахожу максимальное повторение
            if values > i1:
                i1 = values
        for keys, values in s.items():
            if values == i1:
                min1 = keys
        print(min1)
        line = f.readline().lower()
    f.close()
