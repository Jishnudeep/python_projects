"""
Min Number Of Coins For Change
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, 
write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations. 
Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10] . 
you have access to an unlimited amount of 1 s, 5 s, and 10 s. If it's impossible to make change for the target amount, return -1

Optimal complexity level - O(n * d) - at the edge case, complexity will be O(n^2)

Sample Input: 
n=7
Denoms = [1, 5, 10]

Sample Output:
3

"""

import time
import sys
 

def min_coins(values,target):
    # using dynamic programming to solve this
    # the approach is such that we will take a temporary array where array[i] will store minimum
    # number of coins required for i th value.
    temp = [sys.maxsize for i in range(target + 1)]

   #Our base case is if the target is 0
    temp[0] = 0
    
    # Computing minimum values for all coins from 1 to target
    for i in range(1, target + 1):
        # Going through all coins smaller than i 
       for j in range(len(values)):
           if(values[j] <= i):
               sub_res = temp[i - values[j]]
               print(sub_res)
               if(sub_res != sys.maxsize and sub_res + 1 < temp[i]):
                    temp[i] = sub_res + 1
    print(temp)
                    
    if temp[target] == sys.maxsize:
        return -1
    
    #print(temp)
    return temp[target]



if __name__ == "__main__":
    coin_values = list(map(int,input("Enter coin denominations with space: ").split(' ')))
    target_value = int(input("Enter target value: "))
      
    start_time = time.time()


    result = min_coins(sorted(coin_values),target_value)
    print("The the number coins needed for {} is : {}".format(target_value,result))
    print("%f seconds" % (time.time() - start_time))
