import pygame, sys,json

class Cell(pygame.sprite.Sprite):
    def __init__(self,cell_x,cell_y,cell_width,draw_color):
        super().__init__()
        self.cell = (cell_x,cell_y)
        self.drawcolor = draw_color
        self.rect = pygame.rect.Rect((cell_x)*cell_width,(cell_y)*cell_width,cell_width,cell_width)
    def update(self):
        self.color = this_frame[f"{self.cell[0]},{self.cell[1]}"]
        pygame.draw.rect(screen,self.drawcolor[self.color],self.rect)
        
cell_width = 18
cell_row = 50
cell_column = 38

window_title = "badapple"
screen_width = 750
screen_height = 570
fps = 30

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()
font = pygame.font.Font("data/font.ttf",20)

color_black = (0,0,0)
color_white = (255,255,255)
color = [color_black,color_white]

badapple = pygame.mixer.Sound("data/badapple.mp3")

loading_text = font.render("Loading...",True,(255,255,255))
loading_text_rect = loading_text.get_rect()
loading_text_rect.center = (screen_width/2,screen_height/2)

frames = {}
frame_index = 0

screen.blit(loading_text,loading_text_rect)
pygame.display.flip()
with open("data/badapple.json") as data:
    frames = json.load(data)
print("import data successful!")

cell_row = frames["width"]
cell_column = frames["height"]
cell_width = frames["cell_width"]
fps = frames["speed"]

screen_width = cell_row*cell_width
screen_height = cell_column*cell_width
screen = pygame.display.set_mode((screen_width,screen_height))

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
    this_frame = frames[str(frame_index)]
        
    screen.fill((0,0,0))

    cell_group.update()

    frame_index += 1

    pygame.display.flip()
    clock.tick(fps)        

          
