from random import randint

import pgzrun
from pgzero.actor import Actor

WIDTH = 700
HEIGHT = 500
score = 0 
game_started = False
game_over = False
health_points = 5

spiderman = Actor("spiderman") 
spiderman.pos = (350 , 250)

spider = Actor("spider")
spider.pos = (400,300)

bomb = Actor("bomb")
bomb.pos = (0, -30)

heart1 = Actor("heart")
heart1.pos = (30 , 40)

heart2 = Actor("heart")
heart2.pos =(60, 40)

heart3 = Actor("heart")
heart3.pos = (90 , 40)

heart4 = Actor("heart")
heart4.pos = (120 , 40)

heart5 = Actor("heart")
heart5.pos = (150, 40)

def draw():


  if game_over:
    screen.fill("black")
    screen.blit(("sad") , (150 , 25))
    screen.draw.text(("GAME OVER :("), center = (350 , 440))
    screen.draw.text(("Press R To Restart "), center = (350 , 460))
    screen.draw.text(("Press M To main menu "), center = (350 , 480))
    screen.draw.text("Score: " + str(score), center = ( WIDTH/2 ,60), fontsize = 50, color = ("white"))

  elif game_started:

    screen.fill("gray")
    screen.blit(("city"), (0 , 0))
    spider.draw()
    spiderman.draw()
    if health_points==5:
      heart1.draw()
      heart2.draw()
      heart3.draw()
      heart4.draw()
      heart5.draw()
    if health_points==4: 
      heart1.draw()
      heart2.draw()
      heart3.draw()
      heart4.draw()
    if health_points==3:
      heart1.draw()
      heart2.draw()
      heart3.draw()
    if health_points==2:
      heart1.draw()
      heart2.draw()
    if health_points==1:
      heart1.draw()
    bomb.draw()
    screen.draw.text("Score: " + str(score), center = (100,10), fontsize = 20, color = ("white"))
   

  else: 
    screen.fill("red")
    screen.blit(("spidermanlogo"), (120,-20))
    screen.draw.text(("Press T to begin"), center = (350 , 300),fontsize = 70 , color = ("white"))
    screen.draw.text(("Spiderman X"), center = (350 , 220),fontsize = 120 , color = ("white"))
  
def random_bomb():
  bomb.x = randint (20 , (WIDTH - 20))
  bomb.y = -30
  
def random_spider():
  spider.pos=(randint(30, WIDTH-30) , randint(30 , HEIGHT-30))

def restart():
  global game_started , game_over,   score , health_points
  game_started = False
  game_over = False  
  score = 0
  health_points = 5

def restart_join():
  global game_started , game_over,   score , health_points
  game_started = True
  game_over = False  
  score = 0
  health_points = 5
  
def update():
  global score , game_started, game_over, health_points 
  if spiderman.colliderect(spider):
    random_spider()
    score += 1 
  if game_started:
    if spiderman.colliderect(bomb):
      random_bomb()
      health_points -=1 
  
  if keyboard.W or keyboard.up:
    spiderman.y -=5
  if keyboard.A or keyboard.left:
    spiderman.x -=5
  if keyboard.S or keyboard.down:
    spiderman.y +=5
  if keyboard.D or keyboard.right:
    spiderman.x +=5

  if keyboard.T:
    game_started = True 
  if keyboard.R:
    restart_join()
  if keyboard.M:
    restart()
  
  if health_points == 0:
    game_over = True

def bajada():
  bomb.y+=7
  if bomb.y > 450:
    random_bomb()

clock.schedule_interval(bajada,0.01)
random_bomb()

pgzrun.go()