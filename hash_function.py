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


