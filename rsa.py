#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:21:23 2020
Based off of: https://brilliant.org/wiki/rsa-encryption/
@author: liamhough
"""

#import check
import random

arr1 = []
arr2 = []
relPrime = 65537


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def prime(pos1, pos2):

    print("Prime numbers between", pos1, "and", pos2, "are:")
    arr = []

    for num in range(pos1, pos2 + 1):
   # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
              if (num % i) == 0:
                  break
           else:
               arr.append(num)
    return arr

def euler(p, q):
    return (p-1)*(q-1)

def str2ascii(s):
    asciiChars = []
    for c in s:
        asciiChars.append(ord(c))
    print(asciiChars)
    return asciiChars

def numConcat(num1, num2): 
  
     # find number of digits in num2 
     digits = len(str(num2)) 
  
     # add zeroes to the end of num1 
     num1 = num1 * (10**digits) 
  
     # add num2 to num1 
     num1 += num2 
  
     return num1 

def rsa():
    global private, n
    rand1low = random.randint(100, 499) #random lower number
    rand1high = random.randint(500, 999) #random uppper number
    rand2low = random.randint(100, 499) #random lower number
    rand2high = random.randint(500, 999) #random upper number
    arr1 = prime(rand1low, rand1high) #find all prime numbers in that range 1
    arr2 = prime(rand2low, rand2high) #find all prime numbers in that range 2
    print(arr1)
    print(arr2)
    p = random.choice(arr1) #choose random number from that
    q = random.choice(arr2)
    print(p)
    print(q)
    n = p*q #n is a 
    print(n)
    private = modinv(relPrime, euler(p, q))
    print("private", private)
    print("public", n, relPrime)
    
    return private, n

def encrpyt(n, message):
    rsa()
    print("private", private, "n", n)
    m = str2ascii(message)
    base = m[0]
    for i in range(1, len(m)):
        base = numConcat(base, m[i])
    print ("base", base)
    #a will be m^e
    a = base**relPrime
    c = a % n #this is the ciphertext
    print("c", c)





encrpyt(n, "monkey")


#check.expect("ex 1", swap_two("banana", 2, 5), "baaaaann")
  
