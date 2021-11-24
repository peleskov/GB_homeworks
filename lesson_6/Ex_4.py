with open('in_data/users.csv', 'r', encoding='utf-8') as f_users:
    with open('in_data/hobby.csv', 'r', encoding='utf-8')  as f_hobby:
        with open('out_data/users_hobby.txt', 'w+', encoding='utf-8') as f_users_hobby:
            if sum(1 for _ in f_users) < sum(1 for _ in f_hobby):
                exit(1)

            f_users.seek(0)
            f_hobby.seek(0)
            for user in f_users:
                hobby = f_hobby.readline().strip()
                f_users_hobby.write(f"{user.strip()}: {hobby if hobby else None}\n")
            f_users_hobby.seek(0)
            print(f_users_hobby.read())
