#Code for Program

n = int(input("Enter number of elements for the dynamic list: "))
# Below line read inputs from user using map() function
num= list(map(int,input("\nEnter the numbers (with a space) : ").strip().split()))[:n]
print("\nList is - ", num)
print("Original list of integers:")
print(num)
print("\nSquare every number of the input list:")
square_num = list(map(lambda x: x ** 2, num))
print(square_num)
print("\nCube every number of the input list:")
cube_num = list(map(lambda x: x ** 3, num))
print(cube_num)

#End of the program#
