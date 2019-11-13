# Introduction to ImageJ2 Scripting

(Mafalda Sousa, acknowledged to Jan Eglinger )

This exercise will introduce some basics of the scripting functionality in ImageJ2
 
1. How to get started with script parameters
 
# What are script parameters?
They look like this:

```python
  #@ Dataset image
  ```

* The "hash at" (#@) is used to identify a script parameter.
* The "Dataset" is the type of the input. In this case, we want an image.
* There are several types associated with images, but when in doubt, just use Dataset. :-)
* The "image" is the name of the variable.
* The input value will be assigned differently depending on the context.

Other script parameters:

An informative message
```python
  #@ String (visibility=MESSAGE, value="Please enter some parameter values", persist=false, required=false) msg
  ```

A set of predefined choices
```python
#@ String (label="Which measurement?", choices={mean,median,min,max}) measurement
```
A File parameter can have two styles: "open" (the default) or "save"
```python
#@ File (style=save, label="Save image to") destinationFile
```
A slider to choose a numeric input value
```python
#@ Double (style=slider, min=0.5, max=10, stepSize=0.5, columns=3) someValue
```
We can also define OUTPUTs.
Output parameters will be processed by the framework after executing the script.
Most known output types (e.g. numbers, text or boolean values) will be shown in a results table.

```python
#@output Boolean success

success = true
return 
```
Note that all these script parameters also work in .ijm macros! No need to use Dialog.create, Dialog.addNumber, Dialog.show etc. anymore!!

2. ImageJ API: SciJava Services and Ops
 
A large part of the ImageJ functionality is provided by services.
Let us introduce some of the most important services here.
We can access them easily using script parameters:
 
LogService can be used to log e.g. infos, warnings and errors
```python
#@ LogService log

log.info("This is an info message.")
log.warn("This is a warning.")
log.error("This is an error.")
```

IOService can be used to open and save images or other data
```python
#@ IOService io
```
baboon = io.open("https://imagej.net/images/baboon.gif")

UIService can be used to display an image or other data
```python
#@ UIService ui

ui.show(baboon)
```
Note that in addition to IOService, there's also DatasetIOService, which has more control over how images are opened.

Finally, there's OpService, giving access to the powerful ImageJ Ops
```python
#@ OpService ops
```
Now, for example run the "stats.mean" op. (Note that it returns an ImgLib2 Type, so we need to call getRealDouble() to get its value.)
```python
value = ops.run("stats.mean", image).getRealDouble()
```
For more services, see https://imagej.net/SciJava_Common#Services

3. How to mix and match IJ1 and IJ2 API

In many cases, we can rely on the framework to do the conversion autmatically.

For other cases, we can use the ConvertService to convert from one type to another.

If we need to have the active image both as (IJ2) Dataset and (IJ1) ImagePlus,
we can just use two input parameters (the Dataset above and a new ImagePlus here):
```python
#@ ImagePlus imp

# Run an ImageJ1 plugin, e.g. Invert...
import ij.IJ
IJ.run(imp, "Invert", "")

````

If we really need to convert between the two,
(e.g. because you create a new image and need to process it)
we have several options to do so:

** ConvertService.convert()
** LegacyService.getImageMap.register...
** ImageJFunctions.wrap()

```python
# Create a new image using Ops

sinusoidImage = ops.run("create.img", [100, 100])

# Fill image with some data

ops.run("image.equation", sinusoidImage, "63 * (Math.cos(0.3*p[0]) + Math.sin(0.3*p[1])) + 127")

# Create a Dataset from the result
#@ DatasetService datasetService
sinusoidDataset = datasetService.create(sinusoidImage)

#show image
ui.show(sinusoidDataset)

# Convert the image

#  Using ConvertService
import ij.ImagePlus
sinusoidImp = convertService.convert(sinusoidDataset, ImagePlus.class)

```
For further information on mixing and matching IJ1 and IJ2, see:
https://imagej.net/ImageJ1-ImageJ2_cheat_sheet


```python
# Run "Find Maxima...", an ImageJ1 plugin, to count the maxima
IJ.run(sinusoidImp, "Find Maxima...", "noise=10 output=Count")
```

