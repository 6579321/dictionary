test_dict = {'codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}

print("The original dictionary :" + str(test_dict))

k = int(input("Enter the frequencies you want to know"))

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of k is : " + str(res))