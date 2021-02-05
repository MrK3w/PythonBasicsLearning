############ LIST ####################

# Create a new list
#list1 = [1,2,3]

# Append
#list1.append('append me!')

# Show
#print(list1)
# Pop off the 0 indexed item default is -1
#list1.pop(0)
#print(list1)
#reverse this list
#list1.reverse()
#print(list1)


# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print(matrix)
# Grab first item of the first item in the matrix object
print(matrix[0][0])

#Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
