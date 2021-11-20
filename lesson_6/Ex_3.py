import json

f_users = open('in_data/users.csv', 'r', encoding='utf-8')
f_hobby = open('in_data/hobby.csv', 'r', encoding='utf-8')
if len([0 for _ in f_users]) < len([0 for _ in f_hobby]):
    f_users.close()
    f_hobby.close()
    exit(1)

dictionary = {}
f_users.seek(0)
f_hobby.seek(0)
while True:
    user = ' '.join(f_users.readline().strip().split(','))
    hobby = f_hobby.readline().strip()
    if not user:
        break
    dictionary.setdefault(user, hobby if hobby else None)
f_users.close()
f_hobby.close()
with open('out_data/dictionary1.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(dictionary))
    f.seek(0)
    print(json.loads(f.read()))
