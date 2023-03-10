
"""
AUTHOR: Francis Osei Annin
DATE: 23/02/23
DESCRIPTION: This program searches for an element in a sequential data structure such 
as an array/list.
"""



"""
Algorithm Explained

* Given an array or a collection data structure
* The algorithm walks through each item in the structure
* it checks each element and compares it to the desired/target element.
* if found, it breaks and return a boolean 
* with the position of the element in the array

EDGE CASES:
This naive implementation doesn't really work well for all data types.
For example, a floating point number comparism of (0.5 + 0.1 != 0.6),
this is as a result of internal rounding error. In such an instance, the
algorithm designed below won't be effective and efficient.
We must take care of this edge case.
... see function **linear_search_float**

"""
def linear_search(array, target_element):
    """
    This function accepts two parameters, array and target_element arguments
    returns a boolean and position(index) of the target element in the array/list.
    Big Oh: O(N)
    """
    for index, element in enumerate(array):
        if element == target_element:
            return True, index
    return False, None


def linear_search_float(array, target_element:float):
    """
    **edge case**
    this implementation handles the edge case described on line 20 - 26
    """
    for index, element in enumerate(array):
        if abs(element-target_element) <1e-9: # determines the absolute difference between the 
            # target element and the element in array. if the difference is less than 
            # 1e-9 which is a very small number, then we can safely say,they are equal
            return True, index
        return False, None 



if __name__ == '__main__':
    print(linear_search([1,2,3,4,5,6,7], 2))
    print(linear_search(["male", "female"], "male"))
    print(linear_search(["male", "female"], "female"))
    print(linear_search([100,34.45, 3.00], 3))
    
    
