# 文字列を書いた作り方
answer = """○ ● ● ●
● ○ ● ●
● ● ○ ●
● ● ● ○
"""
print(answer)

# 制御文字と掛け算
w = "○ "
b = "● "
answer = w + b * 3 + "\n" + b + w + b * 2 + "\n" + b * 2 + w + b + "\n" + b * 3 + w
print(answer)

# for,if
answer = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer += w
        else:
            answer += b
    answer += "\n"
print(answer)
