# def find_balance_index(arr):
#     total_sum = sum(arr)
#     left_sum = 0
    
#     for i in range(len(arr)):
#         # Right sum is total_sum - left_sum - current_element
#         right_sum = total_sum - left_sum - arr[i]
        
#         if left_sum == right_sum:
#             return i
        
#         # Update left_sum for the next index
#         left_sum += arr[i]
    
#     return -1

# # Example usage:
# print(find_balance_index([1, 2, 3, 4, 3, 2, 1]))  # Output: 3
# print(find_balance_index([1, 100, 50, -51, 1, 1]))  # Output: 1
# print(find_balance_index([20, 10, -80, 10, 10, 15, 35]))  # Output: 0

def find_balance_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]

    return -1

print(find_balance_index([1, 2, 3, 4, 3, 2, 1]))