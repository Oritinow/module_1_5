Immutable_var = (1, 2, 'apple', 'strawberry')
print(Immutable_var)
#Immutable_var_[0] = 10 изменение в данном списке невозможны, потому что кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 'apple', 'strawberry']
mutable_list.extend(["coconut"])
print(mutable_list)
