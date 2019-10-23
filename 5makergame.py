# ！/usr/bin/python3
# -*-coding=utf-8-*-

import matplotlib.pyplot as plt
import tkinter.messagebox as tkm

chessboard = 20
chess_place = {}
turn_now = "k"
turn_after = "w"
win = 0


def win_or(now_x, now_y):
    """
    判断赢家是否存在
    :param now_x: 最后点击的坐标X
    :param now_y: 最后点击的坐标Y
    :return: 胜利者的颜色(字符)
    """
    global win
    now_x_s, now_y_s = now_x, now_y
    pos_y = 0
    pos_x = 0
    pos_q = 0
    pos_e = 0

    count = 0
    # up
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_y += 1
        else:
            break
        now_y_s += 1
        count += 1

    # down
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_y += 1
        else:
            break
        now_y_s -= 1
        count += 1

    # left
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_x += 1
        else:
            break
        now_x_s -= 1
        count += 1

    # right
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_x += 1
        else:
            break
        now_x_s += 1
        count += 1

    # left_up
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_q += 1
        else:
            break
        now_y_s += 1
        now_x_s -= 1
        count += 1

    # left_down
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_q += 1
        else:
            break
        now_y_s -= 1
        now_x_s += 1
        count += 1

    # right_up
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_e += 1
        else:
            break
        now_y_s += 1
        now_x_s += 1
        count += 1

    # right_down
    count = 0
    now_x_s, now_y_s = now_x, now_y
    while (now_x_s, now_y_s) in chess_place and count < 6:
        if chess_place[(now_x, now_y)] == chess_place[(now_x_s, now_y_s)]:
            pos_e += 1
        else:
            break
        now_y_s -= 1
        now_x_s -= 1
        count += 1

    if pos_y >= 6 or pos_x >= 6 or pos_q >= 6 or pos_e >= 6:
        win = "黑棋" if turn_now == "k" else "白棋"

    return win


def on_press(event):
    """
    鼠标交互动作
    """
    global turn_now, turn_after
    if win == 0:
        moses_x = int(round(event.xdata))
        moses_y = int(round(event.ydata))
        marke_on(moses_x, moses_y)


def marke_on(moses_x, moses_y):
    """
    棋子标记
    :param moses_x: 点击的坐标X
    :param moses_y: 点击的坐标Y
    """
    global turn_now, turn_after
    if (moses_x, moses_y) in chess_place and chess_place[(moses_x, moses_y)] == " ":
        ax.plot(moses_x, moses_y, 'o', markersize=(40 - chessboard), markeredgecolor=(0, 0, 0),
                markerfacecolor=turn_now,
                markeredgewidth=2)
        chess_place[(moses_x, moses_y)] = turn_now
        count_mark("black" if turn_after == "k" else "white", 3)
        fig.canvas.draw()
        turn_change(moses_x, moses_y)


def turn_change(moses_x, moses_y):
    """
    交换颜色
    :param moses_x: 点击的坐标X
    :param moses_y: 点击的坐标Y
    """
    global turn_now, turn_after
    if win_or(moses_x, moses_y) in ("黑棋", "白棋"):
        tkm.showinfo('胜利！', '%s是胜利者哦！' % win)
        # exit()
        plt.close()
        main()
    turn_now, turn_after = turn_after, turn_now


def chess_place_def():
    """
    初始化棋盘
    """
    global chess_place
    for y in range(chessboard):
        for x in range(chessboard):
            chess_place[(x, y)] = " "


def draw_chessboard():
    """
    画出棋盘
    """
    global ax, fig
    fig = plt.figure(figsize=[8, 8])
    fig.patch.set_facecolor((1, 1, 0.8))
    ax = fig.add_subplot(111)
    for x in range(chessboard):
        ax.plot([x, x], [0, chessboard - 1], 'k')
    for y in range(chessboard):
        ax.plot([0, chessboard - 1], [y, y], 'k')
    ax.set_position([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_xlim(-1, chessboard)
    ax.set_ylim(-1, chessboard)


def main():
    global win
    win = 0
    draw_chessboard()
    chess_place_def()
    # print(chess_place)
    # ===========
    count_mark("5-maker-game", -2)
    # ===========
    fig.canvas.mpl_connect("button_press_event", on_press)
    plt.show()


def count_mark(title, lift):
    plt.text(9.5 + lift, 19.5, f"{title}", size=10, rotation=0.,
             ha="center", va="center",
             bbox=dict(boxstyle="round",
                       ec=(0, 0, 0),
                       fc=(1, 1, 1),
                       )
             )


main()
