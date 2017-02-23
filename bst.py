
#   Binary Search Tree
#
#   AVERAGE (access, search, insertion, deletion):  O(log n)
#   WORST: (access, search, insertion, deletion):   O(n)
#
#   In ordered list if we are clever with our comparisons. 
#   In the sequential search, when we compare against the first node.
#    
#   of all this, a binary search will start by examining the middle node.
#   in some cases we can edit this to a set it at random pivot, if pivot is equal
#   to the number we are looking on list, we are done. If not we can use the ordered
#   list to eliminate half of the remaining nodes.
#
#   If the node we are searching for is greater than the middle node,
#   we know that the entire lower half of the list as well as the middle node
#   can be eliminated from further consideration. The node,
#   if it is in the list, must be in the upper half.
#
#   We can then repeat the process with the upper half.
#   Start at the middle node and compare it against what we are looking for.
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

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# A utility function to search a given key in BST
def search(root,key):
    
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
    
    # Key is smaller than root's key
    return search(root.left,key)

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def search_iteratively(list, node):

    # set the root node and last node
    # substract 1 to avoid counting null terminator
    first = 0
    last = len(list)-1
    found = False
    
    #it searches iterative
    while first<=last and not found:
        
        #get the floor average pivot midpoint
        #pivot = midpoint
        midpoint = (first + last)//2
        
        if list[midpoint] == node:
            found = True
        else:
            if node < list[midpoint]:
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
    
    print "\nSearch Iteratively for a number 3: "
    print search_iteratively(list, 3)
    print "\nSearch Iteratively for a number 13: "
    print search_iteratively(list, 13)

# Driver program to test the above functions
# Let us create the following BST
#      50
#    /    \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

# Print inoder traversal of the BST
inorder(r

if __name__ == '__main__': main()

