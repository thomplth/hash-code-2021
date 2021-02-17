def parse(filename):
    with open(filename, 'r') as fi:
        nOfPizzas, nOfTwo, nOfThree, nOfFour = map(int, fi.readline().split())
        pizzas = []
        ingredients = {}
        index = 0

        for line in fi:
            try:
                pizza = [index]
                index += 1
                pizza.extend(list(map(str, line[1:].split())))
                for ingredient in pizza[1:]:
                    if ingredient not in ingredients:
                        ingredients[ingredient] = 1
                    else:
                        ingredients[ingredient] += 1
                pizzas.append(pizza)
            except ValueError:
                print(line)

        pizzas = sorted(pizzas, key=lambda x: len(x), reverse=True)
        ingredients = {k: v for k, v in sorted(ingredients.items(), key=lambda item: item[1])}

        dataset = {
            'pizzas': pizzas,
            'nOfPizzas': nOfPizzas,
            'nOfTwo': nOfTwo,
            'nOfThree': nOfThree,
            'nOfFour': nOfFour,
            'ingredients': ingredients      
        }

        return dataset

# print(parse('datasets/a_example'))
# print(parse('datasets/b_little_bit_of_everything.in'))
# print(parse('datasets/e_many_teams.in'))