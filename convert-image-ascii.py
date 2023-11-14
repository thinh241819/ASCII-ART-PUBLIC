from PIL import Image
import numpy as numpy
import os
import time

'''
Defining grey scale
'''
grey_scale1 = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h',
        'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J',
        'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', 
        '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', 
        'i', '!', 'l', 'I', ';', ':', '"', '^', '`', '.']

ASCII_CHARS = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$']
scale1 = False

ASCII_CHARS = ASCII_CHARS[::-1]

grey_scale2 = ['@', '%', '#', '*', '+', '=', '-', ':', '.']
grey_scale2 = grey_scale2[::-1]
print(len(ASCII_CHARS))
'''
method calAverageLight()
        - This function takes in a cropped portion of the image
        and compute the average brightness of that portion.
        - This works similar to resize function, making the picture blurry. 
        But we are doing this by hand.
'''
def calAverageLight(image):
    # Use numpy array method to turn the image into a 2-dimension array
    cropped_image = numpy.array(image)
    # Use numpy shape to get the dimension of the cropped section
    width_cropped, height_cropped = cropped_image.shape
    # Use numpy reshape to turn the cropped_image into a 1 dimension array
    pixel_list = cropped_image.reshape(width_cropped * height_cropped)
    # Return the average Light value of the whole cropped section
    return numpy.average(pixel_list)

def openImage(filename, new_width=200):
    image = Image.open(filename).convert('L')
    old_width, old_height = image.size[0], image.size[1]
    image_ratio = float(old_width) / float(old_height)

    # Crop the image into tile
    tile_width = old_width / new_width
    tile_height = tile_width / image_ratio
    # Num of rows
    rows = int(old_height / tile_height)

    # ascii image is a list of characters
    ascii_image = []
    # generate list of dimensions for tiles
    for i in range(rows):
        y1 = int(i * tile_height)
        y2 = int((i+1) * tile_height)
        # Correct last tile
        if i == rows - 1:
            y2 = old_height
        
        # Append an empty string
        ascii_image.append("")
        # Crop the image
        for j in range(new_width):
            x1 = int(j * tile_width)
            x2 = int((j + 1) * tile_width)
            # Correct the last tile
            if j == new_width - 1:
                x2 = old_width
            # Crop image
            cropped_tile = image.crop((x1, y1, x2, y2))
            # Get average light level of the cropped tile
            avg = int(calAverageLight(cropped_tile))
            # Look up the ascii char
            if scale1:
                ascii_val = grey_scale1[int((avg*64)/255)]
            else:
                ascii_val = grey_scale2[int((avg*8)/255)]
            # Append ascii char to string
            ascii_image[i] += ascii_val
    return ascii_image

if __name__ == '__main__':
    for i in range(1, 24):
        imageName = "h" + str(i) + ".jpg"
        imagePath = os.path.join('./temp_pic', imageName)
        outputName = "h" + str(i) + ".txt"
        outputPath = os.path.join('./output', outputName)
        aimg = openImage(imagePath)
        f = open(outputPath, 'w')
        for row in aimg:
            f.write(row + '\n')
        f.close()





print(grey_scale1)
