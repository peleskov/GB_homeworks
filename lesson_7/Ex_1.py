import os

starter = {
    'my_project': [
        'settings',
        'mainapp',
        'adminapp',
        'authapp',
        'test1.py',
        {'test1': [
                'test2',
                'test2.py',
                {'test3': [
                    'test3.py',
                    'test4'
                ]
                }
            ]
        }
    ]
}


def make_el(el, path):
    full_path = f'{path}/{el}'
    try:
        if '.' not in el:
            os.mkdir(full_path)
        else:
            if os.path.exists(full_path):
                raise FileExistsError
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write('')
        print(f'{os.path.abspath(full_path)} - создан')
    except FileExistsError:
        print(f'{os.path.abspath(full_path)} - существует')


def check_el(el, path='.'):
    if isinstance(el, dict):
        for key, val in el.items():
            make_el(key, path)
            check_el(val, f'{path}/{key}')
    else:
        for e in el:
            if isinstance(e, dict):
                for key, val in e.items():
                    make_el(key, path)
                    check_el(val, f'{path}/{key}')
            else:
                make_el(e, path)


if __name__ == "__main__":
    check_el(starter)
