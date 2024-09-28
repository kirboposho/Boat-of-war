#pgzero
import random

WIDTH = 1075
HEIGHT = 525

TITLE = "Boat of War"
FPS = 30

nivel = Actor("bonus", (450, 263))
nivel2 = Actor("bonus", (680, 263))
play = Actor("play", (538, 263))
play2= Actor("play",(538,350))

flecha = Actor("flecha", (1000, 480))
botonx = Actor("x", (40, 40))
        
boton1= Actor("bonus", (138, 300))
boton2= Actor("bonus", (538, 300))
boton3= Actor("bonus", (900, 300))

a = random.randint(800,1050)
b = random.randint(0, 520)
barco = Actor("barquito", (a, b))
crew = Actor("crew", (a,b))

n = random.randint(800,1050)
m = random.randint(0, 520)
ruina = Actor("ruina", (n, m))
fuego = Actor("fire", (n, m))
fuego1 = Actor("fire1", (n, m))

c = random.randint(800,1050)
v = random.randint(0, 520)
ruina1 = Actor("ruina1", (c, v))

ship = Actor('ship', (300, 360))
ship.health = 100
ship.attack = 10

fondo = Actor("fondo")

enemies = []
bullet = []
count = 0
pc = 0
pi = 0


mode = "menu"


type1 = Actor("type1",(100,200))
type2 = Actor("type2",(300,200))
type3 = Actor("type3",(500,200))
type4 = Actor("type4",(300,400))

for i in range(7):
    x = random.randint(1075, 1200)
    y = random.randint(0, 520)
    enemy = Actor("enemy",(x, y))
    enemy.speed = random.randint(10, 50)
    enemies.append(enemy)
    enemy.health = random.randint(10,20)
    enemy.attack = random.randint(15, 25)
    
def draw():
    if mode == "game":
        fondo.draw()
        ship.draw()
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(bullet)):
            bullet[i].draw()
        screen.draw.text(count ,center = (50,10), color ="white", fontsize= 36)
        screen.draw.text(ship.health ,center = (50,90), color ="white", fontsize= 36)
    
    if mode == "menu":
        fondo.draw()
        play.draw()
        screen.draw.text("BOAT OF WAR",center = (538,40), color ="black", fontsize= 36)
        screen.draw.text("Psychology EDITION",center = (538,100), color ="black", fontsize= 36)
    
    elif mode == "menu3":
        fondo.draw()
        screen.draw.text("Elige Tu Barco",center = (300,100), color ="white", fontsize= 36)
        type1.draw()
        type2.draw()
        type3.draw()
        type4.draw()
        barco.draw()
        ruina.draw()
        ruina1.draw()
        fuego.draw()
        fuego1.draw()
        crew.draw()
        
    elif mode == "menu2":    
        fondo.draw()
        nivel.draw()
        #nivel2.draw()
        screen.draw.text("Nivel 1: Medio punto",center = (450, 263), color ="black", fontsize= 20)
        #screen.draw.text("Nivel 2",center = (680, 263), color ="black", fontsize= 40)
        
    elif mode == "end":
        screen.fill("black")
        screen.draw.text("¡Preguntas!", center = (538, 263), color = "white", fontsize = 60)
        play2.draw()
        
    elif mode == "p1":
        screen.fill("black")
        screen.draw.text("¿Cuánto es 33 + 77?", center = (538, 50), color = "white", fontsize = 60)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("110", center = (138, 300), color = "white", fontsize = 60)
        screen.draw.text("113", center = (538, 300), color = "white", fontsize = 60)
        screen.draw.text("100", center = (900, 300), color = "white", fontsize = 60)
        
    elif mode == "rp1":
        screen.fill("black")
        screen.draw.text("¡Respuesta correcta!", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "rip1":
        screen.fill("black")
        screen.draw.text("Respuesta incorrecta :(", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "p2":
        screen.fill("black")
        screen.draw.text("¿Cuál es la capital de Estados Unidos?", center = (538, 50), color = "white", fontsize = 60)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("New York", center = (138, 300), color = "white", fontsize = 30)
        screen.draw.text("Washington D. C.", center = (538, 300), color = "white", fontsize = 25)
        screen.draw.text("Florida", center = (900, 300), color = "white", fontsize = 30)
        
    elif mode == "rp2":
        screen.fill("black")
        screen.draw.text("¡Respuesta correcta!", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
    
    elif mode == "rip2":
        screen.fill("black")
        screen.draw.text("Respuesta incorrecta :(", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
    
    elif mode == "p3":
        screen.fill("black")
        screen.draw.text("¿las técnicas proyectivas son subjetivas?", center = (538, 50), color = "white", fontsize = 60)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("DEPENDE", center = (138, 300), color = "white", fontsize = 35)
        screen.draw.text("SI", center = (538, 300), color = "white", fontsize = 60)
        screen.draw.text("NO", center = (900, 300), color = "white", fontsize = 60)
    
    elif mode == "rp3":
        screen.fill("black")
        screen.draw.text("¡Respuesta correcta!", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "rip3":
        screen.fill("black")
        screen.draw.text("Respuesta incorrecta :(", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "p4":
        screen.fill("black")
        screen.draw.text("¿En que año salió minecraft CLASSIC?", center = (538, 50), color = "white", fontsize = 60)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("2011", center = (138, 300), color = "white", fontsize = 60)
        screen.draw.text("2009", center = (538, 300), color = "white", fontsize = 60)
        screen.draw.text("2007", center = (900, 300), color = "white", fontsize = 60)
    
    elif mode == "rp4":
        screen.fill("black")
        screen.draw.text("¡Respuesta correcta!", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
    
    elif mode == "rip4":
        screen.fill("black")
        screen.draw.text("Respuesta incorrecta :(", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw() 
    
    elif mode == "p5":
        screen.fill("black")
        screen.draw.text("¿En que año salió MINECRAFT 1.0?", center = (538, 50), color = "white", fontsize = 60)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("2009", center = (138, 300), color = "white", fontsize = 60)
        screen.draw.text("2007", center = (538, 300), color = "white", fontsize = 60)
        screen.draw.text("2011", center = (900, 300), color = "white", fontsize = 60)
        
    elif mode == "rp5":
        screen.fill("black")
        screen.draw.text("¡Respuesta correcta!", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "rip5":
        screen.fill("black")
        screen.draw.text("Respuesta incorrecta :(", center = (538, 263), color = "white", fontsize = 60)
        flecha.draw()
        
    elif mode == "final":
        screen.fill("black")
        screen.draw.text("¡Felicitaciones!", center = (538, 263), color = "white", fontsize = 60)
        screen.draw.text(pc , center = (50, 50), color = "white", fontsize = 40)
        screen.draw.text(pi , center = (50, 120), color = "white", fontsize = 40)
        flecha.draw()
    
    elif mode == "todoonada":
        screen.fill("black")
        screen.draw.text("¿El test de la familia evalúa violencia familiar?", center = (538, 50), color = "white", fontsize = 40)
        boton1.draw()
        boton2.draw()
        boton3.draw()
        screen.draw.text("Si", center = (138, 300), color = "white", fontsize = 60)
        screen.draw.text("No", center = (538, 300), color = "white", fontsize = 60)
        screen.draw.text("Depende", center = (900, 300), color = "white", fontsize = 50)
       
def on_mouse_move(pos):
    ship.pos = pos

def on_mouse_down(button, pos):
    global mode, ship, bullet, pc, pi
    if mode == "menu3" and type1.collidepoint(pos):
        ship.image = "type1"
        mode = "game"
    
    elif mode == "menu3" and type2.collidepoint(pos):
        ship.image = "type2"
        mode = "game"
    
    elif mode == "menu3" and type3.collidepoint(pos):
        ship.image = "type3"
        mode = "game"
    
    elif mode == "menu3" and type4.collidepoint(pos):
        ship.image = "type4"
        mode = "game"
    
    elif mode == "menu" and play.collidepoint(pos):
        mode = "menu2"
    
    elif mode == "menu2" and nivel.collidepoint(pos):
        mode = "menu3"
    
    elif mode == "end" and play2.collidepoint(pos):
        mode = "p1"
    
    
    
    elif mode == "p1" and boton1.collidepoint(pos):
        mode = "rp1"
        pc = pc + 1
    
    elif mode == "p1" and boton2.collidepoint(pos):
        mode = "rip1"
        pi += 1
    
        
    elif mode == "p1" and boton3.collidepoint(pos):
        mode = "rip1"
        pi += 1
        
    elif mode == "rp1" and flecha.collidepoint(pos):
        mode = "p2"
    
    elif mode == "rip1" and flecha.collidepoint(pos):
        mode = "p2"
        
    elif mode == "p2" and boton1.collidepoint(pos):
        mode = "rip2"
        pi += 1
        
    
    elif mode == "p2" and boton2.collidepoint(pos):
        mode = "rp2"
        pc = pc + 1
        
                
    elif mode == "p2" and boton3.collidepoint(pos):
        mode = "rip2"
        pi += 1
        
    elif mode == "rp2" and flecha.collidepoint(pos):
        mode = "p3"
        
    elif mode == "rip2" and flecha.collidepoint(pos):
        mode = "p3"
    
    elif mode == "p3" and boton1.collidepoint(pos):
        mode = "rip3"
        pi += 1
        
    elif mode == "p3" and boton2.collidepoint(pos):
        mode = "rip3"
        pi += 1
        
    elif mode == "p3" and boton3.collidepoint(pos):
        mode = "rp3"
        pc = pc + 1
        
    elif mode == "rp3" and flecha.collidepoint(pos):
        mode = "p4"
    
    elif mode == "rip3" and flecha.collidepoint(pos):
        mode = "p4"
    
    elif mode == "p4" and boton1.collidepoint(pos):
        mode = "rip4"
        pi += 1
    
    elif mode == "p4" and boton2.collidepoint(pos):
        mode = "rp4"
        pc = pc + 1
        
    elif mode == "p4" and boton3.collidepoint(pos):
        mode = "rip4"
        pi += 1
        
    elif mode == "rp4" and flecha.collidepoint(pos):
        mode = "p5"
    
    elif mode == "rip4" and flecha.collidepoint(pos):
        mode = "p5"
        
    elif mode == "p5" and boton1.collidepoint(pos):
        mode = "rip5"
        pi += 1
        
    elif mode == "p5" and boton2.collidepoint(pos):
        mode = "rip5"
        pi += 1
        
    elif mode == "p5" and boton3.collidepoint(pos):
        mode = "rp5"
        pc = pc + 1
        
    elif mode == "rp5" and flecha.collidepoint(pos):
        mode = "final"
    
    elif mode == "rip5" and flecha.collidepoint(pos):
        mode = "final"
        
    elif mode == "final" and pc == 5 and flecha.collidepoint(pos):
        mode = "todoonada"
    
    elif mode == "todoonada" and boton1.collidepoint(pos):
        mode == "gameover"
    
    elif mode == "todoonada" and boton2.collidepoint(pos):
        mode == "victoria"
    
    elif mode == "todoonada" and boton3.collidepoint(pos):
        mode == "gameover"
        
    
    if mode == "game" and button == mouse.LEFT:
        bullets = Actor("missiles")
        bullets.pos = ship.pos
        bullet.append(bullets)
    
    
def new_enemy():
    x = 1075
    y = random.randint(0, 520)
    enemy = Actor("enemy",(x, y))
    enemy.speed = random.randint(10, 30)
    enemies.append(enemy)
    
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].x > 10:
            enemies[i].x = enemies[i].x - enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

            
def collisions():
    global mode, count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            ship.health -= enemy.attack
            if ship.health <= 0:
                mode = "end"
        for j in range(len(bullet)):
            if bullet[j].colliderect(enemies[i]):
                enemies.pop(i)
                bullet.pop(j)
                new_enemy()
                count += 1
                break

def update(dt):
    global mode, count, bullet, pc, pi
    if mode == "game":
        enemy_ship()
        collisions()
    
    if mode == "game" and ship.image == "type1":
            for i in range(len(bullet)):
                if bullet[i].x < 0:
                    bullet.pop(i)
                    break
                else:
                    bullet[i].x = bullet[i].x + 50
    
    elif mode == "game" and ship.image == "type2":
            for i in range(len(bullet)):
                if bullet[i].x < 0:
                    bullet.pop(i)
                    break
                else:
                    bullet[i].x = bullet[i].x + 30
                    
    elif mode == "game" and ship.image == "type3":
            for i in range(len(bullet)):
                if bullet[i].x < 0:
                    bullet.pop(i)
                    break
                else:
                    bullet[i].x = bullet[i].x + 65
    
    elif mode == "game" and ship.image == "type4":
            for i in range(len(bullet)):
                if bullet[i].x < 0:
                    bullet.pop(i)
                    break
                else:
                    bullet[i].x = bullet[i].x + 25
