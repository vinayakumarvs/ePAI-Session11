# Session 11 - Tuples & Named Tuples and Modules
# EPAi Session11 Assignment

#### Objective of Assignment:

1. Create these modules:
    
    1. jpg/jpeg to png conversion (use PIL library) j2p
    
    2. png to jpg conversion (use PIL library) p2j

    3. image resizer that can resize bulk images with these features:
        
        1. resize by user determined percentage (say 50% for height and width) (proportional) res_p
        2. resize by user determined width (proportional) res_w
        3. resize by user determined height (proportional) res_h
    4. image cropper that can crop bulk images with these features:
        1. center square/rectangle crop by user-determined pixels crp_px
        2. centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
        3. it let's user know which all images were not cropped due to size mismatches
    5. a __main__ module that exposes all these features (using argparse)
    6. finally create an zipped app, that exposes all of these features

    ## How to test your code:
1. each module must be independently available and tested (write test to check whether you can call them from command line) 
2. each feature must be available via argument selection
3. images must not be required to be in the same folder where your code is
4. final test:
    1. download 20 jpeg images of size more than 1000x1000
    2. convert to png
    3. convert to jpg
    4. resize to 80%
    5. resize to 500 width
    6. resize to 500 height
    7. all this using your zipped app
    8. center crop to 224x224

## Solution:
### j2p
    The function does convert the jpg and jpeg file to png

### p2j 
    The function does convert the png to jpg and jpeg file

### image_resize_pct
    The function does resize the images propotionally to the user provided percentage

### image_resize_width
    The function does resize the images propotionally to the user provided width of the image

### image_resize_height
    The function does resize the images propotionally to the user provided height of the image

### image_crop_size
    The function does crop the images propotionally to the user provided height and width

### image_crop_pct
    The function does crop the images propotionally to the user provided percentage



Created a test functions to validate the above functions.
