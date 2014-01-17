#!/usr/bin/env python
import sys
import operator
import string
from collections import defaultdict

POSSIBLE_CHARACTERS = [ord(c) for c in (" ," + string.ascii_uppercase + string.ascii_lowercase)]

def tohex(v):
  return chr(v).encode("hex")

class Unscramblr:

  def __init__(self, possibleChars=POSSIBLE_CHARACTERS):
    self.possibleChars = possibleChars
    self.tocompare = []

  def addHexString(self, hexString):
    self.tocompare.append(hexString.decode("hex"))

  def decode(self, hexString): 
    print hexString
    hexString = hexString.decode("hex")
    likelihoods = defaultdict(lambda : defaultdict(int))

    for comparing in self.tocompare:
      charIndex = 0
      xored = [tohex(ord(x) ^ ord(y)) for (x, y) in zip(hexString, comparing)]
      for xoredChar in xored:
        inputs = self.getPossibleChars(xoredChar)

        for k in inputs:
          likelihoods[charIndex][k] = likelihoods[charIndex].get(k, 0) + inputs[k]

        charIndex += 1

    truths = []

    for charIndex, character in likelihoods.iteritems():
      truths.append(chr(max(character, key=character.get)))

    return "".join(truths)

  
  def getPossibleChars(self, xored):
    xored = int(xored, 16)
    # Small optimization for common case
    if xored == 0:
      return {}
    possible = defaultdict(int)
    for i in self.possibleChars:
      for j in self.possibleChars:
        if i ^ j == xored:
          possible[i] += 1
          possible[j] += 1
    return possible

