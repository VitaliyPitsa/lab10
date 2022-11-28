#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f = open('text.txt', 'r')
    line = f.readline()
    if line:
        k = 0
        m = 0
        for i in line:
            if i.isalpha():
                m += 1
            else:
                if m > 7:
                    k += 1
                m = 0
        print(k)
    f.close()
