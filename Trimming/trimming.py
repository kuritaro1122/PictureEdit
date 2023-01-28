from PIL import Image, ImageFilter
import os
import glob
import sys

# paths
inputPath = './input/'
outputPath = './output/'

CROP_FROM_SIZE = 0
CROP_FROM_ASPECT = 1

# crop types
CROP_CENTER = 0
CROP_LEFTDOWN = 1
CROP_LEFTUP = 2
CROP_RIGHTDOWN = 3
CROP_RIGHTUP = 4

def main():
    set_type = -1
    while set_type != CROP_FROM_SIZE and set_type != CROP_FROM_ASPECT:
        set_type = int(input('select setting type ([width height] : 0, [aspect] : 1) :'))
    crop_width = -1
    crop_height = -1
    if set_type == CROP_FROM_ASPECT:
        while crop_width <= 0:
            crop_width = int(input('crop aspect width:'))
        while crop_height <= 0:
            crop_height = int(input('crop aspect height:'))
    elif set_type == CROP_FROM_SIZE:
        while crop_width <= 0:
            crop_width = int(input('crop width:'))
        while crop_height <= 0:
            crop_height = int(input('crop height:'))
    print('search files...')
    files = glob.glob(inputPath + '*.png')
    if len(files) == 0:
        print('input files not found!!')
        return
    print("found {fn} files!!".format(fn=len(files)))
    for i, f in enumerate(files):
        img = Image.open(f)
        img_crop = None
        if set_type == CROP_FROM_ASPECT:
            if  crop_height / crop_width > img.height / img.width:
                img_crop = crop_center(img, img.height * (crop_width / crop_height), img.height)
                pass
            else:
                img_crop = crop_center(img, img.width, img.width * (crop_height / crop_width))
                pass
        elif set_type == CROP_FROM_SIZE:
            img_crop = crop_center(img, crop_width, crop_height)
        file_name = f.split('/')
        file_name = file_name[len(file_name) - 1]
        img_crop.save(outputPath + file_name)
        print('o', end= ('/' if (i + 1) % 5 == 0 else ''))
        sys.stdout.flush()
    print('\nfinish!!')

def crop_center(img : Image.Image, width, height):
    img_crop = img.crop(((img.width - width) // 2, (img.height - height) // 2, (img.width + width) // 2, (img.height + height) // 2))
    return img_crop

if __name__ == "__main__":
    main()