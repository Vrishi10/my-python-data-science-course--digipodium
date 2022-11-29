import pgzrun

WIDTH = 1080
HEIGHT = 500

scr = 0

def gamescr(title, bgcolor='gray', info="Play the Game"):
    screen.fill(bgcolor)
    screen.draw.text(title, center=(WIDTH/2, HEIGHT/2), fontsize=100, color='white',
             align='center')
    screen.draw.text(info, center=(WIDTH/2, HEIGHT/2+100), fontsize=50,
           color='white', align='center')


def draw():
    if scr == 0:
        gamescr('Amazing Game',bgcolor='black', 'Press space to Start')
    elif scr == 1:
        gamescr(bgcolor='green', title='Game is Running')
    elif scr == 2:
        gamescr('Game Over', info='Go Home')
        

def update():
    global scr
    if keyboard.space and scr == 0:
        scr = 1
    elif keyboard.escape and scr == 1:
        scr = 2
    elif keyboard.space and scr == 2:
        scr = 0
    print

pgzrun.go()