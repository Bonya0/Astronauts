from collections import Counter


def opening_file():
    space = []
    with open('astronauts.csv', 'r', encoding='utf-8') as file:
        for index, data in enumerate(file):
            if index != 0:
                formed_data = data.strip().split(',')
                astronauts = {'Name': formed_data [0],'Birthday': formed_data [4]}
                space.append(astronauts)
    return space


def birthdays():
    birth_month = []
    astronaut = opening_file()

    for elem in astronaut:
        month = elem['Birthday'][:2]
        if month[1] == '/':
            month = month.replace('/', '')
        birth_month.append(month)
    return birth_month


def main():
    birth_month = birthdays()
    counter = Counter(birth_month)

    frequent1 = counter.most_common(1)[0]
    frequent2 = counter.most_common(2)[1]
    frequent3 = counter.most_common(3)[2]

    length = len(birth_month)

    print(f'A három leggyakoribb születési hónap:\n{frequent1[0]}. hónap - {round((frequent1[1]/length*100),2)}%'
          f'\n{frequent2[0]}. hónap - {round((frequent2[1]/length*100),2)}%'
          f'\n{frequent3[0]}. hónap - {round((frequent3[1]/length*100),2)}%')


main()


