pass_str = 'asdf'
pass_list_int = [10, 20, 30, 40]
make_object_generator = zip(pass_str, pass_list_int)
print(make_object_generator)
for value in make_object_generator:
    print(value)