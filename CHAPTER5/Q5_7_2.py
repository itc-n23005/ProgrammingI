deta = [
    ["0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["0002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["0003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["0004", "Male", "Suzuki", "Ichiro", 35, "Hokkaido"],
]
deta

member_information = {}
for record in deta:
    key = record[0]
    info = record[1:]
    member_information[key] = info

print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)

# 9行目〜13行目で辞書変数生成と表データの格納をしている
