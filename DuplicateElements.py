'''
 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
n = int(input("Enter the number of values: "))
values_list = []
for _ in range(n):
    value = int(input())
    values_list.append(value)
unique_values = set(values_list)
duplicate_count = len(values_list) - len(unique_values)
print("Duplicate Values:", duplicate_count)
print(" ".join(map(str, sorted(unique_values))))
