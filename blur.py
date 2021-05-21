"""
File: blur.py
Name: Andy Wu
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    According to the four loops to deal with the image.
    """
    old_img = img
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for y in range(old_img.height):
        for x in range(old_img.width):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    # By the nearby neighbors, to average the value.
                    pixel_x = x+i
                    pixel_y = y + i
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            sum_red += pixel.red
                            sum_green += pixel.green
                            sum_blue += pixel.blue
                            count += 1
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = sum_red / count
            new_pixel.green = sum_green / count
            new_pixel.blue = sum_blue / count
    return blurred


def main():
    """
    Using the function blur() to blur the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
