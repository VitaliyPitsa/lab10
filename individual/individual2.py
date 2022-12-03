#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == '__main__':
    file_name = input("Введите имя файла: ")
    os.rename("ind2.txt", file_name)
    with open(file_name, 'r') as f:
        line = f.readline().lower()
        if line:
            line = line.split()
            s = {}
            i1 = 0
            max = 0
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
                     max = keys
            print(max)
