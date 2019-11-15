# Introduction to ImageJ2 Scripting

(Mafalda Sousa, acknowledged to Jan Eglinger )

This exercise will introduce some basics of the scripting functionality in ImageJ2
 
# 1. How to get started with script parameters
 
*What are script parameters?*
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

# 2. ImageJ API: SciJava Services and Ops
 
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
baboon = io.open("https://imagej.net/images/baboon.gif")
```


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

# 3. Creating and Displaying an Image
The following piece of code creates and displays an 400x320 8-bit gray-level image:
```groovy
import net.imglib2.img.Img
import net.imglib2.img.array.ArrayImgFactory
import net.imglib2.type.numeric.integer.UnsignedByteType
 
// will create a window showing a black 400x320 image
long[] dimensions = [400, 320]
final Img< UnsignedByteType > img = new ArrayImgFactory<>( new UnsignedByteType() ).create( dimensions )
  ```

Line 1: Pixel images in ImgLib2 are created using an *ImgFactory*. There are different ImgFactories, that create pixel containers with different memory layouts. Here, we create an ArrayImgFactory. This factory creates containers that map to a single flat Java array.

The type parameter of the factory specifies the value type of the image we want to create. We want to create a 8-bit gray-level image, thus we use UnsignedByteType.

Line 2: Next we create a long[] array that specifies the image size in every dimension. The length of the array specifies the number of dimensions. Here, we state that we want to create 400x320 2D image.

Line 3: We create the image, using the factory and dimensions. We store the result of the create() method in an Img variable. Img is a convenience interface that gathers properties of pixel image containers such as having a number of dimensions, being able to iterate its pixels, etc.

# 4. Opening and Displaying Image Files
You can open image files with the IO utility class of SCIFIO which calls Bio-Formats as needed. The following opens and displays an image file.

```groovy
import net.imglib2.img.Img
import net.imglib2.img.array.ArrayImgFactory
import net.imglib2.type.numeric.integer.UnsignedByteType
import io.scif.img.IO

// save path for an image of Lena
path = "https://samples.fiji.sc/new-lenna.jpg"

// load image
final Img< UnsignedByteType > img = IO.openImg( path,
    new ArrayImgFactory<>( new UnsignedByteType() ) );
```

When opening an image, we can specify which memory layout to use and as which value type we want to load the image. We want to use the ArrayImg layout again, and we want to have UnsignedByteType values again. We need an ImgFactory and an instance of the value type.
We can use the IO.openImg method, giving a filename and ImgFactory.
