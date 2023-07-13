for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# if文で偶数を指定しているので、奇数のみが表示される
# 0も偶数(WAO)
#
for i in range(10):
    if i % 2 == 0:
        break
    print(i)
# ちなみにcontinueをbreakに変えると何も表示されない。
# 一発目で偶数(0)が該当してしまうため
