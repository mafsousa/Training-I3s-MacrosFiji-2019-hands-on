/ Introduction to ImageJ2 Scripting
// =================================

// (Mafalda Sousa, acknoledged to Jan Eglinger )

This exercise will introduce some basics of the scripting functionality in ImageJ2
 
 * 1. How to get started with script parameters
 
 What are script parameters?
They look like this:

#@ Dataset image

 * The "hash at" (#@) is used to identify a script parameter.
 * The "Dataset" is the type of the input. In this case, we want an image.
 * There are several types associated with images, but when in doubt, just use Dataset. :-)
 * The "image" is the name of the variable.
 * The input value will be assigned differently depending on the context.
 * In this case, we have a single image input, so the active ImageJ image will be used.
 * I.e.: the user will not need to explicitly select anything from any dialog box.
 
 
 
 
 * 2. ImageJ API: SciJava Services and Ops
 * 3. Calling scripts from other scripts
 * 4. Using ImgLib2 ROIs
 * 5. How to mix and match IJ1 and IJ2 API
 */
 
 
