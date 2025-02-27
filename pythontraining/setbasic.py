#creating sets
empty_set=set()
fruits={"apple","banana","cherry"}
print("empty set:",empty_set)
print("set of fruits: ",fruits)

#ADDING AND REMOVING ELEMENTS


#SET OPERATION
# Creating two sets
a = {1, 2, 3, 4, 5, 6}
b = {2, 6, 7, 8, 9, 0}

print("Set a:", a)
print("Set b:", b)
#adding and removing elements from tuple
add=a.add(7)
remove=a.remove(2)
print("the tuple after adding and removing is:",a)

# Union of sets
union_set = a | b  # Alternatively, use a.union(b)
print("Union of a and b:", union_set)

# Intersection of sets
intersection_set = a & b  # Alternatively, use a.intersection(b)
print("Intersection of a and b:", intersection_set)

# Difference of sets (a - b)
difference_set = a - b  # Alternatively, use a.difference(b)
print("Difference (a - b):", difference_set)

# Difference of sets (b - a)
difference_set_b_a = b - a  # Alternatively, use b.difference(a)
print("Difference (b - a):", difference_set_b_a)

# Symmetric difference of sets
symmetric_difference_set = a ^ b  # Alternatively, use a.symmetric_difference(b)
print("Symmetric difference of a and b:", symmetric_difference_set)

# Iterating through a set
