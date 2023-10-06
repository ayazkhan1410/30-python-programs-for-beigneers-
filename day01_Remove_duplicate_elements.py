# Remove duplicate elements
# from a list without using
# sets() in python
# Day 1 of '30 days of 30 Programs challenege' ..
old_list = [1,1,2,2,3,3,4,4,5,5,6,6]
new_list = []

for i in old_list:
    if i not in new_list:
        new_list.append(i)
print("Old list : ", old_list)
print("New list : ", new_list)