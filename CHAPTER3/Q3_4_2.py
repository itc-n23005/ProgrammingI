numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n
print(x)

# 20
# if文で10より大きい数をbreakしているため
# n内の10より小さい数を足した数が表示される。
