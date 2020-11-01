# jpg to png converter
from PIL import Image
import os
import argparse


def convert_to_png(source_path : 'String'):
    '''
    function to convert jpg images to png
    Args:
        source_path: path to a folder containing all jpg files
    '''
    if not os.path.isfile(source_path):
        raise ValueError("Image file does not exist")
    elif source_path.split('.')[-1] not in ['jpg','jpeg']:
        raise ValueError("Image is either not JPG or JPEG")

    dest_path = source_path.split("."+source_path.split('.')[-1])[0]+'.png'
    file = Image.open(source_path).convert('RGB')
    file.save(dest_path,'png')
