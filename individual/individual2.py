#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    file_name = input("Введите имя файла: ")
    os.rename("ind2.txt", file_name)
    f = open(file_name, 'r')
    line = f.readline().lower()
    while line:
        line = line.split()
        s = {}
        i1 = 0
        min1 = 0
        for i in line:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        for values in s.values():
            if values > i1:
                i1 = values
        for keys, values in s.items():
            if values == i1:
                min1 = keys
        print(min1)
        line = f.readline().lower()
    f.close()
