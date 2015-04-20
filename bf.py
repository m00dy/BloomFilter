#!/usr/bin/python

import random
from jhash import jhash_short

class HashFunction():

  def __init__(self,M):
    self.m = M
    self.a = random.randint(0,self.m)
    self.b = random.randint(0,self.m)

  def base_hash_function(self,key):
    return jhash_short(key)
  
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

"""
class Experiment():
  def __init__(self,B,M,K):
    self.b = B
    self.m = M
    self.k = K

  def make_experiment(self):
    bf = BloomFilter(self.m,self.k)
    for i in range(0,self.m):
"""

B = 150
all = 0
for i in range(0,B):

  bf = BloomFilter(20000,13)
  ##2000 inserions
  for i in range(0,20000):
    rnumber = random.randint(0,2000) % 2000 + 2000
    rnumber = rnumber*2 + 1
    bf.insert(str(rnumber))

  counter = 0
  for i in range(0,20000):
    rnumber = random.randint(0,2000) % 2000 + 2000
    rnumber = rnumber*2
    result = bf.check(str(rnumber))

    if(result is True):
      counter = counter+1

  all+=counter

print all/B


"""
http://corte.si/%2Fposts/code/bloom-filter-rules-of-thumb/index.html
"""
