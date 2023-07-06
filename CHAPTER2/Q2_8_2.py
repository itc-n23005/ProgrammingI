my_list = ["I", "have", "an", "apple"]
my_list[2:4] = ["a", "pineapple"]
print(my_list)
# 終了位置を[4]ではなく[3]にすると、
# ["I", "have", "a", "pineapple", "apple"]の表示
# "an"は"a"になっているけど、"apple"が"pineapple"の前に追加されているだけ。
# インデックスの上限数の次の数を終了位置に指定する。

my_list = ["I", "have", "an", "apple"]
my_list[2:] = ["a", "pineapple"]
print(my_list)
# ↑ 別の書き方
# インデックスの[2]以降を全て置き換えの意味
