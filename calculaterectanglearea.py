def rectangle_area(length : float, width : float) -> float:
    
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {rectangle_area(length, width)}")
