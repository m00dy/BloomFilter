#!/usr/bin/python
import random
from hash_function import HashFunction

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


