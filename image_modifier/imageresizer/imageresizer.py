# image_resizer.py resize the images

from PIL import Image
import os, sys



def image_resize_pct(source_path : 'string',res_p : int = None):
    '''
    Args:
        source_path: path to folder containing all files
        res_p: center square/rectangle resize by user-determined percentage of Horizontal and Verticle propotionally
    '''
    if not os.path.isdir(source_path):
        raise ValueError('No such folder exists.')


    dirs = os.listdir(source_path)

    dest_folder = os.path.join(source_path, 'resized_images_percentage_'+str(res_p))
    os.mkdir(dest_folder)

    for item in dirs:
        if os.path.isfile(source_path+item):
            f, e = os.path.splitext(item)  
            im = Image.open(source_path+item)
            width, height = im.size

            if res_p:
                if not((0 < res_p <=100) and (0 < res_p <=100)):
                    raise ValueError('invalid percentage, please provide between 0 and 100')

                new_width = int(res_p*width/100)
                new_height = int(res_p*height/100)
            else:
                new_width = width
                new_height = height

            imresize = im.resize((new_width,new_height))

            imresize.save(f'{dest_folder}/{f}.jpg')






def image_resize_width(source_path : 'string',res_w : int=None):
    '''
    Args:
        source_path: path to folder containing all files
        res_w: width pixels to resize image by proportionally
    '''
    if not os.path.isdir(source_path):
        raise ValueError('No such folder exists.')


    dirs = os.listdir(source_path)

    dest_folder = os.path.join(source_path, 'resized_images_size_w'+str(res_w))
    os.mkdir(dest_folder)

    for item in dirs:
        if os.path.isfile(source_path+item):
            f, e = os.path.splitext(item)  
            im = Image.open(source_path+item)
            width, height = im.size

            new_width = int(res_w)
            new_height = int(height*res_w/width)

            imresize = im.resize((new_width,new_height))
            imresize.save(f'{dest_folder}/{f}.png')

def image_resize_height(source_path : 'string',res_h : int=None):
    '''
    Args:
        source_path: path to folder containing all files
        res_h: height pixels to resize image by proportionally
    '''
    if not os.path.isdir(source_path):
        raise ValueError('No such folder exists.')


    dirs = os.listdir(source_path)

    dest_folder = os.path.join(source_path, 'resized_images_size_h'+str(res_h))
    os.mkdir(dest_folder)

    for item in dirs:
        if os.path.isfile(source_path+item):
            f, e = os.path.splitext(item)  
            im = Image.open(source_path+item)
            width, height = im.size

            new_height = int(res_h)
            new_width = int(width*res_h/height)

            imresize = im.resize((new_width,new_height))
            imresize.save(f'{dest_folder}/{f}.png')
