import sys

if len(sys.argv) < 4:
    print(r"py .\Ex_5.py 'in_data/users.csv' 'in_data/hobby.csv' 'out_data/users_hobby.txt'")
    exit()

with open(sys.argv[1], 'r', encoding='utf-8') as f_users:
    with open(sys.argv[2], 'r', encoding='utf-8') as f_hobby:
        with open(sys.argv[3], 'w+', encoding='utf-8') as f_users_hobby:
            if sum(1 for _ in f_users) < sum(1 for _ in f_hobby):
                exit(1)

            f_users.seek(0)
            f_hobby.seek(0)
            for user in f_users:
                hobby = f_hobby.readline().strip()
                f_users_hobby.write(f"{user.strip()}: {hobby if hobby else None}\n")
