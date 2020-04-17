"""
hackerRank--tuples.py
Given an integer, n , and n space-separated integers as input, create a tuple, t, of those n integers.
Then compute and print the result of hash(t).
INPUT:
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t .
"""


while True:
  n = int(input('Enter the number of elements in tuple:  '))
  if n == 'stop': break
  input_line = input('Enter the elements of the tuple, seperated by a space: ')
  integer_list = map(int, input_line.split())
  t = tuple(integer_list)
  print(hash(t))
