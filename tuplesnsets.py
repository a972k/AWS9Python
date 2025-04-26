unique_numbers = {2, 3, 5, 6, 8}
square_tuple = tuple(x**2 for x in unique_numbers)
print(f"\nsquare of unique numbers: {square_tuple}")

numbers_list = list(unique_numbers)
numbers_list.sort(reverse=True)
print(f"\nsorted list of unique numbers in reverse order: {numbers_list}") 

numnbers_intersectionv = unique_numbers.intersection(square_tuple)
if len(numnbers_intersectionv) == 0:
    print("\nno intersection found.")
else:
    print(f"\nintersection of unique numbers and square tuple: {numnbers_intersectionv}") 
    
print("\nlenght of unique numbers set is :", len(unique_numbers))
print("\nlenght of square tuple is :", len(square_tuple))   
      
#square_tuple = tuple{"\nx**3 for x in unique_numbers"}
#print(f"\nsquare of unique numbers: {square_tuple}")
    