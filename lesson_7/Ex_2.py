import yaml
from Ex_1 import check_el
config = {
    'my_project': {
        'settings': ['__init__.py', 'dev.py', 'prod.py'],
        'mainapp': ['__init__.py', 'models.py', 'views.py', {
                'templates': {
                    'mainapp': ['base.html', 'index.html']
                }
            }
        ],
        'authapp': ['__init__.py', 'models.py', 'views.py', {
                'templates': {
                    'authapp': ['base.html', 'index.html']
                }
            }
        ]
    }
}

with open('config.yaml', 'w', encoding='utf-8') as f:
    f.write(yaml.dump(config))

with open('config.yaml', encoding='utf-8') as f:
    starter = yaml.safe_load(f.read())

check_el(starter)
