#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

if __name__ == "__main__":
    with open("newfile.txt", "w") as data:
        data.write(os.environ["USERNAME"])
    check = os.path.exists("myName.txt")
    if not check:
        os.rename("newfile.txt", "myName.txt")
    else:
        print("Файл уже существует")
