import random


class random_id():
    id_list = []
    brak_id_list = []
    while len(id_list) < 7:
        id_list.append(random.randint(0, 9))
    n = int(''.join(map(str, id_list)))


r_id = random_id()
