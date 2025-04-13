import pygame
import random


class Food:
    def __init__(self, name_image, x, y, width, height):  # конструктор.Создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect=self.image.get_rect()# создание прям по границам картинки
        self.rect.x = x
        self.rect.y = y


    def collide_food(self, f): #обработка сталкновения между едой и тарелкой
        if self.rect.colliderect(f.rect) == True:
            food_list.remove(self)

    def draw_image(self):  # МЕТОД!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        screen.blit(self.image, (self.rect.x, self.rect.y))  # это отрисовка картинок на координатах x и y

    def move_food(self):  # ПОСТОЯННОЕ ДВИЖЕНИЕ ВНИЗ
        self.rect.y += 4
        if self.rect.y > 720:
            self.rect.y = 0
    def move_plate(self):  # метод!!!!!!!!!!!!!!!!!!!!
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 8
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 8


pygame.init()  # обязательная каманда people
window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
a=1280/5
plate = Food('plate.png', 490, 620, 330, 98)
fon = Food("kitchen.jpg", 0, 0, 1280, 720)
food1 = Food("food1.png", a,  random.randint(-1280,0), 64, 64)
food2 = Food("food2.png", 2*a, random.randint(-1280,0), 64, 64)
food3 = Food("food3.png", 3*a, random.randint(-1280,0), 64, 64)
food4 = Food("food4.png", 4*a, random.randint(-1280,0), 64, 64)
food5 = Food("food5.png",4*a , random.randint(-1280,0), 64, 64)
food_list = [food1, food2, food3, food4, food5]
font = pygame.font.SysFont("Arial" , 50)
txt=''
text = font.render(txt, True, (0,0,0))
while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    fon.draw_image()
    screen.blit(text, (50,50))

    for i in food_list:
        i.draw_image()
        i.move_food()
        i.collide_food(plate)
    plate.draw_image()
    plate.move_plate()

    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА

    pygame.display.update()  # ОБНОВЛЕНИЕ ДИСПЛЕЯ