__author__ = 'RongbingMiao'


def roll_dice(nb_dice):
    input('> Press Enter to cast dice!')
    time.sleep(1)
    return [randint(1,6) for _ in range(nb_dice)]

