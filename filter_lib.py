#!/usr/bin/env python
import numpy as np
import scene_generation as scene



def getRow(im):
  nonZero = 0
  colAcc = 0
  rowAcc = 0 
  for row, imRow in enumerate(im):
    for col, pixel in enumerate(imRow):
      print ("{} {} {}".format(row, col, pixel))
      if pixel > 0:
        colAcc = colAcc + col * pixel
        rowAcc = rowAcc + row * pixel
        nonZero = nonZero + pixel

  return [colAcc/ nonZero, rowAcc/ nonZero]

def thresh(im, cutOff):
  im[im<cutOff] = 0
  return im



def testFunction():
  im = scene.generateDummyScene()
  im = thresh(im,2)
  
  print(im)
  print(getRow(im))
  
if __name__ == '__main__':
  testFunction()



