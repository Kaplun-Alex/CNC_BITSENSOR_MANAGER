import numpy as np

def list_creator(speed: int, acceleration: int, impulse_count):     # макс скорость, ускорение, количество импульсов.
    res_list = []
    center_list = []
    hvost_list = []
    acc = acceleration
    runner = impulse_count
    half_runner = int(runner / 2)
    acc_ar_aceleration = list(np.arange(acc, speed, acc))  # определяем список для максимального разгона
    to_max_speed = sum(acc_ar_aceleration) * 2
    half_to_max = int(to_max_speed / 2)
    print(acc_ar_aceleration, sum(acc_ar_aceleration))
    print('Полный розгон + остановка займет - ', to_max_speed, 'импульса')
    print(to_max_speed, runner)
    if runner <= acceleration:
        res_list.append(runner)
        print(res_list)
    elif acceleration < runner < acceleration*2:     # Участок инвалидной каляски,
        # между ускорением и ускорением *2 косяк в дальнейшем -> acc_ar_aceleration[-1]
        popadalovo = runner % 2
        print(popadalovo)
        popadalovo_speed = int((runner-popadalovo)/2)
        res_list.append(popadalovo_speed)
        res_list.append(popadalovo_speed)
        res_list.append(popadalovo)
        print(res_list)
    else:
        print('Розгон и торможение займут по - ', half_to_max)
        print('Всего на розгон или торможение по - ', half_runner)
        # Режем ранне определенный список розгона с конца, пока  списка не будет меньше половины пути
        while half_to_max > half_runner:
            s = acc_ar_aceleration.pop()
            half_to_max -= s
        # полный остаток после среза формирования списка розгона и торможения.
        ostatok = runner - (sum(acc_ar_aceleration) * 2)


        if ostatok >= acc_ar_aceleration[-1]:  # если в полном остатке есть величина
            # хотябы одна величина достигнутой скорости
            for i in range(ostatok // acc_ar_aceleration[-1]):
                center_list.append(acc_ar_aceleration[-1])
                ostatok -= acc_ar_aceleration[-1]
            for i in range(ostatok // acceleration):
                hvost_list.append(acceleration)
                ostatok -= acceleration
            hvost_list.append(ostatok)

        elif ostatok < acc_ar_aceleration[-1]:
            for i in range(ostatok // acceleration):
                hvost_list.append(acceleration)
                ostatok -= acceleration
            hvost_list.append(ostatok)

        acc_ar_deceleration = acc_ar_aceleration.copy()
        acc_ar_deceleration.reverse()
        res_list = acc_ar_aceleration + center_list + acc_ar_deceleration + hvost_list

        print('Разгон - ', acc_ar_aceleration, 'Центральный лист - ', center_list, 'Торможение - ', acc_ar_deceleration,
              'Хвосты - ', hvost_list)
    return res_list, sum(res_list)

if __name__ == '__main__':
    print(list_creator(255, 20, 1000))
