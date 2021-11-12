import random
import numpy as np

random_list = [random.choices(range(100))[0] for i in range(100)]


def entropy(word):
    arr = np.array([c for c in word])
    lenght = len(arr)
    count = (np.unique(arr, return_counts=True))[1]
    prob = []
    for value in return_counts):

        p = float(value/lenght)
        prob.append(p)

    H = - np.sum(p*np.log2(p))

    return H






def max(array):

    maximun = array[0]
    for element in array:
        if element > maximum:
            element = maximum

    return maximum


def min(array):

    minimum = array[0]
    for element in array:
        if element < minimum:
            element = minimum

    return minimum

def repeated_values(array):

    repeated = []


    uniques = set(array)

    report = { u:0 for u in set(uniques)}
    for u in uniques:
        for value in array:
            if u == value:
                report.update({u: report[u] + 1 })

    return report


def find_duplicates(list):
  if len(list) == len(set(list)):
      return print("no duplicates")
  if  len(list) != len(set(list)):
      d = {i:list.count(i) for i in list}


      l={}
      for i in d:
          if d[i] != 1 & d[i] != l.items() :
                  l.update({i:d[i]})

  l=dict(sorted(l.items()))
  return l



def eval_func(func):
    arr = np.arange(0, 10, 0.1)

    return func(arr)
