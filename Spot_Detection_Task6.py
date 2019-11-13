#@ IOService io
#@ UIService ui
#@ OpService ops

# Task 1.1: open a single image using io.open(path)
image = io.open("/path/to/oocyte_4_1.tif")

# Task 1.2: find out the type/class of the returned object
print(image.class)

# Task 1.3: show the image in the UI
#ui.show(image)

# Task 2: find out the image dimensions and axis order
print("The image has %s dimensions." % image.numDimensions())
dims = [image.dimension(d) for d in range(image.numDimensions())]
print("The dimensions are %s" % dims)

# Task 3: Extract the first channel (i.e. index 0 from dimension 2)
channel1 = ops.run("hyperSliceView", image, 2, 0)
print("The result has %s dimensions." % channel1.numDimensions())

# Task 4: Apply a Difference of Gaussians (DoG) filter
#   NOTE: we have to convert to 'float32' to get the desired result
dog_ch1 = ops.run("filter.dog", ops.run("convert.float32", channel1), 1.5, 1.0)

# Task 5: Detect local maxima using LocalExtrema from ImgLib2
from net.imglib2.algorithm.localextrema import LocalExtrema
from net.imglib2.type.numeric.real import FloatType

pointList1 = LocalExtrema.findLocalExtrema(dog_ch1, new LocalExtrema.MaximumCheck(new FloatType(100)))
print("The returned list has %s entries." % len(pointList1))

# Task 6: Add point coordinates to results table
#@ ResultsTable rt
