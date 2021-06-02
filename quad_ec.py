# function to make sure only an integer is input
def get_int(s):
    while True:
        x = input(s)
        try:
            return int(x)
        except ValueError:
            print("Value must be integer")


# intro to program
print("Quadratic equation solver")
print("Given equation in the form ax^2 + bx + c = 0, enter coefficients a, b, c one by one to get results")

# gets coefficients of x
a = get_int("Input coefficient a: ")
while a == 0:
    print("a cannot be = 0")
    a = get_int("Input coefficient a: ")
b = get_int("Input coefficient b: ")
c = get_int("Input coefficient c: ")

# calculates discriminant and checks if roots are real or not
discriminant = (b**2) - (4 * a * c)
if discriminant < 0:
    message = "! No real roots ! 'j' is the square root of -1 !"
    should_calculate_vertex = False
else:
    should_calculate_vertex = True
    message = " "

# calculates the 2 roots of x
discriminant = discriminant**0.5
denominator = 2 * a
sol1 = (discriminant - b)/denominator
sol2 = (0 - b - discriminant)/denominator

# outputs the 2 roots
print(message)
print(f"Solution 1:\nx = {sol1:.3f}\n")
print(f"Solution 2:\nx = {sol2:.3f}\n")

if should_calculate_vertex:
    xcoord = (sol1 + sol2)/2
    ycoord = (a*(xcoord**2) + b*xcoord + c)
    print(f"Vertex is at ({xcoord:.3f}, {ycoord:.3f})")
else:
    print("Vertex can be calculated only by completing the square")