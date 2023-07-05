def sum_list(my_list):
    sum = 0
    list_length=len(my_list)
    for i in range(list_length):
        sum+=my_list[i]
    return sum




list1 = [10, 2, 9, 8]
list1.append(11)
list1.append(19)

print(list1)
my_sum = sum_list(list1)

print(my_sum)



