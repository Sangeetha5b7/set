'''
 Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
'''
set_input = input("Enter the set values separated by space: ")
value_to_delete = int(input("Enter the value to delete: "))
values_set = set(map(int, set_input.split()))
if value_to_delete in values_set:
    values_set.remove(value_to_delete)
    # Print the remaining values with space separation
    print(" ".join(map(str, sorted(values_set))))
else:
    print("Given value is not present in the set list.")
