#!/usr/bin/python

import time
import random
from BloomFilter import BloomFilter


class Experiment():
  def __init__(self,B,N,M,K):
    self.b = B
    self.m = M
    self.k = K
    self.n = N
    self.timeStart = 0
    self.timeFinish = 0
    self.falsePositiveCounter = 0
    self.f = 1

  def percentage(self,part, whole):
    return 100 * float(part)/float(whole)

  def make_experiment(self):
    self.timeStart = time.time()
    
    for i in range(0,self.b):
      #Build the bloomFilter
      bf = BloomFilter(self.m,self.k)

      #Insert N times odd items to the bloomFilter
      for i in range(0,self.n):
        rnumber = random.randint(0,self.n)
        rnumber = rnumber*2 + 1
        bf.insert(str(rnumber))
    
    #Check N times even items from the bloomFilter
      for i in range(0,self.n):
        rnumber = random.randint(0,self.n)
        rnumber = rnumber*2
        result = bf.check(str(rnumber))

        if(result is True):
          self.falsePositiveCounter = self.falsePositiveCounter + 1

    self.falsePositiveCounter = self.falsePositiveCounter / self.b
    self.timeFinish = time.time()

    #return [(self.timeFinish-self.timeStart),self.percentage(self.falsePositiveCounter,self.n)]
    return self.percentage(self.falsePositiveCounter,self.n)

### Number of Hash Functions Test ###


l=[]
for i in range(2000,22000,1000):
  exp1 = Experiment(150,2000,i,6)
  l.append(exp1.make_experiment())




"""
PLOT API
"""

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Scatter(
    x=l,
    y=range(2000,22000,1000),
    name="Graph1"
)

data = Data([trace1])

layout = Layout(
    title='Constant number of HashFunctions',
    xaxis=XAxis(
        title='False Positive Probability',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Number of Vector Size',
        showline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='line-style')


"""
http://corte.si/%2Fposts/code/bloom-filter-rules-of-thumb/index.html
"""
