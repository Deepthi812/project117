import os
import cv2

path = "C:/Users/vindy/Downloads/project117/Images/"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext.lower() in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = os.path.join(path, file)
        
        print(file_name)

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape

size = (width, height)

print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count - 1):
    img = cv2.imread(images[i])

    out.write(img)

print("Done")

out.release()