import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.d = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("catch the ball 1.0")
        pygame.display.update()

        self.height_end_circle = 580
        self.taghir_moghtasat = 10
        self.width_circle = 200
        self.moghtasat_rec = 200
        self.size_rec = 10
        self.height_circ = 20
        self.f = True
        self.x = 0
        self.y = 0
        self.speed = 10
        self.ball_timer = 0

        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def show_text(self, message, x_pos, y_pos, color):
        text_place = self.font.render(message, True, color)
        self.d.blit(text_place, (x_pos, y_pos))

    def menu(self):
        p = "hello which level do you want to play? easy==press .e  medium==press .m  hard==press .h"
        game_started = False

        while not game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.speed = 30
                        game_started = True
                    elif event.key == pygame.K_m:
                        self.speed = 20
                        game_started = True
                    elif event.key == pygame.K_h:
                        self.speed = 15
                        game_started = True
            
            self.d.fill((0, 0, 0))
            self.show_text(p, 10, 200, (225, 0, 0))
            pygame.display.update()
            pygame.time.delay(50)

    def run(self):
        while self.f:
            pygame.time.delay(self.speed)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.f = False
            
            self.ball_timer += 1

            if self.height_circ < self.height_end_circle:
                self.height_circ += 10
                self.d.fill((0, 0, 0))
            else:
                if self.ball_timer > 40:
                    if self.moghtasat_rec <= self.width_circle <= (self.moghtasat_rec + 90):
                        self.x += 1
                    else:
                        self.y += 1
                    
                    self.height_circ, self.width_circle = 20, random.randint(10, 390)
                    self.ball_timer = 0
                    continue

            self.show_text("score:" + str(self.x), 10, 10, (225, 0, 0))
            self.show_text("miss:" + str(self.y), 10, 50, (225, 0, 0))

            pygame.draw.circle(self.d, (255, 0, 0), (self.width_circle, self.height_circ), self.taghir_moghtasat)

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.moghtasat_rec > 0:
                self.moghtasat_rec -= self.taghir_moghtasat
            elif key[pygame.K_RIGHT] and self.moghtasat_rec < 310:
                self.moghtasat_rec += self.taghir_moghtasat

            pygame.draw.rect(self.d, (225, 0, 0), (self.moghtasat_rec, 580, 90, self.size_rec))
            pygame.display.update()

        pygame.quit()

game = Game()
game.menu()
game.run()