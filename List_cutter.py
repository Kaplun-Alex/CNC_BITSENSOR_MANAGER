from time import sleep
def client_worker2():
    max_speed = 102
    run_speed = 8
    cor = 227
    print(cor)
    half_cor = cor/2
    print(half_cor)
    hvost = half_cor % run_speed
    print(hvost)
    half_cor = int(half_cor - hvost)
    print(half_cor)
    mes_list = []
    right_now_speed = 0
    mes_list.append(0)

    while run_speed != half_cor:
        while (sum(mes_list)) != half_cor:
            print('Сумма робочого списку - ', sum(mes_list))
            print('Швидкість прискорення - ', run_speed)
            print('Швидкысть прямо зараз - ', right_now_speed)
            print('Перший if - ', (sum(mes_list) + right_now_speed + run_speed))
            if (sum(mes_list) + right_now_speed + run_speed*2) == int(half_cor):
                right_now_speed = right_now_speed + run_speed
                mes_list.append(right_now_speed+run_speed)
                print(mes_list)

            elif (sum(mes_list) + run_speed*2) == int(half_cor):
                mes_list.append(right_now_speed)
                print(mes_list)

            else:
                right_now_speed = right_now_speed + run_speed
                mes_list.append(right_now_speed)
                print(mes_list)
            print('Сумма списку результату - ', sum(mes_list))
            print('Точка координат кінця - ', int(half_cor))
            sleep(0.05)

    return mes_list

# s = s0 + v0 * t + a * t**2
# a * t**2 = s - s0 - v0
#



client_worker2()
