'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
input_values = input("Enter the set values separated by space: ")
values_set = set(map(int, input_values.split()))
max_value = max(values_set)
min_value = min(values_set)
print("Maximum:", max_value)
print("Minimum:", min_value)
