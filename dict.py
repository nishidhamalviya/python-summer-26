my_dict = {'a':'1','b':'2'}
my_dict['c'] = 3
print("updated dict", my_dict)
#createdmydict
dict_comp = {x: x**2 for x in range(1, 6)}
print("Dictionary comprehension:", dict_comp)

for k,v in my_dict.items():
     print(f"Key: {k}, Value: {v}")
