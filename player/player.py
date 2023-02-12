import pygame, sys,json
   
version = "0.4"

cell_width = 18
cell_row = 50
cell_column = 38

window_title = f"Bad apple player v{version} by BachNob. https://github.com/SussyGuy35/badapple"
screen_width = 750
screen_height = 570
fps = 30

try:
    pygame.mixer.pre_init(44100,-16,2,512)
    hav_music = True
except:
    print("Failed to init pygame.mixer. Will play without audio!")    
    hav_music = False
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(window_title)
clock = pygame.time.Clock()
font = pygame.font.Font("data/font.ttf",20)

color_black = (0,0,0)
color_white = (255,255,255)

badapple = pygame.mixer.Sound("data/badapple.mp3")

loading_text = font.render("Loading...",True,(255,255,255))
loading_text_rect = loading_text.get_rect()
loading_text_rect.center = (screen_width/2,screen_height/2)

frames = {}
frame_index = 0

screen.fill(color_black)
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

if hav_music: badapple.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(color_black)        
    this_frame = frames[str(frame_index)]
        
    cells_length = len(this_frame["list_x"])
    for i in range(cells_length):
        x = this_frame["list_x"][i]
        y = this_frame["list_y"][i]
        cell_rect = pygame.rect.Rect(x*cell_width,y*cell_width,cell_width,cell_width)
        pygame.draw.rect(screen,color_white,cell_rect)

    frame_index += 1

    pygame.display.flip()
    clock.tick(fps)        

          
