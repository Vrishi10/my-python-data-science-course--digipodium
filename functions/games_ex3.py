import pgzrun
from random import randint

HEIGHT = 600
WIDTH  = 1200

p = Actor('ironman', (WIDTH//2 , HEIGHT//2))
c = Actor('cookie_img',(randint(0,WIDTH), randint(0,HEIGHT)))

title = "IRON-MAN GAME"
score = 0
#music.play('bg')
music.set_volume(0.2)

def draw():
    screen.fill('white')
    screen.draw.text(title,(10,10), center= (WIDTH//2,30), fontsize=50, color = 'black',
        align = 'center', shadow=(.1,2), scolor='red')
    screen.draw.text(f'score: {score}', (10,10), fontsize=40, color = 'black')
    p.draw()
    c.draw()

def p_move():
    if keyboard.right and p.right < WIDTH :
        p.x += 10
        p.angle = -60
    elif keyboard.left and p.left > 0:
        p.x -= 10
        p.angle = 60
    else:
        p.angle = 0
    if keyboard.up and p.top > 0:
        p.y -= 10
    if keyboard.down and p.bottom < HEIGHT:
        p.y += 10

def update():
    global score          #tells python, that we want to change the value of the global variable score...
    p_move()              #function call
    if p.colliderect(c):  #function
        score += 1
        c.pos = (randint(0,WIDTH), randint(0,HEIGHT))
        sounds.s1.play()
    print(p.x , p.y , p.angle)

pgzrun.go()