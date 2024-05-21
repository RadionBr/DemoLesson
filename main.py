#### KORTAGE

# info = ("test1", 123)
# print(info)
# print(type(info))
#
# info = "test2", 12314, 444422
# print(info)
# print(type(info))
#
# print(info[0])
#
# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

# import copy
#
# info = "test2", 12313, 2222
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)


# for num in 1, 3, 4, 5, 6, "hello", 7:
#     print(num)
#
# for i in range(5):
#     print(i)
#
# numbers= list(range(10))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)


# users = {
#     1: "john",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     2: "qwerty", #dublirowat nelzya
# }
#
# print(id(users))
# print(users)
# print(type(users))
# print(users[1]) #[1] -> not index
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])

# user_list = [
#     ("1231314214","Tom"),
#     ("+3333333333333", "Bob"),
#     ("+321222222", "Alice")
# ]
#
# users_dict = dict(user_list)
# print(users_dict)
#
# print(users["+3333333333333"])
# users["3333333333333"] = "Petya"
# print(users["3333333333333"])
#
# users["+4444"] = "test"
# print(users["+4444"])

# for key, value in users.items():
#     print(f"key: {key} value: {value}")

# users_1 =  users = {
#      1: "john",
#         2: "Vasya",
#         3: "Petya",
#         "key1": "some-value",
#         2.4: 123,
#         True: 111,
#         2: "qwerty", #dublirowat nelzya
# }
#
# users_2 = {
#     "11111": "rrrrrr"
# }
#
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)

# users = {
#     "Vasya": {
#         "phone": "12312312",
#         "email": "r@gmail.com",
#         "hobby": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "123123",
#         "email": "awweqeqeqw",
#         "hobby": "userelll"
#     }
# }
#
#
# print(users["Vasya"]["hobby"][1])



# key = input("Enter key: ")
# if key in users:
#     print(users[key])
# else:
#     print("noth")


# key = input("Enter key: ").strip().lower()
# for curr_key in users.keys():
#     if curr_key.lower() == key:
#         print(users[curr_key])
#         break
# else:
#     print("noth1")


############################## Mnojini (set)


# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
#
# print(len(users))
#
# users.add("Sam")
# print(users)
#
#
# users = {"Tom", "Bob", "Alice"}
# user = "Tom"
# if user in users:
#     users.remove(user)
# print(users)


# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)


#Read about dictioneries
#make homework

# import random
#
# words = ["apple", "banana"]
#
# secret_word = words[random.randint(0, len(words) -1)]
#
# user_word = ["_"] * len(secret_word)
# print(user_word)