import requests


def make_request(x):
    age, pclass, sex = x
    data = {'Age': age,
            'Pclass': pclass,
            'Sex': sex}
    myurl = 'http://127.0.0.1:8080' + '/predict'
    headers = {'content-type': 'application/json'}
    response = requests.post(myurl, json=data, headers=headers)
    return response.json()['predictions']


if __name__ == '__main__':
    stop = False
    print('Предсказание, выживет ли пассажир Титаника, по его возрасту, полу и классу каюты.\n')

    while not stop:
        try:
            age = int(input('Введите возраст пассажира:\n'))
            pclass = int(input('Введите класс каюты пассажира (1-3):\n'))
            try:
                assert pclass in [1, 2, 3], 'Класс каюты должен быть целым числом в интервале 1-3.\n'
            except AssertionError as err:
                print(err)
                continue
            sex = int(input('Введите пол пассажира, 0-мужчина, 1-женщина:\n'))
            sex = 'male' if sex == 0 else 'female'
        except (TypeError, ValueError):
            print('Вводить нужно целые числа.\n')
            continue

        answer = make_request((age, pclass, sex))
        print('Пассажир выживет :)\n' if answer else 'Пассажир не выживет :(\n')
        again = input('Введите 1 для проверки следующего пассажира, либо что-то другое для выхода из предсказаний: ')
        stop = True if again != '1' else False
