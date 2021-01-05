import PIL

# rotate an image and display image

from PIL import Image
im = Image.open("example.jpg")
im.rotate(45).show()

# resize an image and save the new image with a new name

from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

# rotate an image and save the new image with a new name

from PIL import Image
im = Image("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

#  rotate, resize, and save an image with a new name

from PIL import Image
im = Image("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

# import images from /home/user/images/ folder and convert all to jpg, rotated 90', and resize to 128x128 then save in new directory /opt/icons/

#!/usr/bin/env python3
from PIL import Image
import os, sys
user=os.getenv('USER')
images_dir='/home/{}/images/'.format(user)
for image_name in os.listdir(images_dir):
    if not image_name.startswith('.'):
        image_path=images_dir+image_name
        im=Image.open(image_path)
        new_path='/opt/icons/'+image_name.split('.')[0]
        im.rotate(-90).convert('RGB').resize((128,128)).save(new_path,'jpeg')
        im.close()