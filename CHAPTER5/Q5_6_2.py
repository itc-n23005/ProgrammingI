A = {x for x in range(21)}
B = {y for y in range(21) if y % 2 == 0}
C = A - B
print(A)
print(B)
print(C)

# 集合A.Bを作らない場合は、C={x for in range(21) if x % 2 != 0}で求められる
