for i in range(1, 101):
    check_dig = i if i < 20 else int(str(i)[-1])
    print(f"{i} процент{'' if check_dig == 1 else 'а' if 1 < check_dig < 5 else 'ов'}")


