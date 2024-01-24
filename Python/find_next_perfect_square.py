# DESCRIPTION:
# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square
import math
def next_perfect_square(n):
    if not math.sqrt(n).is_integer():
        return -1
    
    while n > 0:
        n += 1
        if math.sqrt(n).is_integer():
            return n


print(next_perfect_square(121)) #144
print(next_perfect_square(625)) #676
print(next_perfect_square(319225)) # 320356
print(next_perfect_square(15241383936)) # 15241630849
print(next_perfect_square(114)) # -1
print(next_perfect_square(155)) # -1
print(next_perfect_square(342786627)) # -1

### Without math import ###

# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1

### With math import ###
# from math import sqrt
# def find_next_square(sq):
#     return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1