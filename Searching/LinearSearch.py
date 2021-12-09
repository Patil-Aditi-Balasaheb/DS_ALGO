#################
# linear search #
#################

# time complexity = O(n)
# best case = O(1) - when search element is found at first position
# worst case = O(n) - when search element is found last
# space complexity = O(1)
# avg. comparisons = (n+1)/2

li = [45,55,40,97,64,10,37]
search = int(input("Enter a number to be searched: "))
index = -1

for i in range(len(li)):
    if li[i] == search:
        index = i
        break

if index != -1:
    print("Element found at position", index+1)
else:
    print("Element not found")