# 存储朋友喜欢的数字
favorite_numbers = {
    'Alice': 7,
    'Bob': 3, 
    'Charlie': 42,
    'Diana': 13,
    'Edward': 8
}

# 打印每个人的名字和喜欢的数字
print("=== 朋友们喜欢的数字 ===")
for name, number in favorite_numbers.items():
    print(f"{name} 喜欢的数字是: {number}")
