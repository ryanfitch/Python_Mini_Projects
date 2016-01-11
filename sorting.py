# sorting.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Sorting program.
# This program defines and shows buble sort, selection sort, and insertion sort in action on a small list.

def main():

    # define the lists that need sorted for each sort function
    numList1 = [67, 45, 2, 13, 1, 998]
    numList2 = [67, 45, 2, 13, 1, 998]
    numList3 = [67, 45, 2, 13, 1, 998]

    # creates a function called 'bubbleSort' which performs bubble sort on whatever number list is passed to it.
    def bubbleSort(numList1):

        # checks to see how long the list is and iterates through each index of the list 
        for passnum in range(len(numList1)):
            # creates a for loop which iterates through the list checking which number is larger and then passing it to the next index point in the list so that it bubbles up to the top.
            for i in range(passnum):
                # checks to see if the number on the left of two consecutive index points is bigger
                if numList1[i]>numList1[i+1]:
                    # if number loated at index[i] is bigger add it to the temp variable
                    temp = numList1[i]
                    # swaps number at index [i+1] postion to [i] position so the lower number can move lower in the list
                    numList1[i] = numList1[i+1]
                    # adds the bigger number stored in the temp variable to next index number so that it above the lower number which was just moved down
                    numList1[i+1] = temp

    print("List before bubble sort: {}".format(numList1))
    bubbleSort(numList1)
    print("List after bubble sort: {}".format(numList1))


    def selectionSort(numList2):
        # defines fillslot as being the last point in the list index which to move the next largest number to
        for fillslot in range(len(numList2)-1,0,-1):
            positionOfMax=0
            # for ??
            for location in range(1, fillslot+1):
                # look through list to find the largest number and move it the positionOfMax
                if numList2[location]>numList2[positionOfMax]:
                    positionOfMax = location
            # move largest number to the last index position in the list
            temp = numList2[fillslot]
            numList2[fillslot] = numList2[positionOfMax]
            numList2[positionOfMax] = temp

    print("List before selection sort: {}".format(numList2))
    selectionSort(numList2)
    print("List after selection sort: {}".format(numList2))


    def insertionSort(numList3):
        # since we want to swap an item with previous one, we start from 1
        for index in range(1, len(numList3)):
            # look at number value in current index
            currentvalue = numList3[index]
            position = index
            # no point going until index[0] since there is no value to its left to be swapped
            while position>0 and numList3[position-1]>currentvalue:
                # swap the items, if right one is smaller
                numList3[position]=numList3[position-1]
                # take value all the way left to the place where it has a smaller/no value to its left.
                position = position-1

            numList3[position]=currentvalue

    print("List before insertion sort: {}".format(numList3))
    insertionSort(numList3)
    print("List after insertion sort: {}".format(numList3))
    
if __name__ == "__main__": main()


