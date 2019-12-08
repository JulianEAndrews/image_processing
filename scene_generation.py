#!/usr/bin/env python
import numpy as np



def generateDummyScene(numRows = 5, numCols = 5):

  #dummyScene = np.zeros((5,5), dtype = 'int16')
  #use floats for now...
  dummyScene = np.ones((5,5))
  
  #row , col
  dummyScene[2,2]   = 4
  dummyScene[1,1:4] = 2
  dummyScene[3,2] = 2
  return dummyScene

  #  01234
  #  _____
  #0|
  #1| 222
  #2|  4
  #3|  2


if __name__ == '__main__':
  print(generateDummyScene())



