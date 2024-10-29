# # ### creating an empty list

# # empty_list = list()

# # print(empty_list)

# # ## creating another list with 2, 3, 4

# list_nums = list([2, 3, 4])

# # print(list_nums)

# # ## alternative 
# list_nums_2 = [5, 6, 7]

# print(list_nums_2)

# user_name = "Moro"

# ## access the elements within a list
# ## [] = index operator
# print(list_nums_2[0])
# print(list_nums_2[1])
# # print(list_nums_2[2])

# ## To easily get all elements in the list
# # for each_item in list_nums:
# #     print(each_item)

# # for each_item in range (list_nums_2):
# #     print(each_item)

# # for seq in range(0, 3):
# #     print(list_nums[seq])

# # for seq in range (0, 3):
# #     print(list_nums_2[seq])

# ## accessing all items within a list
# print("............................")
# for seq in range(0, len(list_nums)):
#     print(list_nums[seq])

# ## lets return the size
# print("................................")
# print(len(list_nums))

# ## create a new list
# house_items = ["2", 3, "dog", 2, "tv", "boys"]

# ## list slicing

# # print("..............................")
# # print(house_items[0:1])
# # print(house_items[0:3])
# print(house_items[2:6])

# ## adding a new element to the list
# house_items.append("girls")

# print(house_items)

# ## extending a list
# house_items.extend(list_nums)

# print(house_items)
# print(".........................................")

# ## insert an item in a specific index
# house_items.insert(0, "pen")

# print(house_items)
# house_items.remove("dog")
# print(house_items)

# ## returns the index of an element within a list
# print(house_items.index("girls"))

# ## creating an empty list
# fav_sports = []
# ## ask the user for their fav sports
# user_input = ("what is your fav sports:")
# ## add that to the original list
# fav_sports.append(user_input)
# ## ask the user for their fav sports
# user_input = ("What team do you support in that sport:")
# ## add that to the original list
# fav_sports.append(user_input)
# print(fav_sports)

## ways of creating a dic

## dict() , {} key : value
my_dict = {
        "name" : "John", "age" : 30, "City" : "New York"
}

class_records = {
    1 : {"Sam Tugga", "Class 6"},
    2 : {"Lydia Mensah", "Class 6"},
    3 : {"Hassan Musah", "Class 6"}
}
print(my_dict["age"])

print(my_dict["City"])

print(class_records[1])

## return all the keys in a dictionary
print(class_records.keys())

## return all the values in a dictionary
print(class_records.values())

## insert a new record in the dictionary
class_records[4] = {"Shadrack", "Class 6"}

print(class_records)

print("................................................")
var = class_records.keys()
for each_item in var:
    print(class_records [each_item])