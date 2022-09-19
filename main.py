import random
import math
from tkinter import *
from tkinter import messagebox

GAME_WIDTH = 700
GAME_HEIGHT = 600
ROW_BALLS = 6
COLUMN_BALLS = 7
COLOR_FIRST = "black"
COLOR_BALL = ["red", "green"]
x = random.choice(COLOR_BALL)
count = 0


class Empty_Balls:

    def __init__(self, canvas_board, canvas_ball):

        self.empty_ball = None
        self.canvas_board = canvas_board
        self.canvas_ball = canvas_ball
        self.upper_ball = None

    def create_empty_balls(self):
        for j in range(ROW_BALLS):
            for i in range(COLUMN_BALLS):
                self.empty_ball = self.canvas_board.create_oval(i * (GAME_WIDTH / 7), j * (GAME_HEIGHT / 6),
                                                                i * (GAME_WIDTH / 7) + GAME_WIDTH / 7,
                                                                j * (GAME_HEIGHT / 6) + GAME_HEIGHT / 6,
                                                                fill=COLOR_FIRST, width=5, outline="black",
                                                                tag="empty_ball{}{}".format(j, i))

    def above_ball(self):
        self.canvas_ball.bind('<Motion>', self.above_ball_move)
        self.canvas_ball.bind('<Button-1>', self.click_ball)
        self.upper_ball = self.canvas_ball.create_oval(0, 0, 100, 100, fill=x)

    def above_ball_move(self, e):
        cx = self.canvas_ball.winfo_pointerx() - self.canvas_ball.winfo_rootx()
        if 0 <= cx <= 600:
            if cx <= 50:
                cx = 0
            self.canvas_ball.coords(self.upper_ball, int(math.ceil(cx / 100.0)) * 100, 0,
                                    int(math.ceil(cx / 100.0)) * 100 + 100, 100)

    def click_ball(self, e):
        pos_ball = self.canvas_ball.coords(self.upper_ball)
        global x

        for i in range(6):
            if self.canvas_board.itemcget("empty_ball{}{}".format(5 - i, int(pos_ball[0] / 100)),
                                              "fill") == COLOR_FIRST:
                self.canvas_board.itemconfigure("empty_ball{}{}".format(5 - i, int(pos_ball[0] / 100)), fill=x)
                break
        if x == "red":
            x = "green"
        elif x == "green":
            x = "red"
        self.canvas_ball.itemconfigure(self.upper_ball, fill=x)
        self.check_winner()

    def check_winner(self):

        for j in range(ROW_BALLS):
            for i in range(COLUMN_BALLS - 3):
                color = self.canvas_board.itemcget("empty_ball{}{}".format(j, i), "fill")
                color1 = self.canvas_board.itemcget("empty_ball{}{}".format(j, i + 1), "fill")
                color2 = self.canvas_board.itemcget("empty_ball{}{}".format(j, i + 2), "fill")
                color3 = self.canvas_board.itemcget("empty_ball{}{}".format(j, i + 3), "fill")

                if (color == color1 == color2 == color3) and color != COLOR_FIRST:
                    messagebox.showinfo('GAME OVER', color.upper() + ' is winner')

                    quit()

        for j in range(ROW_BALLS - 3):
            for i in range(COLUMN_BALLS):
                color = self.canvas_board.itemcget("empty_ball{}{}".format(j, i), "fill")
                color1 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 1, i), "fill")
                color2 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 2, i), "fill")
                color3 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 3, i), "fill")

                if (color == color1 == color2 == color3) and color != COLOR_FIRST:
                    messagebox.showinfo('GAME OVER', color.upper() + ' is winner')
                    quit()

        for j in range(ROW_BALLS - 3):
            for i in range(COLUMN_BALLS - 3):
                color = self.canvas_board.itemcget("empty_ball{}{}".format(j, i), "fill")
                color1 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 1, i + 1), "fill")
                color2 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 2, i + 2), "fill")
                color3 = self.canvas_board.itemcget("empty_ball{}{}".format(j + 3, i + 3), "fill")

                if (color == color1 == color2 == color3) and color != COLOR_FIRST:
                    messagebox.showinfo('GAME OVER', color.upper() + ' is winner')
                    quit()

        for j in range(3, ROW_BALLS):
            for i in range(COLUMN_BALLS - 3):
                color = self.canvas_board.itemcget("empty_ball{}{}".format(j, i), "fill")
                color1 = self.canvas_board.itemcget("empty_ball{}{}".format(j - 1, i + 1), "fill")
                color2 = self.canvas_board.itemcget("empty_ball{}{}".format(j - 2, i + 2), "fill")
                color3 = self.canvas_board.itemcget("empty_ball{}{}".format(j - 3, i + 3), "fill")

                if (color == color1 == color2 == color3) and color != COLOR_FIRST:
                    messagebox.showinfo('GAME OVER', color.upper() + ' is winner')
                    quit()

        global count
        count = 0
        for j in range(ROW_BALLS):
            for i in range(COLUMN_BALLS):
                color = self.canvas_board.itemcget("empty_ball{}{}".format(j, i), "fill")
                if color != COLOR_FIRST:
                    count += 1
            if count == 42:
                messagebox.showinfo('GAME OVER', 'Tie!')
                quit()


window = Tk()
window.title("Connect 4")
window.resizable(False, False)

frame = Frame(window)
frame.pack()

canvas_upper_ball = Canvas(frame, height=GAME_HEIGHT / 6, width=GAME_WIDTH, bg="blue", highlightthickness=0)
canvas_upper_ball.grid(row=0, column=0)

canvas_game = Canvas(frame, height=GAME_HEIGHT, width=GAME_WIDTH, bg="blue", highlightthickness=0)
canvas_game.grid(row=1, column=0)

empty_balls = Empty_Balls(canvas_game, canvas_upper_ball)
empty_balls.create_empty_balls()
empty_balls.above_ball()

window.update()

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
window_height = window.winfo_height()
window_width = window.winfo_width()

height_mid = int((screen_height - window_height) / 2)
width_mid = int((screen_width - window_width) / 2)

window.geometry("{}x{}+{}+{}".format(window_width, window_height, width_mid, height_mid))

window.mainloop()
