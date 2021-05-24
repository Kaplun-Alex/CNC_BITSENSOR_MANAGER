import get_speed_profiile


def speed_x_y_z_a_interpolator(system_speed, acc, x=0, y=0, z=0, a=0):
    x = abs(x)
    y = abs(y)
    z = abs(z)
    a = abs(a)
    """
    нельзя шутить если точки сильно отличаются то скорость второй оси после псевдо интерполяции будет
    запредельной.
    Проверяем по какой оси перемещение больше и повторно заганяем большое смещение в профайл процес
    Послэ этого профайл становится доминирующим. Ну пока так. Хотя это можно было определить на этапе клиента.
    """
    serv_cor = [x, y, z, a]
    cor_dict = {}
    if serv_cor.count(0) == 4:
        pass
    elif serv_cor.count(0) == 3:
        main_cor_val = max(serv_cor)
        index_main_cor_val = serv_cor.index(main_cor_val)
        main_cor_list = get_speed_profiile.list_creator(system_speed, acc, main_cor_val)
        cor_dict[index_main_cor_val] = main_cor_list
        empty_list = [0 for i in range(len(main_cor_list))]
        for i in range(0, 4):
            if serv_cor[i] == 0:
                cor_dict[i] = empty_list
        #return cor_dict
    else:
        main_cor_val = max(serv_cor)
        main_cor_list = get_speed_profiile.list_creator(system_speed, acc, main_cor_val)
        index_main_cor_val = serv_cor.index(main_cor_val)  # индекс наибольшего числа в координатах, подщет %list
        # cor_dict[index_main_cor_val] = main_cor_list  # exz {1: [20, 40, 40, 40, 20]}
        #print(main_cor_val, main_cor_list)
        #print(index_main_cor_val)
        #print(cor_dict)
        main_cor_list.reverse()
        counter = 0
        rez = []
        empty_list = [0 for i in range(len(main_cor_list))]
        for i in range(len(main_cor_list)):
            s = main_cor_list.pop()
            counter += s
            rez.append(counter)
        #print(rez)  # exz  [20, 60, 100, 140, 160]
        percent_list = [(rez[i] * 100) / rez[-1] for i in range(len(rez))]
        #print(percent_list)  # ekz[12.5, 37.5, 62.5, 87.5, 100.0]
        for i in range(0, 4):
            if serv_cor[i] == 0:
                cor_dict[i] = empty_list  # ekz [0, 0, 0, 0, 0] -> len(main cor list)
            else:
                value_of_cor_in = serv_cor[i]
                item_rez = [int((value_of_cor_in * percent_list[i]) / 100) for i in range(len(percent_list))]
                item_cor = []
                item_cor_last = item_rez[0]
                for j in range(len(item_rez) - 1):
                    last = item_rez.pop()
                    most_last = item_rez[-1]
                    item_cor.append(last - most_last)
                item_cor.append(item_cor_last)
                item_cor.reverse()
                cor_dict[i] = item_cor
    cor_dict[5] = len(cor_dict[0])
    return cor_dict

if __name__ == '__main__':
    x_point = 10
    y_point = 10
    z_point = 0
    a_point = 0
    acceleration = 10
    speed = 255
    print(speed_x_y_z_a_interpolator(speed, acceleration, x_point, y_point, z_point, a_point))
