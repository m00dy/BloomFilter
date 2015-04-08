#!/usr/bin/python

import random

class HashFunction():

  def __init__(self,M):
    self.m = M
    self.a = random.randint(0,self.m)
    self.b = random.randint(0,self.m)

  def base_hash_function(self,key):
    hash=0
    key = str(key)
    for i in range(0,len(key)):
      hash+=(ord(key[i]))
      hash+=(hash << 10)
      hash = hash  ^ ( hash >> 6)
    
    hash+=(hash << 3)
    hash = hash ^ (hash >> 11)
    hash+=(hash << 15)
    return hash
  
  def convert(self,y):
    return (self.a * self.base_hash_function(y) + self.b) % self.m


class BloomFilter():
  def __init__(self,M,K):
    self.m = M
    self.k = K
    self.bitVector = [False] * M
    self.hashFunctions = []
    for i in range(0,self.k):
      obj = HashFunction(M)
      self.hashFunctions.append(obj)

  def insert(self,obj):
    for f in self.hashFunctions:
      hash = f.convert(obj)
      index = int(hash)
      #print "Hash is " + str(hash) + " Index is " + str(index)
      self.bitVector[index] =  True
  
  def check(self,obj):
    ret = True
    for f in self.hashFunctions:
      index = int(f.convert(obj))
      ret = ret & self.bitVector[index]
    return ret



bf = BloomFilter(20000,3)
##2000 inserions
for i in range(0,20000):
  rnumber = random.randint(0,2000) % 2000
  rnumber = rnumber*2 + 1
  bf.insert(rnumber)

counter = 0
for i in range(0,20000):
  rnumber = random.randint(0,2000) % 2000
  rnumber = rnumber*2
  result = bf.check(rnumber)

  if(result is True):
    counter = counter+1

print counter
