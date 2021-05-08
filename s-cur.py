import numpy as np

if __name__ == "__main__":

    q0 = 0.
    q1 = 200.
    v0 = 1.
    v1 = 5.
    v_max = 20.
    a_max = 15.
    j_max = 100
    Tj1 = 1.
    Ta = 1.
    Tj2 = 1.
    Td = 0.
    Tv = 0.
    ACCELERATION_ID = 0
    SPEED_ID = 1
    POSITION_ID = 2



    T = 5
    a_lim_a = j_max*Tj1
    a_lim_d = -j_max*Tj2
    v_lim = v0 + (Ta-Tj1)*a_lim_a

    def trajectory(t):

        if 0 <= t < Tj1:
            a = j_max*t
            v = v0 + j_max*(t**2)/2
            q = q0 + v0*t + j_max*(t**3)/6

        elif Tj1 <= t < Ta - Tj1:
            a = a_lim_a
            v = v0 + a_lim_a*(t-Tj1/2)
            q = q0 + v0*t + a_lim_a*(3*(t**2) - 3*Tj1*t + Tj1**2)/6

        elif Ta-Tj1 <= t < Ta:
            tt = Ta - t

            a = j_max*tt
            v = v_lim - j_max*(tt**2)/2
            q = q0 + (v_lim+v0)*Ta/2 - v_lim*tt + j_max*(tt**3)/6

            # Constant velocity phase
        elif Ta <= t < Ta + Tv:
            a = 0
            v = v_lim
            q = q0 + (v_lim+v0)*Ta/2 + v_lim*(t-Ta)

            # Deceleration phase
        elif T - Td <= t < T-Td+Tj2:
            tt = t-T+Td
            a = -j_max*tt
            v = v_lim - j_max*(tt**2)/2
            q = q1 - (v_lim+v1)*Td/2 + v_lim*tt -\
            j_max*(tt**3)/6

        elif T-Td+Tj2 <= t < T-Tj2:
            tt = t-T+Td
            a = a_lim_d
            v = v_lim + a_lim_d*(tt-Tj2/2)
            q = q1 - (v_lim+v1)*Td/2 + v_lim*tt +\
            a_lim_d*(3*(tt**2) - 3*Tj2*tt + Tj2**2)/6

        elif T-Tj2 <= t < T:
            tt = T-t
            a = -j_max*tt
            v = v1 + j_max*(tt**2)/2
            q = q1 - v1*tt - j_max*(tt**3)/6

        else:
            a = 0
            v = v1
            q = q1

        point = np.zeros((3,), dtype=np.float32)
        point[ACCELERATION_ID] = a
        point[SPEED_ID] = v
        point[POSITION_ID] = q
        print(point)

    for i in range(1000):
        trajectory(i/10)


'''
Tj1     --- non-zero constant jerk period while accelerating
Ta      --- total acceleration period time
Tj2     --- non-zero constant jerk period while decelerating
Td      --- total deceleration time
Tv      --- constant speed time
'''