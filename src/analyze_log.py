def maria(orders):
    most_requested = list()

    for order in orders:
        if "maria" in order:
            food = order.split(',')[1]
            most_requested.append(food)

    return max(set(most_requested), key=most_requested.count)


def arnaldo(orders):
    food = list()

    for order in orders:
        if "arnaldo" in order:
            line = order.split(',')[1]
            food.append(line)

    return food.count('hamburguer')


def joao(orders):
    food = list()
    days = list()
    joao_food = list()
    joao_days = list()

    for order in orders:
        line = order.split(',')
        food.append(line[1])
        days.append(line[2].replace("\n", ""))
        if "joao" in order:
            joao_food.append(line[1])
            joao_days.append(line[2].replace("\n", ""))

    return [list(set(food) - set(joao_food)), list(set(days) - set(joao_days))]


def analyze_log(path_to_file):
    if not (".csv") in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding='utf-8') as file:
            orders = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(maria(orders) + '\n')
        f.write(str(arnaldo(orders)) + '\n')
        f.write(str({k for k in joao(orders)[0]}) + '\n')
        f.write(str({k for k in joao(orders)[1]}) + '\n')
