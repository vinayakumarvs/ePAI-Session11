import inspect
import os
import re
import pytest
from image_modifier.j2p import j2p
from image_modifier.p2j import p2j
from image_modifier.imageresizer import imageresizer
from image_modifier.imagecropper import imagecropper



modules_all = [j2p, p2j, imageresizer, imagecropper]


README_CONTENT_CHECK_FOR = ["j2p","p2j","image_resize_pct","image_resize_width","image_resize_height","image_crop_size","image_crop_pct"]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    for each_module in modules_all:
        lines = inspect.getsource(each_module)
        spaces = re.findall('\n +.', lines)
        for space in spaces:
            assert len(space) % 4 == 2, f"Your script {each_module} contains misplaced indentations"
            assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    for each_module in modules_all:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_docstring():
    for each_module in modules_all:
        functions = inspect.getmembers(each_module, inspect.isfunction)

    for func in functions:
        assert not func.__doc__ is None, f"docstring not included in {func}"

def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    for item in modules_all:
        functions = inspect.getmembers(item, inspect.isfunction)
        for function in functions:
            if function[1].__name__ not in ['namedtuple', 'wraps']:
                assert function[1].__annotations__


path = os.path.abspath('Images')


def test_j2p_converter():
    command = f'python image_modifier/j2p/j2p.py -ip {path}/img_2.jpg'
    execute_command =  os.system(command)
    assert not execute_command, "Image JPG/JPEG Conversion failed"

def test_p2j_converter():
    command = f'python image_modifier/p2j/p2j.py -ip {path}/img_2.png'
    execute_command =  os.system(command)
    assert not execute_command, "Image PNG Conversion failed"


def test_image_resize_pct():
    command = f'python image_modifier/imageresizer/imageresizer.py res_p -fp {path} -p 45'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by Percentage failed"

def test_image_resize_width():
    command = f'python image_modifier/imageresizer/imageresizer.py res_w -fp {path} -w 450'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by width pixel failed"

def test_image_resize_height():
    command = f'python image_modifier/imageresizer/imageresizer.py res_h -fp {path} -H 550'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by height pixel failed"

def test_image_crop_size():
    command = f'python image_modifier/imagecropper/imagecropper.py crp_px -fp {path} -w 480 -H 560'
    execute_command =  os.system(command)
    assert not execute_command, "Image cropper by pixel failed"

def test_image_crop_pct():
    command = f'python image_modifier/imagecropper/imagecropper.py crp_p -fp {path} -p 56'
    execute_command =  os.system(command)
    assert not execute_command, "Image cropper by percentage failed"

def test_image_resize_pct_80():
    command = f'python image_modifier/imageresizer/imageresizer.py res_p -fp {path} -p 80'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by Percentage failed"

def test_image_resize_width_500():
    command = f'python image_modifier/imageresizer/imageresizer.py res_w -fp {path} -w 500'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by width pixel failed"

def test_image_resize_height_500():
    command = f'python image_modifier/imageresizer/imageresizer.py res_h -fp {path} -H 500'
    execute_command =  os.system(command)
    assert not execute_command, "Image resizer by height pixel failed"

def test_image_crop_size_224_224():
    command = f'python image_modifier/imagecropper/imagecropper.py crp_px -fp {path} -w 224 -H 224'
    execute_command =  os.system(command)
    assert not execute_command, "Image cropper by pixel failed"
