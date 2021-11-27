import json

with open('in_data/users.csv', 'r', encoding='utf-8') as f_users:
    with open('in_data/hobby.csv', 'r', encoding='utf-8')  as f_hobby:
        if sum(1 for _ in f_users) < sum(1 for _ in f_hobby):
            exit(1)

        dictionary = {}
        f_users.seek(0)
        f_hobby.seek(0)
        for user in f_users:
            hobby = f_hobby.readline().strip()
            dictionary.setdefault(' '.join(user.strip().split(',')), hobby if hobby else None)

with open('out_data/dictionary1.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(dictionary))
    f.seek(0)
    print(json.loads(f.read()))
