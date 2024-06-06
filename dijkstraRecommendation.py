import math
import os
import random
import re
import sys
def dijkstra (graph, startProduct):
  n = len(graph)
  minDistances = [100000] * n
  visited = [0] * n

  minDistances[startProduct] = 0

  i = 0
  while i < n:
    minIndex = -1
    
    j = 0
    while j < n:
      if visited[j] == 0 and (minIndex == -1 or minDistances[j] < minDistances[minIndex]):
        minIndex = j
      j += 1

    if minDistances[minIndex] == 100000:
      break
    visited[minIndex] = 1

    k = 0
    while k < n:
      if graph[minIndex][k] != 0:
        potentialDist = minDistances[minIndex] + graph[minIndex][k]
        if potentialDist < minDistances[k]:
          minDistances[k] = potentialDist
      k += 1
    i += 1
  print(minDistances)

if __name__ == '__main__':


    a = [[0, 2, 0, 1, 0],
         [2, 0, 3, 0, 0],
         [0, 3, 0, 4, 0],
         [1, 0, 4, 0, 5],
         [0, 0, 0, 5, 0]]

    dijkstra(a, 0)