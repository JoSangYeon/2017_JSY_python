# variable define and input from user
print("-----y = x^2 integral calculator-----")
range_start = int(input("Enter the start point of range : "))
range_end = int(input("Enter the end point of range : "))
size = range_end - range_start
n = int(input("How many divisions do you want? : "))
delta_x = (range_end - range_start) / n

# def the function integral


def integral(range_start, delta_x):
    value = 0
    for i in range(n):
        value = value + delta_x * ((range_start + (delta_x * i))**2)
    return value


# call the function integral`
result = integral(range_start, delta_x)


print("The integral result is %f." % (result))
