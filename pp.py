# ut 15
# user_trace = [3.40893471, 2.77686506, 8.05064237, 11.04612921, 5.46584218,
#               2.91463004, 7.05103451, 2.70810727, 3.47526827, 5.85998051,
#               4.80676966, 10.39347239, 6.67049368, 2.3423358, 8.41007532]


# ut 30
# user_trace = [6.23502038, 6.11125975, 4.17925807, 3.5151793, 0.85431899,
#               5.95140593, 7.22433026, 3.98313183, 11.75646594, 8.35798042,
#               9.52533025, 7.18940481, 8.69408943, 7.26268849, 1.89893377,
#               8.58535765, 7.06610116, 4.51934896, 2.75132782, 4.99183181,
#               7.89331531, 9.74161207, 8.9012917, 4.18916812, 0.06191618,
#               1.21115775, 6.5777687, 9.35452416, 9.15837158, 11.00038402]
#
# # ut 45
# user_trace = [7.77889267, 10.02954148, 6.37947325, 6.7403242, 7.14563618,
#               3.14794419, 9.41009813, 12.14628237, 9.31974839, 4.00098241,
#               10.29692747, 5.72681383, 9.30580245, 5.11720758, 4.09135589,
#               4.72085457, 8.49532917, 1.14730011, 5.88609762, 7.21364805,
#               3.62875801, 4.87534886, 5.96972256, 5.03855685, 4.15950294,
#               4.8445524, 5.49409627, 10.39190599, 9.39772993, 8.72855118,
#               6.48761084, 8.3592708, 6.21550379, 5.71240107, 6.12836417,
#               11.91435423, 7.25785642, 13.21108782, 6.2990825, 6.81775282,
#               3.84959488, 2.36563154, 7.3071175, 11.68495776, 6.24751135]
# # ut 60
# user_trace = [11.72691071, 4.43980204, 7.21221502, 10.9542191, 5.62856538,
#               6.67532165, 6.13557998, 0.59671229, 7.0000452, 6.86029441,
#               11.63128066, 5.26422073, 9.06461419, 6.13324674, 6.66833153,
#               0.93632769, 5.07361008, 3.70176765, 5.02571171, 4.73221222,
#               7.82849559, 5.48526117, 11.15964527, 6.43833553, 5.16100054,
#               10.76302037, 11.40189767, 9.610774, 3.15314894, 5.32482398,
#               3.39999032, 8.44136277, 11.45454256, 7.2379687, 3.81368948,
#               4.0600503, 5.83007175, 6.35709246, 6.11973109, 5.75968785,
#               5.92487382, 3.93062237, 8.24342843, 6.84523868, 11.31053082,
#               8.37442415, 3.40136222, 2.71085524, 5.62646588, 8.044235,
#               9.72158495, 11.11439021, 2.7928167, 3.58578861, 10.84291367,
#               5.48596268, 6.61792104, 5.09370773, 2.30167266, 9.20579298]

# ut 120

user_trace = [4.55239743, 7.41071187, 6.6961394, 8.95839566, 9.94515606,
              7.60111791, 6.48932771, 2.48135515, 11.00584741, 6.32729604,
              5.76183675, 7.32451638, 7.00834137, 8.71665494, 12.3664025,
              3.71582718, 6.67601933, 3.37886764, 8.9279235, 4.61152763,
              6.08911516, 4.02591879, 4.83858819, 3.21229411, 5.94391852,
              5.12132102, 1.29536038, 0.68209539, 5.18862086, 3.30116182,
              10.70903785, 5.62951093, 4.33873208, 1.72704296, 3.75726118,
              6.63344609, 8.98954188, 7.32224842, 7.27818524, 5.08158366,
              1.15726961, 6.71062107, 4.81846377, 5.54463701, 7.7854625,
              2.38447124, 5.87956415, 7.07900913, 3.43545778, 9.06183127,
              8.53718762, 9.84650273, 5.22551677, 7.01599084, 3.86869672,
              10.48076624, 4.3491203, 3.0872391, 8.26592422, 3.60946634,
              8.60829837, 7.50284412, 6.29321858, 8.18856385, 4.58905771,
              6.26196034, 7.70557651, 7.45592141, 5.92835043, 1.32114364,
              12.98956156, 5.00826161, 2.36924158, 4.7175187, 6.29788137,
              6.67859333, 2.36638258, 3.75573297, 5.9700184, 3.55956012,
              3.77262404, 10.64935189, 7.81600593, 4.81331424, 8.16768476,
              3.75669823, 5.32905117, 7.89783758, 6.55040714, 0.06582749,
              5.40575305, 6.60725853, 5.16349211, 7.71757319, 5.49778375,
              3.74664514, 9.38254407, 11.03152287, 9.99253468, 3.34565969,
              9.27705103, 2.01834563, 7.78259146, 10.12439331, 5.17515327,
              8.15494887, 3.97151889, 2.77280136, 7.64231915, 7.97799772,
              9.59845329, 7.4802313, 8.67671439, 8.33285286, 6.06955878,
              8.42581646, 5.83019659, 3.7722565, 3.35303681, 3.58164407]


# Doc file network trace
def read_bw():
    bw = []
    try:
        with open("trace4.txt", "r") as network:
            for i in range(250):
                line = network.readline()
                try:
                    bw.append(float(line.split("\n")[0]))
                except:
                    bw.append(0)
        return bw
    except FileNotFoundError:
        print("Khong the mo file")


def plus_(seg, tx, t, time_step, x):
    seg += time_step * x
    tx += time_step
    t += time_step
    return seg, tx, t


def Rebuffer(Buf, video, Q, time_step, t, D, tx, Tb, TB, seg, BW, bitrate):
    while (Buf[video] - Q) <= 0:
        seg, tx, t = plus_(seg, tx, t, time_step, (BW[int(t)] / bitrate))
        Tb += time_step
        TB += time_step
        if Q == 0:
            D += time_step
        if seg >= 1:
            Buf[video] += seg
            seg = 0
            break
        if tx >= user_trace[video]:
            break
    print(f"rebuf video: {video} Tb: {Tb} t: {t}\n")
    return seg, Buf[video], tx, t, TB, D


def BuffThisVideo(Buf, video, Q, time_step, t, tx, seg, BW, bitrate, D, Tb, TB):
    while True:
        seg, tx, t = plus_(seg, tx, t, time_step, (BW[int(t)] / bitrate))
        if (Buf[video] - Q) > 0:
            Q += time_step
        else:
            seg, Buf[video], tx, t, TB, D = Rebuffer(Buf, video, Q, time_step, t, D, tx, Tb, TB, seg, BW, bitrate)
            break
        if tx >= user_trace[video]:
            break
        if seg >= 1:
            Buf[video] += seg
            seg = 0
            break
    return seg, Buf[video], Q, tx, t, TB, D


def BsegandK(t, s, BW, bitrate):
    i = int(t) - 10
    while i < t - 1:
        s += BW[i]
        i = i + 1
    s /= 10
    if s > (2.5 * bitrate):
        Bseg = 2
        K = 12
    elif s > (2 * bitrate):
        Bseg = 3
        K = 7
    elif s > (1.5 * bitrate):
        Bseg = 3
        K = 4
    else:
        Bseg = 4
        K = 7
    # if s > 2.5 * bitrate:
    #     Bseg = 2
    #     K = 7 # 12
    # elif s > 2 * bitrate:
    #     Bseg = 3
    #     K = 7
    # elif s > 1.5 * bitrate:
    #     Bseg = 2  # 3
    #     K = 4
    # else:
    #     Bseg = 2  # 4
    #     K = 5  # 7

    return Bseg, K, s


def main():
    Tb = 0  # thoi gian rebuffer
    TB = 0  # tong thoi gian rebuffer

    D = 0  # Start up delay

    Waste = 0  # tong waste
    Q = 0  # thoi gian chay video hien tai
    tx = 0  # thoi gian xem video hien tai
    Buf = [0 for i in range(31)]  # thoi gian (duoc ?) buffer cua tung video

    Bseg = 2  # gioi han so segment duoc buffer

    K = 4  # so luong next video duoc buffer
    seg = 0.0  # segment = 1 se buffer 1s cho video
    bitrate = 2000.0  # 1000 kb/s
    time_step = 0.001
    video = 0
    # tong_video = 30
    tong_video = 15
    # tong_video = 45
    # tong_video = 60
    s = 0  # tong thoi gian user xem
    t = 0  # thoi gian thuc

    BW = read_bw()
    for i in range(len(user_trace)):
        s += user_trace[i]

    # Proposed
    while t <= 500:
        if t > 10:
            Bseg, K, s = BsegandK(t, s, BW, bitrate)

        # chuyen video
        if tx >= user_trace[video]:
            Waste += (Buf[video] - Q)
            W = (Buf[video] - Q)
            if Buf[video] - Q < Bseg and Buf[video] < 15:
                W += seg
                Waste += seg
                seg = 0
            print(f"video: {video} W: {W} t: {t}\n")
            Q = 0
            tx = 0
            video += 1

        a = 1  # Next video dang duoc buffer
        # user khong xem nua
        if video == tong_video:
            break
        # chon video it buffer nhat de buffer
        elif video < (tong_video - 1):
            i = video + 2
            while i <= video + K and i < tong_video:
                if Buf[video + a] > Buf[i]:
                    a = i - video
                i += 1

        # buffer video hien tai
        if Buf[video] < 15 and video < tong_video and Buf[video] - Q < Bseg:
            seg, Buf[video], Q, tx, t, TB, D = BuffThisVideo(Buf, video, Q, time_step, t, tx, seg, BW, bitrate, D, Tb,
                                                             TB)
            Tb = 0

        # buffer video tiep theo
        elif Buf[video + a] < Bseg and video < tong_video - 1:
            v = 0  # Vi tri cua video dang duoc buffer sau khi chuyen video
            while True:
                seg, tx, t = plus_(seg, tx, t, time_step, (BW[int(t)] / bitrate))
                if Buf[video] - Q > 0:
                    Q += time_step
                # rebuffer trong luc buffer next K video
                else:
                    Tb += time_step
                    TB += time_step
                    if Q == 0:
                        D += time_step
                # chuyen video trong luc buffer next K video
                if seg >= 1:
                    Buf[video + a - v] += seg
                    seg = 0
                    break
                if tx >= user_trace[video]:
                    v += 1
                    if v > a:
                        break
                    Waste += (Buf[video] - Q)
                    W = Buf[video] - Q
                    print(f"video: {video} W: {W} t: {t}\n")
                    Q = 0
                    tx = 0
                    video += 1
                    v += 1
            Tb = 0
        # da buffer het B segment video hien tai va next K video
        else:
            tx += time_step
            t += time_step
            Q += time_step
    print("user_trace: " + str(len(user_trace)))
    print(f"Waste: {Waste} \nTB: {TB} \nTime rebuffer: {TB - D} \nStart-up delay: {D}")


def NextOne():
    B0 = 0  # thoi gian video da duoc buffer video hien tai
    pass


def WaterFall():
    B1 = 0  # thoi gian video da duoc buffer video tiep theo
    B2 = 0  # thoi gian video da duoc buffer video thu 3
    pass


if __name__ == '__main__':
    x = 3  # select ALG
    if x == 3:
        main()
    elif (x == 2):
        pass
    elif (x == 1):
        pass
