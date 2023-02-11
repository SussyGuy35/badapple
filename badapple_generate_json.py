from PIL import Image
import json
frames_data = {}
frames = {}

frames_num = int(input("Number of frames: "))
width = int(input("Width: "))
height = int(input("Height:"))
file_ext = input("File extension: ")

for i in range(1,frames_num+1):
    image_name = str(i).zfill(len(str(frames_num)))
    print(image_name)
    im = Image.open(f"frames/{image_name}.{file_ext}")
    pix = im.load()
    for x in range(0,width):
        for y in range(0,height):
            combine_rpg = pix[x,y][0] + pix[x,y][1] + pix[x,y][2] 
            if combine_rpg > 128*3:
                frames_data[f"{x},{y}"] = 1
            else: frames_data[f"{x},{y}"] = 0           
    frames[i-1] = frames_data
    frames_data = {}
with open("data/badapple.json","w") as file:
    json.dump(frames,file)
