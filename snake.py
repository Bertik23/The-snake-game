import pygame as pg
from random import randint

CERNA = (0,0,0)
BILA = (255,255,255)
MODRA = (0,40,250)
ZELENA = (0,255,0)
CERVENA = (250,0,0)
ZLUTA = (255,255,100)
ORANZOVA = (255,120,0)
ZUZOVA = (241,88,226)
SEDA = (211,198,198)

sirka_okna = 1280//2
vyska_okna = 720

bezime = True
hra = False
menu = True

highscoreFileR = open("highscores.txt","r")
highscore = highscoreFileR.read()
highscoreFileW = open("highscores.txt","w")


score = 0
print(highscore)
if highscore == "":
    highscore = 14
    print(highscore)
class snake:
    def __init__(self,x,y,s,v,barva,smer,UP,DOWN,LEFT,RIGHT,rychlost,had):
        self.x = x
        self.y = y
        self.s = s
        self.rx = s
        self.v = v
        self.ry = v
        self.barva = barva
        self.smer = smer
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.CDP = 60
        self.rychlost = rychlost
        self.clanku = 3
        self.had = had
    def nakreslise(self):
        pg.draw.rect(okno,self.barva, (self.x,self.y,self.s,self.v))
        if self.smer == "U":
                pg.draw.rect(okno,CERNA, (self.x+2,self.y+5,2,2))
                pg.draw.rect(okno,CERNA, (self.x+6,self.y+5,2,2))
                pg.draw.rect(okno,CERVENA, (self.x+4,self.y-2,2,6))
        if self.smer == "D":
                pg.draw.rect(okno,CERNA, (self.x+2,self.y+2,2,2))
                pg.draw.rect(okno,CERNA, (self.x+6,self.y+2,2,2))
                pg.draw.rect(okno,CERVENA, (self.x+4,self.y+6,2,6))
        if self.smer == "L":
                pg.draw.rect(okno,CERNA, (self.x+6,self.y+2,2,2))
                pg.draw.rect(okno,CERNA, (self.x+6,self.y+6,2,2))
                pg.draw.rect(okno,CERVENA, (self.x-2,self.y+4,6,2))
        if self.smer == "R":
                pg.draw.rect(okno,CERNA, (self.x+2,self.y+2,2,2))
                pg.draw.rect(okno,CERNA, (self.x+2,self.y+6,2,2))
                pg.draw.rect(okno,CERVENA, (self.x+6,self.y+4,6,2))
    def pohyb(self):
        #POHYB A CLANKY
        if self.CDP == 0:
            #CLANKY
            clanky.append(clanek(self.x,self.y,self.s,self.v,self.barva,1,self.had))
            #POHYB
            if self.smer == "U":
                self.y -= self.v
            if self.smer == "D":
                self.y += self.v
            if self.smer == "L":
                self.x -= self.s
            if self.smer == "R":
                self.x += self.s
            self.CDP = self.rychlost
            
        #OKRAJE
        if self.x >= sirka_okna:
            self.x = 0
        if self.x < 0:
            self.x = sirka_okna-self.s
        if self.y >= vyska_okna:
            self.y = 60
        if self.y < 60:
            self.y = vyska_okna-self.v
        #ZMENA SMERU
        if u.type == pg.KEYDOWN:
            if u.key == self.UP and self.smer != "D":
                self.smer = "U"
            if u.key == self.DOWN and self.smer != "U":
                self.smer = "D"
            if u.key == self.LEFT and self.smer != "R":
                self.smer = "L"
            if u.key == self.RIGHT and self.smer != "L":
                self.smer = "R"
        #RYCHLOST A ZPOMALENI
        if self.rychlost <= 2:
            self.rychlost = 2
        self.CDP -= 1

class clanek:
    def __init__(self,x,y,s,v,barva,zivoty,had):
        self.x = x
        self.y = y
        self.s = s
        self.rx = s
        self.v = v
        self.ry = v
        self.barva = barva
        self.zivoty = zivoty
        self.had = had
        for had in hadi:
            if self.had == had.had:
                self.zivoty = had.clanku*had.rychlost
    def nakreslise(self):
        pg.draw.rect(okno,self.barva, (self.x,self.y,self.s,self.v))
    def aPohyb(self):
        if self.zivoty <= 0:
            clanky.remove(self)
        self.zivoty -= 1
    def naraz(self):
        global hadi
        global jablka
        global menu
        global bezime
        global hra
        global score
        global highscore
        for had in hadi:
            if had.x == self.x and had.y == self.y:
                if score > int(highscore):
                    highscore = score
                    score = 0
                else:
                    score = 0
                hra = False
                menu = True
                text("Umřel jsi.",CERVENA,font70,sirka_okna/2-font70.size("Umřel jsi.")[0],vyska_okna/2-font70.size("Umřel jsi.")[1])
                pg.display.update()
                pg.time.wait(3000)
                
                hadi = []
                jablka = []
            
class jablko:
    def __init__(self,x,y,s,v,prida,barva):
        self.x = x
        self.y = y
        self.s = s
        self.rx = s
        self.v = v
        self.ry = v
        self.barva = barva
        self.prida = prida
    def nakreslise(self):
        pg.draw.rect(okno,self.barva, (self.x,self.y,self.s,self.v))
    def snezeno(self):
        global score
        for had in hadi:
            if had.x == self.x and had.y == self.y:
                had.clanku += self.prida
                had.rychlost -= 1
                jablka.remove(self)
                score += 1

class mriz:
    def __init__(self,x,y,smer,barva):
        self.x = x
        self.y = y
        self.smer = smer
        self.barva = barva
    def nakreslise(self):
        if self.smer == "V":
            self.s = sirka_okna
            self.v = 1
        if self.smer == "H":
            self.v = vyska_okna
            self.s = 1
        pg.draw.rect(okno,self.barva, (self.x,self.y,self.s,self.v))

class tlacitko:
    def __init__(self,x,y,s,v,barva,tBarva,text,zmizi,event,font):
        self.x = x
        self.y = y
        self.s = s
        self.rx = s
        self.v = v
        self.ry = v
        self.barva = barva
        self.text = text
        self.event = event
        self.zmizi = zmizi
        self.zmacknuto = False
        self.DZ = 1
        self.tBarva = tBarva
        self.font = font
    def nakreslise(self):
        pg.draw.rect(okno,self.barva, (self.x,self.y,self.s,self.v))
        text(self.text,self.tBarva,self.font,self.x+((self.s-self.font.size(self.text)[0])/2),self.y+((self.v-self.font.size(self.text)[1])/2))
    def zmacknuti(self):
        if self.zmizi and self.DZ == 0:
                tlacitka.remove(self)
                self.zmacknuto = False
        self.zmacknuto = False
        if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[0] <= self.x+self.s and pg.mouse.get_pos()[1] <= self.y+self.v and pg.mouse.get_pressed()[0]:
            self.zmacknuto = True
            if self.zmizi:
                self.DZ = 0

def text(text, barva, font, x, y,):
    text1 = font.render(str(text), 1 ,barva)
    okno.blit(text1, (x,y))
        

pg.init()
okno = pg.display.set_mode((sirka_okna,vyska_okna))
pg.display.set_caption("Tha snake game")
hodiny = pg.time.Clock()

font10 = pg.font.Font("Roboto-Regular.ttf",10)
font20 = pg.font.Font("Roboto-Regular.ttf",20)
font30 = pg.font.Font("Roboto-Regular.ttf",30)
font40 = pg.font.Font("Roboto-Regular.ttf",40)
font50 = pg.font.Font("Roboto-Regular.ttf",50)
font60 = pg.font.Font("Roboto-Regular.ttf",60)
font70 = pg.font.Font("Roboto-Regular.ttf",70)
font80 = pg.font.Font("Roboto-Regular.ttf",80)
font90 = pg.font.Font("Roboto-Regular.ttf",90)
font100 = pg.font.Font("Roboto-Regular.ttf",100)

hadi = []


clanky = []

jablka = []

mrize = []

tlacitka = []



a = 0
for i in range(sirka_okna//10):
    mrize.append(mriz(a,60,"H",SEDA))
    a += 10

a = 60
for i in range(vyska_okna//10):
    mrize.append(mriz(0,a,"V",SEDA))
    a += 10

    


while bezime:
    for u in pg.event.get():
        if u.type == pg.QUIT:
            bezime = False
            highscoreFileW.write(str(highscore))
            highscoreFileW.close()
            highscoreFileR.close()

        
    if jablka == []:
        jablka.append(jablko((randint(0,sirka_okna)//10)*10,(randint(60,vyska_okna)//10)*10,10,10,1,CERVENA))

    if len(hadi) > 1 and len(jablka) < 2:
        if randint(0,5) == 0:
            jablka.append(jablko((randint(0,sirka_okna)//10)*10,(randint(60,vyska_okna)//10)*10,10,10,3,ORANZOVA))
            jablka.append(jablko((randint(0,sirka_okna)//10)*10,(randint(60,vyska_okna)//10)*10,10,10,1,CERVENA))
        else:
            jablka.append(jablko((randint(0,sirka_okna)//10)*10,(randint(60,vyska_okna)//10)*10,10,10,1,CERVENA))
            
        

        
    okno.fill(BILA)

    if menu:
        tlacitka.append(tlacitko(sirka_okna/2-100,vyska_okna/2-50,200,100,ZELENA,CERNA,"1 Hráč",True,"1P",font50))
        tlacitka.append(tlacitko(sirka_okna/2-100,(vyska_okna/2-50)+110,200,100,ZELENA,CERNA,"2 Hráči",True,"2P",font50))
        for tlacidlo in tlacitka:
            tlacidlo.nakreslise()
            tlacidlo.zmacknuti()
            if tlacidlo.zmacknuto == True:
                if tlacidlo.event == "1P":
                    hadi.append(snake(0,60,10,10,ZELENA,"D",pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT,15,"zeleny"))
                    menu = False
                    hra = True
                    
                    len(hadi)
                if tlacidlo.event == "2P":
                    hadi.append(snake(sirka_okna-10,60,10,10,ZELENA,"D",pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT,15,"zeleny"))
                    hadi.append(snake(0,60,10,10,MODRA,"D",pg.K_w,pg.K_s,pg.K_a,pg.K_d,15,"modry"))
                    menu  = False
                    hra = True
                    
                    len(hadi)
        tlacitka = []
                    
    
    if hra:
        pg.draw.rect(okno,CERNA, (0,0,sirka_okna,60))
        
        for had in hadi:
            had.nakreslise()
            had.pohyb()

        for clanecek in clanky:
            clanecek.nakreslise()
            clanecek.aPohyb()
            clanecek.naraz()

        for jabko in jablka:
            jabko.nakreslise()
            jabko.snezeno()

        for mrizka in mrize:
            mrizka.nakreslise()

        for tlacidlo in tlacitka:
            tlacidlo.nakreslise()
            tlacidlo.zmacknuti()
            if tlacidlo.zmacknuto == True:
                if tlacidlo.event == "Menu":
                    pass
                    

        

        text("Score: "+str(score),ZUZOVA,font50,5,0)
        text("Highscore: "+str(highscore),ZUZOVA,font50,sirka_okna-font50.size("Highscore: "+str(highscore))[0],0)

    pg.display.update()

    hodiny.tick(60)
    
pg.quit()
