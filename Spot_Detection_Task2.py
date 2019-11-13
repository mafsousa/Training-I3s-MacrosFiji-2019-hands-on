#@ IOService io
#@ UIService ui

# Task 1.1: open a single image using io.open(path)
image = io.open("/path/to/oocyte_4_1.tif")

# Task 1.2: find out the type/class of the returned object
print(image.class)

# Task 1.3: show the image in the UI
ui.show(image)

# Task 2: find out the image dimensions and axis order
