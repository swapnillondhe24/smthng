#!/usr/bin/env python
# coding: utf-8

# # Fractional KnapSack

# In[15]:


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

    finalvalue = 0.0
    
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        else:
            finalvalue += item.value * W / item.weight
            break
    return finalvalue


if __name__ == "__main__":
    W = 50
    arr = [ Item(100, 20),Item(60, 10), Item(120, 30)]
    max_val = fractionalKnapsack(W, arr)
    print ('Maximum value we can obtain = {}'.format(max_val))


# # 0 1 KnapSack

# In[7]:


def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print (knapSack(W, wt, val, n))


# # 0 1 Knapsack Dynamic Programming

# In[8]:


def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)] # Making the dp array

    for i in range(1, n+1): # taking first i elements
        for w in range(W, 0, -1): # starting from back,so that we also have data of
                                # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])

    return dp[W] # returning the maximum value of knapsack

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)


print(knapSack(W, wt, val, n))


# # QuickSort

# In[3]:


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


# # N-Queens

# In[28]:


class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens) # p is the index of row
            if p == n:
                result.append(queens)
                return None
            for q in range(n): 
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


s = Solution()
res = s.solveNQueens(7)


# In[29]:


for re in res:
    print("*"*10)
    for r in re:
        print(r)


# In[2]:





# In[ ]:




