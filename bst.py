
#   Binary Search Tree
#
#   AVERAGE (access, search, insertion, deletion):  O(log n)
#   WORST: (access, search, insertion, deletion):   O(n)
#
#   In ordered list if we are clever with our comparisons. 
#   In the sequential search, when we compare against the first item.
#    
#   of all this, a binary search will start by examining the middle item.
#   in some cases we can edit this to a set it at random pivot, if pivot is equal
#   to the number we are looking on list, we are done. If not we can use the ordered
#   list to eliminate half of the remaining items.
#
#   If the item we are searching for is greater than the middle item,
#   we know that the entire lower half of the list as well as the middle item
#   can be eliminated from further consideration. The item,
#   if it is in the list, must be in the upper half.
#
#   We can then repeat the process with the upper half.
#   Start at the middle item and compare it against what we are looking for.
#
#   EXAMPLE
#   Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
#   and are using the recursive binary search algorithm.
#   Which group of numbers correctly shows the sequence of comparisons used to find the key 8.
#   (A) 11, 5, 6, 8
# ->(B) 12, 6, 11, 8
#   (C) 3, 5, 6, 8
#   (D) 18, 12, 6, 8
#
#   B IS CORRECT since Binary search starts at the midpoint and halves the list each time.
#   Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
#   and are using the recursive binary search algorithm.
#   Which group of numbers correctly shows the sequence of comparisons used to find the key 16.
#   (A) 11, 14, 17
#   (B) 18, 17, 15
#   (C) 14, 17, 15
# ->(D) 12, 17, 15
#   Starts at middle top (12), since 16 is higher it jumps to second middle(17),
#   jumps back but it wont see anything
#
#   D IS CORRECT since Binary search starts at the midpoint and halves the list each time.
import os

def bst(list, item):

    first = 0
    last = len(list)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

def main():
    
    os.system('clear')

    list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    
    print "Binary Search Tree"
    print "Original List: "
    print list
    
    print "\nLooking for a number 3: "
    print bst(list, 3)
    print "\nLooking for a number 13: "
    print bst(list, 13)
    print "\nLooking for a number 42: "
    print bst(list, 42)

if __name__ == '__main__': main()

