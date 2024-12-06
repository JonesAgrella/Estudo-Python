# def find_outlier(integers):

#     list_even = []
#     list_odd = []

#     list(set(integers))

#     for integer in integers:
#         if integer % 2 == 0:
#             list_even.append(integer)
#             if len(list_even) == 1:
#                 result = integer
#         else:
#             list_odd.append(integer)
#             if len(list_odd) == 1:
#                 result = integer
#     return result


def find_outlier(integers):
    # Check the first three numbers to determine the majority parity
    first_three = integers[:3]
    even_count = sum(1 for x in first_three if x % 2 == 0)
    
    # If more than half of the first three numbers are even, the majority is even, otherwise it's odd
    majority_is_even = even_count > 1
    
    # Now, iterate through the list and find the outlier
    for number in integers:
        # Check if the number's parity matches the majority parity
        if (number % 2 == 0) != majority_is_even:
            return number
        
print(find_outlier([1,1,1,1,1,44,7,7,7,7,7,7,7,7,44]))
