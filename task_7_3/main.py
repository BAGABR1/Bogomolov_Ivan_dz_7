import os
import shutil

root_dir = os.path.join('my_project', 'templates')
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
root_dir = os.path.join('my_project', 'templates', 'mainapp')
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
root_dir = os.path.join('my_project', 'templates', 'authapp')
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
with open(r'my_project\authapp\templates\authapp\base.html', 'r', encoding='utf-8') as fsrc:
    with open(r'my_project\templates\authapp\base.html', 'a', encoding='utf-8') as fdst:
        fsrc.read()
        shutil.copyfileobj(fsrc, fdst)
fsrc = r'my_project\authapp\templates\authapp\index.html'
shutil.copy(fsrc, r'my_project\templates\authapp')
with open(r'my_project\mainapp\templates\mainapp\base.html', 'r', encoding='utf-8') as fsrc:
    with open(r'my_project\templates\mainapp\base.html', 'a', encoding='utf-8') as fdst:
        fsrc.read()
        shutil.copyfileobj(fsrc, fdst)
fsrc = r'my_project\mainapp\templates\mainapp\index.html'
shutil.copy(fsrc, r'my_project\templates\mainapp')
