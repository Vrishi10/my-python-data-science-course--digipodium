import pgzrun
HEIGHT = 300
WIDTH = 800
p = Actor('ironman',(100,100))
c = Actor('cookie_img')

def draw():
    
    p.draw()
    c.draw()

pgzrun.go()