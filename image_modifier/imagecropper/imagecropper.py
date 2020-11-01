# imagecropper.py crop the images by size and percentages

from PIL import Image
import os, sys




def image_crop_size(source_path : 'string',crp_px : 'Size Tuple (W, H)'):
    '''
    Args:
        source_path: path to folder containing all files
        dest_path: path to folder where transformed files should be saved
        crp_px: center square/rectangle crop by user-determined pixels
    Returns:List contaning file names which could not be cropped due to size issues
    '''
    if not os.path.isdir(source_path):
        raise ValueError('No such folder exists.')


    dirs = os.listdir(source_path)

    dest_folder = os.path.join(source_path, 'cropeed_images_size_'+str(crp_px))
    os.mkdir(dest_folder)

    skipped_images=[]
    for item in dirs:
        if os.path.isfile(source_path+item):
            f, e = os.path.splitext(item)  # split extension
            im = Image.open(source_path+item)
            width, height = im.size

            if crp_px:
                if not (len(crp_px)==2):
                    raise ValueError ('two arguments required')

                new_width = crp_px[0]
                new_height = crp_px[1]

            else:
                new_width = width
                new_height = height

            if not (width >= new_width and height>=new_height):
                skipped_images.append(item)

            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2

            imCrop = im.crop((left,top,right,bottom))
            imCrop.save(f'{dest_folder}/{f}.jpg')
            if len(skipped_images)>0:
                print (f'following files could not be cropped due to size mismatches {skipped_images}')
    return skipped_images


def image_crop_pct(source_path : 'string',crp_p : 'Percentage in int(Horizontal, Verticle)'):
    '''
    Args:
        source_path: path to folder containing all files
        dest_path: path to folder where transformed files should be saved
        crp_p: center square/rectangle crop by user-determined percentage of Horizontal and Verticle
    Returns:List contaning file names which could not be cropped due to size issues

    '''
    if not os.path.isdir(source_path):
        raise ValueError('No such folder exists.')


    dirs = os.listdir(source_path)

    dest_folder = os.path.join(source_path, 'cropped_images_percentage_'+str(crp_p))
    os.mkdir(dest_folder)

    skipped_images=[]
    for item in dirs:
        if os.path.isfile(source_path+item):
            f, e = os.path.splitext(item)  # split extension
            im = Image.open(source_path+item)
            width, height = im.size

            if crp_p:
                if not(0 < crp_p <=100):
                    raise ValueError('invalid percentage, please provide between 0 and 100')

                new_width = crp_p*width/100
                new_height = crp_p*height/100
            else:
                new_width = width
                new_height = height

            if not (width >= new_width and height>=new_height):
                skipped_images.append(item)

            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2

            imCrop = im.crop((left,top,right,bottom))
            imCrop.save(f'{dest_folder}/{f}.jpg')
            if len(skipped_images)>0:
                print (f'following files could not be cropped due to size mismatches {skipped_images}')
    return skipped_images
