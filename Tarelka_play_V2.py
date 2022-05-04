#ЭТО ВЕРСИЯ ИГРЫ 2.5(ребаг)
import pygame
import random

#экран
size = width, height = (1720, 880)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
pygame.init()
x = 0
#название окна
pygame.display.set_caption('WING COMMANDER')
running = True
#выбор сложности
while running:
    #вывод текста
    screen.fill((0, 0, 0))#для чёткости текста
    f3 = pygame.font.Font(None, 36)
    text3 = f3.render('Выберите сложность : 1-легко, 2-сложно, 3-невозможно(нажмите цифру на клавиатуре) ', True, (50, 205, 50))
    screen.blit(text3, (250, 350))
    pygame.display.flip()
    clock.tick(fps)
    #нажатие на цифры
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            V = 3
            L = 150
            st = 60
            B = 30
            x = x + 1
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            V = 3
            L = 100
            st = 40
            B = 30
            x = x + 2
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            V = 4
            L = 100
            st = 30
            B = 40
            x = x + 3
            running = False
            # выход
        if event.type == pygame.QUIT:
                running = False
                print("Вы вышли из игры")
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    print("Вы вышли из игры")
#нужно для вывода в конце
if x == 1:
    Level = "Легко"
if x == 2:
    Level = "Сложно"
if x == 3:
    Level = "Невозможно"

#звуки в игре
pygame.mixer.music.load("musik.mp3")
pygame.mixer.music.play(-1)
#создание звёзд на фоне
def draw():
    for i in range(1000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
# Берём из папки фотки
def load_image(name):
    fullname = "Foto" + "/" + name
    try:
        if name[-2:] == 'jpg':
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Cannot load image:', name)

        raise SystemExit()
    return image
#движене тарелки
def update(image, speed):
    #по Х
    if tal.rect.x + tal.rect.width > width:
        speed = -speed
    elif tal.rect.x < 0:
        speed = -speed
    tal.rect.x = tal.rect.x + speed
    return speed

#к звездолёту
image = load_image('Kosmolet_1.gif')
all_sprites = pygame.sprite.Group()
car = pygame.sprite.Sprite()
car.image = image
car.rect = car.image.get_rect()
all_sprites.add(car)

#Тарелка
image_2 = load_image('Tarelka.gif')
tal = pygame.sprite.Sprite()
tal.image = image_2
tal.rect = tal.image.get_rect()
all_sprites.add(tal)
random.seed()
tal.rect.x, tal.rect.y = random.randint(200,1600), random.randint(100,300)
#пересоздане тарелки
def tall():
    tal.rect.x, tal.rect.y = random.randint(200, 1600), random.randint(100, 300)
    all_sprites.add(tal)
#кординаты
car.rect.x = 500
car.rect.y = 500
#луч космолёта
image_3 = load_image('Piy.gif')
piy = pygame.sprite.Sprite()
piy.image = image_3
piy.rect = piy.image.get_rect()
#луч  тарелки
image_4 = load_image('Piy_2.gif')
piy_2 = pygame.sprite.Sprite()
piy_2.image = image_4
piy_2.rect = piy_2.image.get_rect()
#скорость тарелки и лучей и ещё некоторые переменные
v = V
r = 0
l = L
b = B
step = st
running = True
#цикл
while running:
    # возрат космолёта в экран
    #при увеличении размера экрана менять значения учитывая что шаг = 50
    #верх
    if car.rect.x <= 1600 and car.rect.y <= 0 :
        # += step тк step = одному движению
        car.rect.y += step
    #низ
    if car.rect.x <= 1600 and car.rect.y >= 800:
        car.rect.y -= step
    #лево
    if car.rect.x <= +100 and car.rect.y <= 700:
        car.rect.x += step
    #право
    if car.rect.x >= 1500 and car.rect.y <= 700:
        car.rect.x -= step

    #проверка на попадание от космолёта
    if  tal.rect.y  <= piy.rect.y <= tal.rect.y + 140:
        if tal.rect.x + 10 <= piy.rect.x <= tal.rect.x + 100:
            b -= 1
            piy.kill()
            r +=1
            #убираем спрайт
            tal.kill()
            # добовляем новый
            tall()
    # проверка на попадание от тарелки
    if car.rect.y <= piy_2.rect.y <= car.rect.y + 140:
        if car.rect.x <= piy_2.rect.x <= car.rect.x + 150:
            piy_2.kill()
            l -= 1

    # стрельба тарелки
    if car.rect.x <= tal.rect.x <= car.rect.x + 100:
        all_sprites.add(piy_2)
        piy_2.rect.x = tal.rect.x + 50
        piy_2.rect.y = tal.rect.y + 10
    #основной
    for event in pygame.event.get():
        #движение космолёта
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            car.rect.y -= step

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            car.rect.y += step

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            car.rect.x -= step

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            car.rect.x += step

        # создание лазера ИЗ КОСМОЛЁТА  и стрельба при ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.add(piy)
            piy.rect.x = car.rect.x + 75
            piy.rect.y = car.rect.y - 30
        #выход
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #изменение цвета для космолётаd
    if l <= 150:
        Color = (50, 205, 50)
    if l <= 50:
        Color = (255, 255, 0)
    if l <= 25:
        Color = (255, 0, 0)
    # изменение цвета для тарелки
    if b <= 40:
        Color_t = (50, 205, 50)
    if b <= 20:
        Color_t = (255, 255, 0)
    if b <= 10:
        Color_t = (255, 0, 0)

    #проверка на то что энергия закончилась
    if l <= 0:
        running = False
        print("Вас сбили, у врага осталось : " + str(b),"энергии", "На сложности: " + Level)
    if b <= 0:
        running = False
        print("Вы сбили врага","на сложности: " + Level)
    #заливка экрана
    screen.fill((0, 0, 0))
    #Энергия врага
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('ЭНЕРГИЯ ВРАГА: ' + str(b), True, (Color_t))
    screen.blit(text1, (350, 30))
    #Энергия космолёта
    f2 = pygame.font.Font(None, 36)
    text2 = f2.render('ТВОЯ ЭНЕРГИЯ: ' + str(l), True, (Color))
    screen.blit(text2, (670, 30))
    #движене лазеров
    piy.rect.y -= 20
    piy_2.rect.y += 10
    #движене тарелки
    for sprite in all_sprites:
        v = update(sprite, v)
    #создане звёзд
    draw()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()