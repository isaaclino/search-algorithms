import os

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapsackDynamic(W, weight, value, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                K[i][j] = 0
            elif weight[i-1] <= j:
                K[i][j] = max(value[i-1] + K[i-1][j-weight[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
 
    return K[n][W]


#naive representation of knapsack
def knapsackNaive(W, weight, value, n):
    #base case
    if n == 0 or W == 0 :
        return 0
    
    #case if the weihgt in the nth item is more than knapsack of capacity
    #W, it cannot be included in optimal solution
    elif (weight[n-1] > W ) :
        return knapsackNaive (W, weight, value, n-1)
    
    #max of two cases
    else:
        return max(value[n-1] + knapsackNaive(W-weight[n-1], weight, value, n-1), knapsackNaive(W, weight, value, n-1))

def main():
    
    os.system('clear')

    ### Naive test ###
    W = 50
    weight = [10, 20, 30]
    value = [60, 100, 120]
    n = len(value)
    
    print "\nNaive recursive that return max value of knapsack of capacity W"
    print "Max value: ", knapsackDynamic(W, weight, value, n)


    print "\nDynamic Programming that return max value of knapsack of capacity W"
    print "Max capacity: ", knapsackNaive(W, weight, value, n)

if __name__ == '__main__': main()

