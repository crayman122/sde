#open the door
#get on the floor
#every body walk the dinosaur
#chris olson is a sexy beast
#sebastian is cooler than chris
import pygame
import time
import random
import os.path
import sys
import linecache #needed for reading/writing files
#Perform file exists checks
if os.path.exists("resource") == False:
    print "FATAL EXECPTION 1.0: Directory \'resource\' does not exist!"
    quit()
if os.path.exists("resource/sprite") == False:
    print "FATAL EXECPTION 1.1: Directory \'resource/sprite\' does not exist!"
    quit()
if os.path.exists("resource/font") == False:
    print "FATAL EXCEPTION 1.2: Directory \'resource/sound\' does not exist!"
    quit()
#pygame init
pygame.init()
screeninfo = pygame.display.Info()
screen = pygame.display.set_mode((416, 160))
pygame.display.set_caption("Super Dungeon Adventure PC")
font = pygame.font.Font('resource/font/pressstart2p.ttf', 13)
#define all necesary classes
class makeobj(object):
    #creates an object at the position (x*16, y*16)
    def __init__(self,(x,y), sprite, render_group):
        self.x = x*16
        self.y = y*16
        self.sprite = sprite
        self.render_group = render_group
        self.obj = pygame.sprite.Sprite()
        self.obj.image = pygame.image.load(self.sprite)
        self.obj.rect = self.obj.image.get_rect()
        self.obj.rect.left = self.x
        self.obj.rect.top = self.y
        render_group.add(self.obj)
        self.render_group = render_group
    def setpos(self, (x,y)):
        #set position (x*16, y*16)
        self.x = x*16
        self.y = y*16
        self.rect.left = self.x
        self.rect.top = self.y
    def collision(self, groups):
        #return all collisions
        self.collisions = []
        self.groups = groups
        for i in range(len(self.groups)):
            self.collisions.append(pygame.sprite.spritecollideany(self.obj, self.groups[i]))
        return self.collisions
    def changesprite(self, sprite):
        self.sprite = sprite
        self.obj.image = pygame.image.load(self.sprite)
        self.obj.rect = self.obj.image.get_rect()
        self.obj.rect.left = self.x
        self.obj.rect.top = self.y
        self.render_group.draw(screen)
        pygame.display.update()
    def remove(self):
        self.changesprite('resource/sprite/nothing.gif')
        self = None
#Define render groups here
mountain_group = pygame.sprite.OrderedUpdates()
tree_group = pygame.sprite.OrderedUpdates()
house_group = pygame.sprite.OrderedUpdates()
box_group = pygame.sprite.OrderedUpdates()
def initoverworld():
    #draws overworld
    #trees
    treesprite = "resource/sprite/tree.gif"
    tree = makeobj((6, 0), treesprite, tree_group)
    tree1 = makeobj((2,3), treesprite, tree_group)
    tree2 = makeobj((5, 3), treesprite, tree_group)
    tree3 = makeobj((6, 5), treesprite, tree_group)
    tree4 = makeobj((2, 6), treesprite, tree_group)
    tree5 = makeobj((4, 6), treesprite, tree_group)
    tree6  = makeobj((8, 6), treesprite, tree_group)
    tree7 = makeobj((6, 7), treesprite, tree_group)
    tree8 = makeobj((3, 8), treesprite, tree_group)
    tree9 = makeobj((7, 8), treesprite, tree_group)
    tree10 = makeobj((9, 8), treesprite, tree_group)
    tree11 = makeobj((2, 9), treesprite, tree_group)
    tree12 = makeobj((6, 9), treesprite, tree_group)
    tree13 = makeobj((4, 10), treesprite, tree_group)
    tree14 = makeobj((8, 10), treesprite, tree_group)
    #houses
    housesprite = 'resource/sprite/house.gif'
    house = makeobj((3, 2), housesprite, house_group)
    house2 = makeobj((1, 2), housesprite, house_group)
    house3 = makeobj((3, 1), housesprite, house_group)
"""    #mountain
    mountainsprite = "resource/sprite/mountain.gif"
    createobj("mountain", "mountain_group", (9 * 16, 0), mountainsprite)
    createobj("mountain1", "mountain_group", (9 * 16, 1 * 16), mountainsprite)
    createobj("mountain2", "mountain_group", (10 * 16, 1 * 16), mountainsprite)
    createobj("mountain3", "mountain_group", (8 * 16, 2 * 16), mountainsprite)
    createobj("mountain4", "mountain_group", (9 * 16, 2 * 16), mountainsprite)
    createobj("mountain5", "mountain_group", (10 * 16, 2 * 16), mountainsprite)
    createobj("mountain6", "mountain_group", (11 * 16, 2 * 16), mountainsprite)
    createobj("mountain7", "mountain_group", (9 * 16, 3 * 16), mountainsprite)
    createobj("mountain8", "mountain_group", (10 * 16, 3 * 16), mountainsprite)
    createobj("mountain9", "mountain_group", (11 * 16, 3 * 16), mountainsprite)
    createobj("mountain10", "mountain_group", (12 * 16, 3 * 16), mountainsprite)
    createobj("mountain11", "mountain_group", (11 * 16, 4 * 16), mountainsprite)
    createobj("mountain12", "mountain_group", (12 * 16, 4 * 16), mountainsprite)
    createobj("mountain13", "mountain_group", (13 * 16, 4 * 16), mountainsprite)
    createobj("mountain14", "mountain_group", (12 * 16, 5 * 16), mountainsprite)
    createobj("mountain15", "mountain_group", (13 * 16, 5 * 16), mountainsprite)
    createobj("mountain16", "mountain_group", (12 * 16, 6 * 16), mountainsprite)
    createobj("mountain17", "mountain_group", (13 * 16, 6 * 16), mountainsprite)
    createobj("mountain18", "mountain_group", (14 * 16, 6 * 16), mountainsprite)
    createobj("mountain19", "mountain_group", (13 * 16, 7 * 16), mountainsprite)
    createobj("mountain20", "mountain_group", (14 * 16, 7 * 16), mountainsprite)
    createobj("mountain21", "mountain_group", (14 * 16, 8 * 16), mountainsprite)
    createobj("mountain22", "mountain_group", (14 * 16, 9 * 16), mountainsprite)
    createobj("mountain23", "mountain_group", (15 * 16, 9 * 16), mountainsprite)"""
class text(object):
    #makes a text
    def __init__(self, (x,y), ascii, (red, green, blue)):
        self.x = x
        self.y = y
        self.ascii = ascii
        self.red = red
        self.green = green
        self.blue = blue
        self.boldstate = False
        self.underlinestate = False
        self.italicstate = False
        self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
        self.rect = self.obj.get_rect(left=self.x, top=self.y)
        screen.blit(self.obj, self.rect)
        pygame.display.update()
    def changeascii(self, new):
        self.red1 = self.red
        self.green1 = self.green
        self.blue1 = self.blue
        self.color((255,255,255))
        self.ascii = new
        self.color((self.red1, self.green1, self.blue1))     
    def color(self, (red, green, blue)):
        #change text color
        self.red = red
        self.green = green
        self.blue = blue
        self.redraw()
    def location(self, (x,y)):
        #change text location !!EXACT NOT RELATIVE TO GRID!!
        self.x = x
        self.y = y
        self.rect = self.obj.get_rect(left=self.x, top=self.y)
        self.redraw()
    def bold(self, state):
        #makes text bold
        self.boldstate = state
        self.redraw()
    def italic(self, state):
        #makes text italic
        self.italicstate = state
        self.redraw()
    def underline(self, state):
        #makes text underline
        self.underlinestate = state
        self.redraw()
    def normal(self):
        #return text to default
        self.red1 = self.red
        self.green1 = self.green
        self.blue1= self.blue
        self.red = 255
        self.blue = 255
        self.green = 255
        self.redraw()
        self.boldstate = False
        self.italicstate = False
        self.underlinestate = False
        self.red = self.red1
        self.green = self.green1
        self.blue = self.blue1
        self.redraw()
    def remove(self):
        #deletes text
        self.obj = font.render(self.ascii, False, (255,255,255))
        screen.blit(self.obj, self.rect)
        pygame.display.update()
        self = None
    def redraw(self):
        #redraws text
        if self.boldstate == True:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_bold(font, True)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        elif self.boldstate == False:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_bold(font, False)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        if self.italicstate == True:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_italic(font, True)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        elif self.italicstate == False:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_italic(font, False)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        if self.underlinestate == True:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_underline(font, True)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        elif self.underlinestate == False:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_underline(font, False)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        else:
            self.obj = font.render(self.ascii, False, (255,255,255))
            screen.blit(self.obj, self.rect)
            pygame.font.Font.set_bold(font, False)
            pygame.font.Font.set_italic(font, False)
            pygame.font.Font.set_underline(font, False)
            self.obj = font.render(self.ascii, False, (self.red,self.green,self.blue))
            screen.blit(self.obj, self.rect)
        pygame.font.Font.set_underline(font, False)
        pygame.font.Font.set_italic(font, False)
        pygame.font.Font.set_bold(font, False)
        pygame.display.update()
class playsound(object):
    #plays a sound
    def __init__(self, filename):
        self.filename = filename
        self.sound = pygame.mixer.Sound(self.filename)
        self.sound.play()
    def play(self):
        self.sound.play()
    def stop(self):
        self.sound.stop()
class textbox(object):
    #creates a text box
    def __init__(self, string):
        self.string = str(string)
        self.boxgroup = pygame.sprite.OrderedUpdates()
        self.boxobj = makeobj((0,5), "resource/sprite/textbox.gif", self.boxgroup)
        self.boxgroup.draw(screen)
        pygame.display.update()
        self.textobj = text((4,84), self.string, (0,0,0))
        pygame.display.update()
        self.end = False
        while self.end != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.sound = playsound('resource/sound/bading.ogg')
                        self.end = True
                        self.textobj.remove()
                        
                        
class menunew(object):
    #makes a menu using new classes
    #You can use self.resume values to do different things based on output
    def __init__(self, title, choices, functions):
        self.opensound = playsound('resource/sound/bading.ogg')
        
        resume = False
        self.header = title
        if len(choices) > 5 or len(functions) > 5:
            print "Error, more than 5 choices specified!"
            return False
        if len(choices) < 2 or len(functions) <2:
            print "Error Menu Needs more than 2 choices"
            return False
        else:
            self.var = 0
            for i in range(len(choices)):
                temp = "self.choice%d = choices[%d]" %(self.var, self.var)
                exec(temp)
                self.var += 1
            self.var = 0
            self.functions = functions
        self.frame = makeobj((0,0), "resource/sprite/menu.gif", box_group)
        box_group.draw(screen)
        self.titleobj = text((4, 4), self.header, (0,0,0))
        self.titleobj.bold(True)
        self.var = 0
        for i in range(len(choices)):
            self.currentline = self.var+1
            self.currentline = self.currentline*16
            self.currentline = self.currentline+1
            temp = "self.choiceobj%d = text((4, self.currentline), self.choice%d, (0,0,0))" %(self.var, self.var)
            exec(temp)
            self.var += 1
        self.var = len(choices)-1
        self.choiceobj0.underline(state=True)
        self.menu_enter = False
        self.menuselected = 0
        self.resume = False
        while self.resume == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.lowsound = playsound('resource/sound/blip.ogg')
                        if self.menuselected != self.var: 
                            self.menuselected += 1
                    elif event.key == pygame.K_z:
                        
                        self.menu_enter = True
                    elif event.key == pygame.K_UP:
                        self.upsound = playsound('resource/sound/blip.ogg')
                        if self.menuselected != 0:
                            self.menuselected -= 1
                
                if self.menu_enter == True:
                    self.menu_enter = False
                    if self.menuselected == 0:
                        exec(self.functions[0])
                        self.entersound = playsound('resource/sound/bading.ogg')
                    if self.menuselected == 1:
                        exec(self.functions[1])
                        self.entersound = playsound('resource/sound/bading.ogg')
                    if self.menuselected == 2:
                        exec(self.functions[2])
                        self.entersound = playsound('resource/sound/bading.ogg')
                    if self.menuselected == 3:
                        exec(self.functions[3])
                        self.entersound = playsound('resource/sound/bading.ogg')
                    if self.menuselected == 4:
                        exec(self.functions[4])
                        self.entersound = playsound('resource/sound/bading.ogg')
                elif self.menuselected == 0:
                    self.choiceobj0.underline(state=True)
                    self.choiceobj1.normal()
                elif self.menuselected == 1:
                    self.choiceobj1.underline(state=True)
                    self.choiceobj0.normal()
                    if self.var > 1:
                        self.choiceobj2.normal()
                elif self.menuselected == 2:
                    self.choiceobj1.normal()
                    self.choiceobj2.underline(state=True)
                    if self.var > 2:
                        self.choiceobj3.normal()
                elif self.menuselected == 3:
                    self.choiceobj2.normal()
                    self.choiceobj3.underline(state=True)
                    if self.var > 3:
                        self.choiceobj4.normal()
                elif self.menuselected == 4:
                    self.choiceobj3.normal()
                    self.choiceobj4.underline(state=True)
        else:
            self = None
class inputnum(object):
    def __init__(self, maximum, minimum=1):
        self.maximum = maximum
        self.minimum = minimum
        self.value = self.minimum
        self.inputgroup = pygame.sprite.OrderedUpdates()
        self.inputbox =  makeobj((0, 0), 'resource/sprite/num.gif', self.inputgroup)
        self.inputgroup.draw(screen)
        self.text = text((4, 8), str(self.value), (0,0,0))
        self.resume = False
        while self.resume == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.sound = playsound('resource/sound/blip.ogg')
                        if self.value != self.minimum and self.value != 0: 
                            self.value -= 1
                            self.text.changeascii(str(self.value))
                            self.text.redraw()
                    elif event.key == pygame.K_z:
                        self.sound = playsound('resource/sound/blip.ogg')
                        self.resume = True
                    elif event.key == pygame.K_c:
                        self.sound = playsound('resource/sound/blip.ogg')
                        self.resume = True
                        self.value = 0
                    elif event.key == pygame.K_UP:
                        self.sound = playsound('resource/sound/blip.ogg')
                        if self.value != self.maximum and self.value != 999:
                            self.value += 1
                            self.text.changeascii(str(self.value))
                            self.text.redraw()
        print self.value
        self.text.remove()
        self.inputbox.remove()
        self = self.value
        gametick(1)
class inventory(object):
    ###############################
    #documentation for inventories#
    ###############################
    #VALUES OF ITEMS              #
    ###############################
    #0 gold                       #
    #1 health potion              #
    #2 mana potion                #
    #3 key                        #
    #4 Other (Meta specified)     #
    ###############################
    #TODO                         #
    #                             #
    ###############################
    def __init__(self):
        self.inventory = []
    def additem(self, itemval, ammount, meta=None):
        self.itemtoadd = {'type': itemval, 'number': ammount, 'meta': meta}
        loop = next((a for a in self.inventory if a ['type'] == itemval), None)
        if loop:
            loop['number'] += ammount
        else:
            self.inventory.append(self.itemtoadd)
    def removeitem(self, itemval, ammount):
        loop = next((a for a in self.inventory if a ['type'] == itemval), None)
        if loop:
            loop['number'] -= ammount
        else:
            print "err: no thing to remove from inventory"
        
class monster(object):
    def __init__(self, kind, charlevel):
        print 'monster created'
        self.kind = kind
        self.level = random.randint(charlevel, charlevel+2)
        self.health = 10 + self.level*5
        self.inventory = inventory()
        self.gold = random.randint(self.level*2, self.level*2+10)
    def attack(self):
        self.textbox = textbox("%s Attacks" %(self.kind))
        self.attack = random.randint(self.level*10, self.level*10+10)
        if random.randint(1, 10) == random.randint(1,10):
            if random.randint(1,10) == random.randint(1,10):
                self.critbox = textbox("Critical hit!")
                self.critbox = textbox("%d Damage!" %(self.attack*2))
                character.attribute('health', -self.attack*2)
            else:
                self.missbox = textbox("The attack misses")
        else:
            self.textbox = textbox("%d Damage!" %(self.attack))
            character.attribute('health', -self.attack)
    def defeat(self):
        print 'monster defeated'
        self.textbox = textbox("%s Defeated!" %(self.kind))
        self.textbox = textbox("You earned %d Gold!" %(self.gold))
        character.inv.additem(0, self.gold)
        global battleend
        battleend = True
        self = None
class char(object):
    def __init__(self):
        self.x = 1
        self.y = 0
        self.char = pygame.sprite.Sprite()
        self.char.image = pygame.image.load('resource/sprite/char.gif')
        self.char.rect = self.char.image.get_rect()
        self.inv = inventory()
        self.inv.additem(0,10)
        self.attributes = {'health': 100 , 'maxhealth': 100, 'mana': 10, 'maxmana': 10, 'level': 1, 'xp': 0} 
        global char_group
        char_group.add(self.char)
        self.char.rect.top = self.y*16
        self.char.rect.left = self.x*16
        char_group.draw(screen)
        pygame.display.update()
    def draw(self):
        self.char.rect.top = self.y*16
        self.char.rect.left = self.x*16
        global char_group
        char_group.draw(screen)
        pygame.display.update()
    def collision(self, groups):
        self.groups = groups
        self.collisions = []
        for i in range(len(self.groups)):
            self.collisions.append(pygame.sprite.spritecollideany(self.char, self.groups[i]))
        return self.collisions                                                     
    def up(self):
        self.yb = self.y - 1
        self.char.rect.top = self.yb*16
        if all(v is None for v in self.collision(groups)) == True:
            if self.yb < 10 and self.yb >= 0:
                self.y = self.yb
            else:
                self.char.rect.top = self.y*16
        else:
            self.char.rect.top = self.y*16
        self.draw()
    def down(self):
        self.yb = self.y + 1
        self.char.rect.top = self.yb*16
        if all(v is None for v in self.collision(groups)) == True:
            if self.yb < 10 and self.yb >= 0:
                self.y = self.yb
            else:
                self.char.rect.top = self.y*16
        else:
            self.char.rect.top = self.y*16
        self.draw()
    def left(self):
        self.xb = self.x - 1
        self.char.rect.left = self.xb*16
        if all(v is None for v in self.collision(groups)) == True:
            if self.xb <= 25 and self.xb >= 0:
                self.x = self.xb
            else:
                self.char.rect.left = self.x*16
        else:
            self.char.rect.left = self.x*16
        self.draw()
    def right(self):
        self.xb = self.x + 1
        self.char.rect.left = self.xb*16
        if all(v is None for v in self.collision(groups)) == True:
            if self.xb <= 25 and self.xb >= 0:
                self.x = self.xb
            else:
                self.char.rect.left = self.x*16
        else:
            self.char.rect.left = self.x*16
        self.draw()
    def attribute(self, attribute, value):
        self.attributes[attribute] += value
#function definitions here
def gameintro():
    screen.fill((255,255,255))
    pygame.display.update()
    pygame.time.delay(1000)
    introtxt1 = text((-100, 64+8), "- LOW", (230,230,230))
    introtxt2 = text((500, 64+8), "PRESSURE -", (230,230,230))
    color = 230
    location1 = -81
    location2 = 416
    for i in range(208):
        location1 += 1
        location2 -= 1
        color -= 1
        screen.fill((255,255,255))
        introtxt1.location((location1, 64+8))
        introtxt2.location((location2, 64+8))
        introtxt1.color((color, color, color))
        introtxt2.color((color, color, color))
        pygame.display.update()
        pygame.time.delay(10)
    introsound = playsound('resource/sound/intro.ogg')
    pygame.time.delay(3000)
def encounter():
    print 'entering encounter'
    kind = random.randint(1, 3)
    if kind == 1:
        kind = "Wolf"
    elif kind == 2:
        kind = "Rat"
    elif kind == 3:
        kind = "Bat"
    battleend = False
    monster1 = monster(kind, character.attributes['level'])
    encbox = textbox("A wild %s appeared" %(kind))
    while battleend == False:
        if monster1.health <= 0:
            print 'monster defeated'
            monster1.defeat()
            battleend = True
        if character.attributes['health'] <= 0:
            dedbox = textbox('You have been died.')
            pygame.quit()
            quit()
        battlemenu = menunew("Battle", ["Attack", "Run"], ["self.resume = 1", "self.resume = 2"])
        if battlemenu.resume == 1:
            print 'player attack'
            plyrattack = False
            attackfor = random.randint(character.attributes['level']+10, character.attributes['level']+20)
            attacktextbox = textbox("You Attack")
            if random.randint(1, 10) == random.randint(1,10):
                if random.randint(1,10) == random.randint(1,10):
                    critbox = textbox("Critical hit!")
                    critbox = textbox("%d Damage!" %(attackfor*2))
                    monster1.health -= attackfor*2
                    if monster1.health <= 0:
                        monster1.defeat()
                        battleend = True
                    else:
                        pass
                else:
                    missbox = textbox("You miss")
            else:
                attackbox = textbox("%d Damage!" %(attackfor))
                monster1.health -= attackfor
                if monster1.health <= 0:
                    monster1.defeat()
                    battleend = True
            monster.attack
        if battlemenu.resume == 2:
            print 'player run'
            plyrrun = False
            if random.randint(1, 10) == random.randint(1, 10):
                escapebox = textbox('Couldnt escape!')
            else:
                escapebox = textbox('You got away')
                gametick(1)
                battleend = True
    else:
        pass
def inventorymenu():
    #well fuck. I don't know even where to start, I should probably be debuging the acutal program fist though,
    #rather than starting a new thing :/
    return None
def newgame():
    screen.fill((0,0,0))
    pygame.display.update()
    pygame.time.delay(750)
    t1 = textbox(' Where am I?')
    t2 = textbox(' Am I dead?')
    t3 = textbox(' No, I\'m not dead...')
    t4 = textbox(' * You open your eyes *')
    pygame.time.delay(750)
    initoverworld()
def mainmenu():
    screen.fill((255,255,255))
    pygame.display.update()
    background = pygame.sprite.OrderedUpdates()
    backgroundsprite = makeobj((0,0), 'resource/sprite/titlescreen.gif', background)
    background.draw(screen)
    exec(linecache.getline('build.txt', 1))
    print 'This is version %s of SDE' %(version)
    versiontext = text((1,160-16), version, (0,0,0))
    pygame.mixer.music.load('resource/sound/musictemp.ogg')
    pygame.mixer.music.play(0)
    menu = menunew("Main Menu", ["New", "Load", "Quit"], ['pygame.mixer.music.stop(); self.resume = True; newgame()', '', 'pygame.quit(); exit()'])
def gametick(kind=0):
    #0 for full tick
    #1 for redraw only
    print 'gametick'
    screen.fill((255,255,255))  
    char_group.draw(screen)
    tree_group.draw(screen)
    house_group.draw(screen)
    mountain_group.draw(screen)
    pygame.display.update()
    if battleend == True:
        if random.randint(1, 25) == random.randint(1,25):
            print 'two numbers were equal'
            if battleend == False:
                print 'battle is already in progress, ignoring'
            else:
                encounter()
                gametick(1)
battleend = True 
end = False
#Runonce functions
gameintro()
mainmenu()
pygame.mixer.music.play(0)
initoverworld()
global char_group
char_group = pygame.sprite.OrderedUpdates()
groups = [mountain_group, tree_group, house_group]
character = char()
gametick(1)
#Main loop
while end != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character.up()
                gametick()
            elif event.key == pygame.K_DOWN:
                character.down()
                gametick()
            elif event.key == pygame.K_LEFT:
                character.left()
                gametick()
            elif event.key == pygame.K_RIGHT:
                character.right()
                gametick()
            elif event.key == pygame.K_c:
                menu = menunew("Menu", ["Resume", "Items", "Levels", "Save", "Quit"], ["self.resume = True", "", "", "", "quitconf = menunew(\"Really?\", [\"Yes\", \"No\"],  [\"mainmenu()\", \"self.resume = True\"])"])
                gametick()
            elif event.key == pygame.K_ESCAPE:
                end = True
    
pygame.quit()
quit()
