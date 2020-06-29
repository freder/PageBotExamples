# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E01_ScalingAnImage.py
#
#     How to scale an image (without being an element) in plain DrawBot?
#     Since the core DrawBot does not support w/h attrbiutes for images,
#     it needs to be done by using the scale() function.
#
#     Unfortunately this also changes to x/y position scale, so when
#     drawing an image on the canvas, the position must be scaled the
#     other way around. In this example it doesn't matter, because the
#     scaled image is positioned at (0, 0).
#
import os # Import module that communicates with the file system.
import sys

from pagebot.filepaths import getResourcesPath
from pagebot.toolbox.units import pt
from pagebot import getContext

for contextName in ('DrawBot', 'Flat'):
	print('Scaling image by', contextName)
	context = getContext(contextName)

	# Define the path where to find the example image.
	path = getResourcesPath() + "/images/cookbot1.jpg"
	# Use the standard DrawBot function to get the width/height of the image from the file.
	w, h = context.imageSize(path)

	# Let's say we want to scale it to 50%. The 0.5 is the multiplication factor.
	newScale = 0.5

	# Make a page with the size of the scaled image, rounded to whole pixels.
	context.newPage(pt(int(w*newScale)), pt(int(h*newScale)))

	# Save the “graphics state“, just in case the script is extended later, where other
	# operation need to work in 100%.
	context.save()
	context.scale(newScale) # Make all drawing scale to 50%
	context.image(path, pt(0, 0)) # Draw the scaled image at the bottom-left corner. It fills the whole page.
	# Save the page as png file (and also do conversion from jpg to png this way).
	# Save to _export folder, so the file will not upload into git. Otherwise anyone running this script will update the (same) image.
	if not os.path.exists('_export/'):
	    os.makedirs('_export/')
	# Note that resulting images may look sharper, but has 4.5x the size of the .jpg.
	context.saveImage('_export/01_ScaleImage-cookbot1-%d-%s.png' % (newScale*100, contextName)) # 944Kb size
	context.saveImage('_export/01_ScaleImage-cookbot1-%d-%s.jpg' % (newScale*100, contextName)) # 168Kb size
	context.saveImage('_export/01_ScaleImage-cookbot1-%d-%s.gif' % (newScale*100, contextName)) # 346Kb size
	# Restore the graphics state, so context scaling is back to 100% after this.
	context.restore()


print('Done')
