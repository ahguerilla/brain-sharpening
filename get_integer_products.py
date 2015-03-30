'''
You have an array of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes an array of integers and returns an array of the products.

For example, given:

[1, 7, 3, 4]
your function would return:

[84, 12, 28, 21]
by calculating:

[7*3*4, 1*3*4, 1*7*4, 1*7*3]
Do not use division in your solution.
'''

def get_products_of_all_ints_except_at_index(list_integers):
    product_list = [1] * len(list_integers)
    multiplier = 1
    for index, i in enumerate(list_integers):
        product_list[index] = multiplier
        multiplier *= i

    multiplier = 1
    counter = len(list_integers) - 1
    while counter >= 0:
        product_list[counter] = product_list[counter]*multiplier
        multiplier *= list_integers[counter]
        counter -= 1

    return product_list

print get_products_of_all_ints_except_at_index([1, 7, 3, 4])
# [84, 12, 28, 21]