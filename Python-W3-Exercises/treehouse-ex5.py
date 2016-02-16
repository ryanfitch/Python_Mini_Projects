# create a function named combo() that takes two iterables and returns a list of tuples.  each tuple should hold the first item in each list
# then the second set, then the third and so on.  Assume the iterables will be the same length.

def combo(iter1, iter2):
    combo_list = []
    for index, value in enumerate(iter1):
        tuple = value, iter2[index]
        combo_list.append(tuple)
    print(combo_list)

combo([1, 2, 3], 'abc')

