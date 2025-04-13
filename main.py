import pygame #импорт библиотеки для создания игр
import random #импорт модуля для работы с рандомными числами


class Food:
    def __init__(self, name_image, x, y, width, height):  # конструктор.Создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки
        self.image = pygame.transform.scale(self.image, (width, height)) #ширина и высота
        self.rect=self.image.get_rect()# создание прям по границам картинки
        self.rect.x = x #координаты прямоугольника
        self.rect.y = y


    def collide_food(self, p): #обработка сталкновения между едой и тарелкой
        if self.rect.colliderect(p.rect) == True: # если прямоугольники еды и тарелки сталкнулись
            food_list.remove(self)  #удаление объекта селф(еда) из списка фуд_лист

    def draw_image(self):  # МЕТОД!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! отрисовки
        screen.blit(self.image, (self.rect.x, self.rect.y))  # это отрисовка картинок на координатах x и y

    def move_food(self):  # ПОСТОЯННОЕ ДВИЖЕНИЕ ВНИЗ
        self.rect.y += 4 # движение еды в низ
        if self.rect.y > 720: #если еда не попадает на тарелку, а падает мимо, то она спавнится в верху
            self.rect.y = 0
    def move_plate(self):  # метод!!!!!!!!!!!!!!!!!!!!
        keys = pygame.key.get_pressed()  # получение списка нажатых клавиш
        if keys[pygame.K_LEFT]: # если нажата клавиша влево 
            self.rect.x -= 8
        elif keys[pygame.K_RIGHT]:# если нажата клавиша вправо 
            self.rect.x += 8


pygame.init()  # обязательная каманда people
window_size = (1280, 720) # размер окна
screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
a=1280/5
plate = Food('plate.png', 490, 620, 330, 98) #создание объекта класса фуд (тарелка)
fon = Food("kitchen.jpg", 0, 0, 1280, 720) #создание объекта класса фуд (фон)
food1 = Food("food1.png", a,  random.randint(-1280,0), 64, 64) #создание объекта класса фуд (еда 1)
food2 = Food("food2.png", 2*a, random.randint(-1280,0), 64, 64) 
food3 = Food("food3.png", 3*a, random.randint(-1280,0), 64, 64)
food4 = Food("food4.png", 4*a, random.randint(-1280,0), 64, 64)
food5 = Food("food5.png",4*a , random.randint(-1280,0), 64, 64)
food_list = [food1, food2, food3, food4, food5] #создание списка из еды
font = pygame.font.SysFont("Arial" , 50) #создание шрифта для текста победы
txt=''
text = font.render(txt, True, (0,0,0)) #сглаживание и цвет
while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймера
    fon.draw_image() #применение метода отрисовки к ОБЪЕКТУ fon
    screen.blit(text, (50,50)) # отрисовка текста (изначально это пустая строка)

    for i in food_list: #проходимся по списку еды, i - это каждый элемент списка, то есть каждая еда 
        i.draw_image() #отрисовка текущей еды
        i.move_food() #применение метода движение еды
        i.collide_food(plate) #роверка столкновения еды и тарелки
    plate.draw_image() #рименение метода отрисовки к ОБЪЕКТУ тарелке
    plate.move_plate() #бработка перемещения тарелки

    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА

    pygame.display.update()  # ОБНОВЛЕНИЕ ДИСПЛЕЯ
