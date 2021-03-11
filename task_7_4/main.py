import os

key = int(100)
my_list = [int(0), int(0), int(0), int(0)]
my_dict = {}
root_dir = 'my_project'
for root, dirs, files in os.walk(root_dir):
    for i in files:
        if int(os.stat(rf'{root}\{i}').st_size) < 100:
            my_list[0] += 1
        else:
            if 100 < int(os.stat(rf'{root}\{i}').st_size) < 1000:
                my_list[1] += 1
            else:
                if 1000 < int(os.stat(rf'{root}\{i}').st_size) < 10000:
                    my_list[2] += 1
                else:
                    if 10000 < int(os.stat(rf'{root}\{i}').st_size) < 100000:
                        my_list[3] += 1
for i in range(len(my_list)):
    my_dict[key] = my_list[i]
    key *= 10
print(my_dict)
