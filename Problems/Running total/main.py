list_numbers = input()
list_numbers = [int(x) for x in list_numbers]
cu_list = [sum(list_numbers[0:x:1]) for x in range(len(list_numbers) + 1)] 
cu_list.pop(0)
print(cu_list)


# smart code
#inp_list = [int(x) for x in input()]
#print([sum(inp_list[:i + 1]) for i in range(len(inp_list))])
digits_list = [int(x) for x in input() if int(x) % 2 != 0]
print(digits_list)

digits_list = [int(x) for x in input()]
print(sum(digits_list) / len(digits_list))


'''Sample Input 1:

12345
Sample Output 1:

[1.5, 2.5, 3.5, 4.5]'''
input_numbers = [int(x) for x in input()]
running_avg = [(input_numbers[i] + input_numbers[i + 1]) / 2 for i in range(len(input_numbers) - 1)]

print(running_avg)
