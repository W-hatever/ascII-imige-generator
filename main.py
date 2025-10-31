from PIL import Image

img = Image.open("Image.jpeg")  # link your image here
img = img.resize((80, 40))  # scales it down to fit in terminal
img = img.convert("L")  # converts to grayscale

pixels = img.getdata()  # gets pixel data
chars = ["@", "#", "S", "%", "?", "*", "+", ";",
         ":", ",", "."]  # characters from dark to light
new_pixels = [chars[pixel // 25]
              for pixel in pixels]  # change pixels to characters
new_pixels = ''.join(new_pixels)  # join list to string

ascii_image = [new_pixels[index:index + 80]  # split string into lines of 80 characters
               # couse 80 is width of image
               for index in range(0, len(new_pixels), 80)]
ascii_image = "\n".join(ascii_image)  # join lines with newline character

with open("ascii_image.txt", "w") as f:  # write to a text file
    f.write(ascii_image)
print(ascii_image)  # print to console
