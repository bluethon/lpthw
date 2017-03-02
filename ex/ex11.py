the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 大小
print(len(the_count))
# 正向取值
print(the_count[3])
# 逆向取值
print(the_count[-1])

# 增加
the_count.append(6)
print(the_count)

# 赋值
the_count[2] = 10
print(the_count)

# 5
# 4
# 5
# [1, 2, 3, 4, 5, 6]
# [1, 2, 10, 4, 5, 6]

# 扩展部分

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!


# Wait there are not 10 things in that list. Let's fix that.
# Adding:  Boy
# There are 7 items now.
# Adding:  Girl
# There are 8 items now.
# Adding:  Banana
# There are 9 items now.
# Adding:  Corn
# There are 10 items now.
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do some things with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone#Light
