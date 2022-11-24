import pgzrun
HEIGHT = 600
WIDTH = 800
p = Actor('ironman',(100,100))
c = Actor('cookie_img')

def draw():
    screen.fill('white')
    p.draw()
    c.draw()
    print('drawing')

def update():
    # print('updating')
    p.x += 3
    p.angle = -10
    if p.x > WIDTH:
        p.x = 0
    # print(f'p.x = {p.x}')
    print(p.x , p.y)
    
pgzrun.go()