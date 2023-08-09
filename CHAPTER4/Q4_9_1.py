# 悪い例1
spam(ham[1], {eggs: 2})
# 正
spam(ham[1], {eggs: 2})

# 悪い例2
foo= (0, )
# 正
foo = (0,)

# 悪い例3
if x == 4 : print (x , y) ; x , y = y , x
# 正
if x == 4: print(x, y); x, y = y, x
