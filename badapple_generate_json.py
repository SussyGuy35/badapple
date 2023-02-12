from PIL import Image
import json
frames_data = {}
frames = {}

frames_num = int(input("Number of frames: "))
width = int(input("Width: "))
height = int(input("Height: "))
file_ext = input("File extension: ")
file_prefix = input("File name prefix: ")
sensitive = int(input("Sensitive (128 if unsure): "))
speed = int(input("FPS: "))
cell_width = int(input("Pixel size on play: "))


for i in range(1,frames_num+1):
    image_name = str(i).zfill(len(str(frames_num)))
    print(image_name)
    im = Image.open(f"frames/{file_prefix}{image_name}.{file_ext}")
    pix = im.load()
    for x in range(0,width):
        for y in range(0,height):
            combine_rpg = pix[x,y][0] + pix[x,y][1] + pix[x,y][2] 
            if combine_rpg > sensitive*3:
                frames_data[f"{x},{y}"] = 1
            else: frames_data[f"{x},{y}"] = 0           
    frames[i-1] = frames_data
    frames_data = {}
frames["width"] = width
frames["height"] = height
frames["speed"] = speed
frames["cell_width"] = cell_width
print("Creating json...")
with open("player/data/badapple.json","w") as file:
    json.dump(frames,file)
print("Create json successful!")
