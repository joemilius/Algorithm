# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

# Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

# alternative text

# Hint:
# See Fibonacci sequence

# Ref:
# http://oeis.org/A000045

# The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

# perimeter(5)  should return 80
# perimeter(7)  should return 216

def perimeter(n):
    previous = 0
    current = 1
    next = 1
    total_perimeter = 1
    for i in range(n):
        next = previous + current
        previous = current
        current = next
        
        total_perimeter += next
        

    return total_perimeter * 4


print(perimeter(5)) # 80
print(perimeter(7)) # 216
print(perimeter(20)) # 114624
print(perimeter(30)) # 14098308
print(perimeter(100)) # 6002082144827584333104
print(perimeter(500)) # 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504


#####
# def perimeter(n):
#     a, b = 1, 2
#     while n:
#         a, b, n = b, a + b, n - 1
#     return 4 * (b - 1)

#####
# def perimeter(n):
#     list= [1,1]
#     for i in range(1,n):
#         list.append(list[i]+list[i-1])
#     perimeter = 4 * sum(list)
#     return perimeter

#####
# def perimeter(n):
#     x1 = 1
#     x2 = 0
#     s = 0
#     for i in range(n + 1):
#         x1, x2 = x2, x1 + x2
#         s += x2
#     return 4 * s