from random import shuffle, randint
import os


class Player:
    def __init__(self, is_pc=False):
        self.__is_pc = is_pc
        __nums = [i for i in range(1, 91)]
        shuffle(__nums)
        self.card = []
        for row in [sorted(__nums[i*5:(i+1)*5]) for i in range(3)]:
            for _ in range(4):
                row.insert(randint(0, 9), '')
            self.card.append(row)

    def __str__(self):
        out = '--- Карточка копьютера ---\n' if self.__is_pc else '------ Ваша карточка -----\n'
        out += '\n'.join([f'{" ".join([f"{el:2}" for el in row])}' for row in self.card])
        out += f'\n{"-" * 26}'
        return out

    def check_answer(self, barrel, answer):
        if self.__is_pc:
            self.__find_digit(barrel)
            return True
        else:
            if answer == 'y':
                return self.__find_digit(barrel)
            else:
                return False if self.__find_digit(barrel) else True

    def __find_digit(self, barrel):
        for i in range(3):
            if barrel in self.card[i]:
                self.card[i][self.card[i].index(barrel)] = f' -'
                return True
        return False

    def check_card(self):
        return any([str(el).isdigit() for row in self.card for el in row])


def lotto():
    you = Player()
    pc = Player(True)
    barrels = [i for i in range(1, 91)]
    shuffle(barrels)
    while len(barrels) > 0:
        os.system('cls')
        barrel = barrels.pop()
        print(f'Новый бочонок: {barrel} (осталось {len(barrels)})', you, pc, sep='\n')
        pc.check_answer(barrel, '')
        if not you.check_answer(barrel, input('Зачеркнуть цифру? (y/n): ')):
            print('Вы проиграли!')
            break
        if not pc.check_card():
            print(you, pc, 'Победа компьютера!', sep='\n')
            break
        if not you.check_card():
            print(you, pc, 'Победа Ваша!', sep='\n')
            break
    print('Игра окончена!')


if __name__ == '__main__':
    lotto()
