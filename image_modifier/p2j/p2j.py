# convert_to_jpg
from PIL import Image
import os


def convert_to_jpg(source_path : 'string'):
    '''
    function to convert jpg images to jpg
    Args:
        source_path: path to a folder containing all png files
    '''
    if not os.path.isfile(source_path):
        raise ValueError("Image file does not exist")
    elif source_path.split('.')[-1] not in ['png']:
        raise ValueError("Image is not PNG")

    dest_path = source_path.split("."+source_path.split('.')[-1])[0]+'.jpg'
    file = Image.open(source_path).convert('RGB')
    file.save(dest_path,'jpeg')
