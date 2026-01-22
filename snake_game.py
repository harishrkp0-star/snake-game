import curses
import random

screen = curses.initscr()
curses.curs_set(0)
height, width = screen.getmaxyx()
win = curses.newwin(height, width, 0, 0)
win.keypad(1)
win.timeout(100)

snake = [[height//2, width//4], [height//2, width//4-1], [height//2, width//4-2]]
food = [height//2, width//2]
win.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key
    head = snake[0][:]
    if key == curses.KEY_DOWN:
        head[0] += 1
    elif key == curses.KEY_UP:
        head[0] -= 1
    elif key == curses.KEY_LEFT:
        head[1] -= 1
    elif key == curses.KEY_RIGHT:
        head[1] += 1

    snake.insert(0, head

    if head == food:
        food = None
        while food is None:
            nf = [random.randint(1, height-2), random.randint(1, width-2)]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    if head[0] in [0, height] or head[1] in [0, width] or head in snake[1:]:
        curses.endwin()
        print("Game Over! Score:", len(snake)-3)
        break

    win.addch(head[0], head[1], curses.ACS_CKBOARD)
