import json
import sys

if len(sys.argv) < 4:
    print('script.py <PATH to users.csv> <PATH to hobby.csv> <PATH to OUT FILE>')
    exit()

f_users = open(sys.argv[1], 'r', encoding='utf-8')
f_hobby = open(sys.argv[2], 'r', encoding='utf-8')
if len([0 for _ in f_users]) < len([0 for _ in f_hobby]):
    f_users.close()
    f_hobby.close()
    exit(1)

dictionary = {}
f_users.seek(0)
f_hobby.seek(0)
while True:
    user = f_users.readline().strip()
    hobby = f_hobby.readline().strip()
    if not user:
        break
    user_info = dict(zip(('Фамилия', 'Имя', 'Отчество'), user.split(',')))
    user_info.update({'хобби': hobby.split(',') if hobby else None})
    dictionary.setdefault(' '.join(user.split(',')), user_info)
f_users.close()
f_hobby.close()
with open(sys.argv[3], 'w+', encoding='utf-8') as f:
    f.write(json.dumps(dictionary))
    f.seek(0)
    print(json.loads(f.read()))
