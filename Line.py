'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
input_values = input("Enter the set values separated by space (including duplicates): ")
values_list = list(map(int, input_values.split()))
unique_values = set(values_list)
print(len(unique_values))
