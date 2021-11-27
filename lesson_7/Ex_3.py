import os
import shutil

target = os.path.abspath(r'my_project\templates')
if not os.path.exists(target):
    os.mkdir(target)

for root, dirs, files in os.walk('my_project'):
    if 'templates' in root and files and r'my_project\templates' not in root:
        dir_path = os.path.abspath(os.path.join(target, root.split('\\templates\\')[1]))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        for f in files:
            src = os.path.abspath(os.path.join(root, f))
            trgt = os.path.abspath(os.path.join(dir_path, f))
            if not os.path.exists(trgt):
                shutil.copy(src, trgt)
