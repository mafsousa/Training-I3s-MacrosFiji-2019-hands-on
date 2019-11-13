# Introduction to ImageJ2 Scripting
=====================================

(Mafalda Sousa, acknowledged to Jan Eglinger )

This exercise will introduce some basics of the scripting functionality in ImageJ2
 
1. How to get started with script parameters
 
What are script parameters?
They look like this:

  #@ Dataset image

* The "hash at" (#@) is used to identify a script parameter.
* The "Dataset" is the type of the input. In this case, we want an image.
* There are several types associated with images, but when in doubt, just use Dataset. :-)
* The "image" is the name of the variable.
* The input value will be assigned differently depending on the context.

Other script parameters
An informative message
  #@ String (visibility=MESSAGE, value="Please enter some parameter values", persist=false, required=false) msg

We can provide a set of predefined choices
#@ String (label="Which measurement?", choices={mean,median,min,max}) measurement

A File parameter can have two styles: "open" (the default) or "save"
#@ File (style=save, label="Save image to") destinationFile

A slider to choose a numeric input value
#@ Double (style=slider, min=0.5, max=10, stepSize=0.5, columns=3) someValue

We can also define OUTPUTs.
Output parameters will be processed by the framework after executing the script.
Most known output types (e.g. numbers, text or boolean values) will be shown in a results table.

#@output Boolean success

success = true
return 

Note that all these script parameters also work in .ijm macros! No need to use Dialog.create, Dialog.addNumber, Dialog.show etc. anymore!!

2. ImageJ API: SciJava Services and Ops
 
 A large part of the ImageJ functionality is provided by services.
  
 Let us introduce some of the most important services here.
 We can access them easily using script parameters:
 

LogService can be used to log e.g. infos, warnings and errors
#@ LogService log

log.info("This is an info message.")
log.warn("This is a warning.")
log.error("This is an error.")

IOService can be used to open and save images or other data
#@ IOService io

baboon = io.open("https://imagej.net/images/baboon.gif")

UIService can be used to display an image or other data
#@ UIService ui

ui.show(baboon)

Note that in addition to IOService, there's also DatasetIOService, which has more control over how images are opened.

Finally, there's OpService, giving access to the powerful ImageJ Ops

#@ OpService ops

// Let's also define another output here:

#@output value

Now, for example run the "stats.mean" op. (Note that it returns an ImgLib2 Type, so we need to call getRealDouble() to get its value.)
value = ops.run("stats.mean", image).getRealDouble()

For more services, see https://imagej.net/SciJava_Common#Services
 
 * 3. Calling scripts from other scripts
 * 4. Using ImgLib2 ROIs
 * 5. How to mix and match IJ1 and IJ2 API
 */
 
 
