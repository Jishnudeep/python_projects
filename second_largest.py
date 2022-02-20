"""
Second Largest in the Array of Integers
Find the Second largest number from the array of integers

Optimal complexity level - O(n)
Edge test case eg :  [1,2,3,4,5,4,5,6,5,4]

"""
import time

def second_largest_element(array):
    array_set = set(array)
    array_set.remove(max(array_set))

    return max(array_set)



if __name__ == "__main__":
    array = list(map(int,input("Enter list elements with space: ").split(' ')))
    
    start_time = time.time()


    result = second_largest_element(array)
    print("The second largest element is : {}".format(result))
    print("%f seconds" % (time.time() - start_time))