def date_format(dur):
    qty_days = dur // (24 * 60 * 60)
    qty_hours = dur % (24 * 60 * 60) // (60 * 60)
    qty_mins = dur % (24 * 60 * 60) % (60 * 60) // 60
    qty_secs = dur % (24 * 60 * 60) % (60 * 60) % 60
    result = f'{qty_days} дн ' if qty_days > 0 else ''
    result += f'{qty_hours} час ' if qty_hours > 0 else ''
    result += f'{qty_mins} мин ' if qty_mins > 0 else ''
    result += f'{qty_secs} сек' if qty_secs > 0 else ''
    return result


def date_format_list(dur_list):
    result = ''
    for dur in dur_list:
        result += f'{date_format(dur)}\n'
    return result


duration = 53
print(date_format(duration))
duration = 153
print(date_format(duration))
duration = 4153
print(date_format(duration))
duration = 400153
print(date_format(duration))
duration_list = [53, 153, 4153, 400153]
print(date_format_list(duration_list))
