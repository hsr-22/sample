# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:38:44 2022

@author: Harsh Roniyar
"""

num = int(input("Enter a number: "))
absnum = abs(num)
rev = absnum % 10
absnum = absnum // 10
while (absnum > 0):
    r = absnum % 10
    absnum = absnum // 10
    rev = rev*10 + r
if (num < 0):
    rev = rev - 2*rev
if (num == rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
