def full_mes(cor_dict, go_mes):
    full = []
    x_speed = cor_dict[0]
    y_speed = cor_dict[1]
    z_speed = cor_dict[2]
    a_speed = cor_dict[3]
    cor_dict_len = cor_dict[5]
    for i in range(cor_dict_len):
        mes = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Проверяем x
        if int(go_mes[1]) > 0:
            mes[9] = x_speed[i]
        elif int(go_mes[1]) < 0:
            if x_speed[i] == 0:
                mes[9], mes[10], mes[11], mes[12] = 0, 0, 0, 0
            elif x_speed[i] == 1:
                mes[9], mes[10], mes[11], mes[12] = 255, 255, 255, 255
            else:
                mes[9] = 256-x_speed[i]
                mes[10], mes[11], mes[12] = 255, 255, 255
        else:
            pass

        # Проверяем y

        if int(go_mes[2]) > 0:
            mes[13] = y_speed[i]
        elif int(go_mes[2]) < 0:
            if y_speed[i] == 0:
                mes[13], mes[14], mes[15], mes[16] = 0, 0, 0, 0
            elif y_speed[i] == 1:
                mes[13], mes[14], mes[15], mes[16] = 255, 255, 255, 255
            else:
                mes[13] = 256-y_speed[i]
                mes[14], mes[15], mes[16] = 255, 255, 255
        else:
            pass

        # Проверяем z

        if int(go_mes[3]) > 0:
            mes[17] = z_speed[i]
        elif int(go_mes[2]) < 0:
            if z_speed[i] == 0:
                mes[17], mes[18], mes[19], mes[20] = 0, 0, 0, 0
            elif z_speed[i] == 1:
                mes[17], mes[18], mes[19], mes[20] = 255, 255, 255, 255
            else:
                mes[17] = 256-z_speed[i]
                mes[18], mes[19], mes[20] = 255, 255, 255
        else:
            pass

        # Проверяем z
        if int(go_mes[4]) > 0:
            mes[21] = a_speed[i]
        elif int(go_mes[2]) < 0:
            if a_speed[i] == 0:
                mes[21], mes[22], mes[23], mes[24] = 0, 0, 0, 0
            elif a_speed[i] == 1:
                mes[21], mes[22], mes[23], mes[24] = 255, 255, 255, 255
            else:
                mes[21] = 256-a_speed[i]
                mes[22], mes[23], mes[24] = 255, 255, 255
        else:
            pass

        full.append(mes)
    return full


if __name__ == '__main__':
    item = {0: [1, 10, 10, 10, 10, 5], 1: [1, 20, 20, 20, 20, 10],
            2: [1, 15, 15, 15, 15, 8], 3: [1, 5, 5, 5, 5, 3], 5: 6}
    go = ['<COR>', '9937', '03331', '0333317', '033971', '<COR>']
    print(full_mes(item, go))