#1 Объединение словарей
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_3 = dictionary_1.copy()
dictionary_3.update(dictionary_2)
print(dictionary_3)

#2 Перемноженные значения словаря
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1
for key in my_dict:
    result = result * my_dict[key]
print(result)

#3 Словарь от 1 до 10 в кубе
a = {i: i**2 for i in range(11)}
print(a)

# 4 Созданте списка из словарей
list1 = ['I', 'Love', 'Python']
list2 = [10, 20, 30]
dic = {}
for i in range(0, len(list1)):
    dic[list1[i]] = list2[i]
dic = dict(zip(list1, list2))
print(dic)