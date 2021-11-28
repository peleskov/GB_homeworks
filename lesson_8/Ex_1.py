import re


def email_parse(email):
    result = pattern.match(email)
    if not result:
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    return result


input_data = [
    'someone@geekbrains.ru',
    'someone@geekbrainsru',
]

pattern = re.compile(r'^[\w.+-]+@[\w]+(?:\.[\w]+)+$')

for i in input_data:
    print(email_parse(i))
