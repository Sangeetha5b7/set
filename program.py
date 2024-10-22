'''
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
''''
input_values = input("Enter the values separated by space: ")
values = set(map(int, input_values.split()))
sorted_values = sorted(values)
print(" ".join(map(str, sorted_values)))