a = {x for x in "abcabcabc" if x not in "ab"}
print(a)

# 'a'でも'b'でもない'c'がxに追加
# 集合では重複が排除されるので要素はç単体となる
