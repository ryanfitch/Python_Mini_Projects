import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def nchoices(iterable, n):
  newlist = []
  for index in range(n):
    sample = random.choice(iterable)
    newlist.append(sample)
    print(newlist)

nchoices(my_list, 5)