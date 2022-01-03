###############################
# Fractional Knapsack Problem #
###############################

# time complexity: O(n log n)

'''
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In Fractional Knapsack, we can break items for maximizing the total value of knapsack. This problem in which we can break an item is also called the fractional knapsack problem. 
An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can. Which will always be the optimal solution to this problem.
'''

def fractional_knapsack(value, weight, capacity):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """

    # index = [0, 1, 2, ..., n - 1] for n times
    index = list(range(len(value)))

    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]

    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key = lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)

    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break
    
    return max_value, fractions


n = int(input("Enter number of items: "))
value = input("Enter the values of the {} item(s) in order: ".format(n)).split()
value = [int(v) for v in value]

weight = input("Enter the weights of the {} item(s) in order: ".format(n)).split()
weight = [int(w) for w in weight]

capacity = int(input("Enter maximum weight: "))

max_value, fractions = fractional_knapsack(value, weight, capacity)

print("The maximum value of items that can be carried:", max_value)
print("The fractions in which the items should be taken:", fractions)

'''
Runtime test cases

Case 1:
Enter number of items: 3
Enter the values of the 3 item(s) in order: 60 100 120
Enter the positive weights of the 3 item(s) in order: 10 20 30
Enter maximum weight: 50
The maximum value of items that can be carried: 240.0
The fractions in which the items should be taken: [1, 1, 0.6666666666666666]
 
Case 2:
Enter number of items: 5
Enter the values of the 5 item(s) in order: 3 5 1 2 4
Enter the positive weights of the 5 item(s) in order: 40 50 20 10 30
Enter maximum weight: 75
The maximum value of items that can be carried: 9.5
The fractions in which the items should be taken: [0, 0.7, 0, 1, 1]
 
Case 3:
Enter number of items: 1
Enter the values of the 1 item(s) in order: 5
Enter the positive weights of the 1 item(s) in order: 10
Enter maximum weight: 5
The maximum value of items that can be carried: 2.5
The fractions in which the items should be taken: [0.5]
'''