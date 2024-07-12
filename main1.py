import cv2
import os
from PIL import Image
#Pillow - Image Processing Library Python Imaging Library

os.chdir('C:/Users/desha/OneDrive/Documents/Opencv/Opencv Lesson 6/photos')
path='C:/Users/desha/OneDrive/Documents/Opencv/Opencv Lesson 6/photos'

mean_width=0
mean_height=0

#os.listdir('.') - to list files and directories in a current working directory
num_of_images = len(os.listdir('.'))
print(num_of_images)

for file in os.listdir('.'):
    #C:/Users/HP/Desktop/JL/OpenCV/Lesson6/photos/3d_1563.jpg
    img=Image.open(os.path.join(path,file))
    width,height=img.size
    mean_width = mean_width+width
    mean_height = mean_height+height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print("Mean Width : ",mean_width)
print("Mean Height : ",mean_height)

for file in os.listdir('.'):
    img=Image.open(os.path.join(path,file))
    image_resize=img.resize((mean_width, mean_height))
    image_resize.save(file, 'JPEG', quality = 100)

print('Image has been resized.')

def video_generate():
    video_name = "MyFirstVideo.avi"
    os.chdir('C:/Users/desha/OneDrive/Documents/Opencv/Opencv Lesson 6/photos')
    images = []
    for file in os.listdir('.'):
        images.append(file)
    print(images)
    frame = cv2.imread(os.path.join(".",images[0]))
    height, width, layer = frame.shape
    print(frame.shape)
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for file in images:
        video.write(cv2.imread(os.path.join(".", file)))
    cv2.destroyAllWindows()
    video.release()
    

video_generate()

