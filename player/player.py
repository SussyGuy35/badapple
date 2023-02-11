import pygame, sys,json

class Cell(pygame.sprite.Sprite):
    def __init__(self,cell_x,cell_y,cell_width,draw_color):
        super().__init__()
        self.cell = (cell_x,cell_y)
        self.drawcolor = draw_color
        self.rect = pygame.rect.Rect((cell_x)*cell_width,(cell_y)*cell_width,cell_width,cell_width)
    def update(self):
        self.color = this_frame[f"{self.cell[0]},{self.cell[1]}"]
        pygame.draw.rect(screen,(self.drawcolor[0]*self.color,self.drawcolor[1]*self.color,self.drawcolor[2]*self.color),self.rect)
        #pygame.draw.rect(screen,(255*self.color,255*self.color,255*self.color),self.rect)

game_title = "badapple"
screen_width = 900
screen_height = 684
game_speed = 1

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(game_title)
clock = pygame.time.Clock()
font = pygame.font.Font("data/font.ttf",20)

cell_row = 50
cell_column = 38
cell_width = 18

color = (255,255,255)

badapple = pygame.mixer.Sound("data/badapple.mp3")

loading_text = font.render("Loading...",True,(255,255,255))
loading_text_rect = loading_text.get_rect()
loading_text_rect.center = (screen_width/2,screen_height/2)

frames = {}
frame = 0

screen.blit(loading_text,loading_text_rect)
pygame.display.flip()
with open("data/badapple.json") as data:
    frames = json.load(data)
print("import data successful!")

cell_group = pygame.sprite.Group()

for x in range(cell_row):
    for y in range(cell_column):
        cell_group.add(Cell(x,y,cell_width,color))
print(f"Created {cell_row*cell_column} cell!")

#print(frames)

badapple.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    this_frame = frames[str(frame)]
        
    screen.fill((0,0,0))

    cell_group.update()

    frame += 1

    pygame.display.flip()
    clock.tick(game_speed)        

          