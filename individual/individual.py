#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()
        k = 0
        m = 0
        for i in text:
            if i.isalpha():
                m += 1
            else:
                if m > 7:
                    k += 1
                m = 0
    print(k)
