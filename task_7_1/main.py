import os

dir_path = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
dir_path = os.path.join('my_project', 'mainapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
dir_path = os.path.join('my_project', 'adminapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
dir_path = os.path.join('my_project', 'authapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
