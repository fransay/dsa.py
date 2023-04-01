# AUTHOR: Francis Osei Annin
# DATE: 17/02/23
# DESCRIPTION: This program linearly searches for desired elements in a collection data structure,
# using the sentinel approach.


"""
ALGORITHM EXPLAINED
* Given an array of size n and a target which defines a search element
* The algorithm defines the last element in the target array/list.
* The last element in the array/list is replaced with target element which
* in this implementation is known as the key.
* An iteration is defined walk through the data structure.
* The last element is replaced with its initial value.
* The iteration breaks when the search term/key is found.
* Sentinel linear is an unpopular variant of the linear search algorithm with an O(N) complexity.


EDGE CASE
* floating point comparison must be taken care. See linear_search.py script for
extended information on handling floating point comparison.
"""


# sentinel_ls: sentinel_ls is an abbreviation of the term sentinel linear search
def sentinel_linear_search(array, n, key):
    """
    returns a boolean representation of an index value of the key in search
    array: array structure
    n: size of the array
    key: item in search
    """
    last_element = array[n - 1]
    array[n - 1] = key
    counter = 0
    while array[counter] != key:
        counter += 1
    array[n - 1] = last_element
    if counter <= n - 1 or counter == key:
        return True, counter
    return False, None


if __name__ == '__main__':
    print(sentinel_linear_search([1, 2, 4, 5], 4, 2))
    print(sentinel_linear_search([11, 12, 14, 15], 4, 12))
    print(sentinel_linear_search([11, 21, 41, 51], 4, 41))
    print(sentinel_linear_search([111, 211, 411, 511], 4, 511))

