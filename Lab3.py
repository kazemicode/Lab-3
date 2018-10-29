# Sara Kazemi
# Group: SCSI Logic - Ryan Dorrity, Sara Kazemi, Nathan Warren-Acord, Cody Young  
# CST 205
# Lab 3 
# 2018-10-28

# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Reduces the amount of red in each pixel by half
def halfRed():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
    r = getRed(p)
    # set red value to the new reduced value
    setRed(p, r * .5)
   repaint(pic) 
    

# Eliminates all blue in each pixel        
def noBlue():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
    b = getBlue(p)
    setBlue(p, 0)
   repaint(pic)
    
# Problem 1:
# Reduces amount of redness by the percentage passed in to the parameter        
def lessRed(percent):
   pic = getPic()
   pixels = getPixels(pic)
   setColorWrapAround(0)
   for p in pixels:
    r = getRed(p)
    newRed = r - (r * (percent/100))
  
    # set red value to the new reduced value
    setRed(p, newRed)
   repaint(pic) 
    
# Problem 2:
# Increases amount of redness by the percentage passed in to the parameter      
def moreRed(percent):
   pic = getPic()
   pixels = getPixels(pic)
   setColorWrapAround(0)
   for p in pixels:
    r = getRed(p)
    newRed = r + (r * (percent/100))
    # The commented lines below aren't needed since ColorWrapAround 
    # is set to false by default to prevent overflow
    #if newRed > 255:
    # newRed = 255
    setRed(p, newRed)
   repaint(pic) 
    
# Problem 3:
# Makes an image appear pink
def roseColoredGlasses():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
     myRed = getRed(p) 
     myGreen = getGreen(p) * .50
     myBlue = getBlue(p) * .75
     setColor(p, makeColor(myRed, myGreen, myBlue))
   repaint(pic) 

# Problem 4:
# Makes every pixel in the picture appear lighter; effectively lightens the entire picture
def lightenUp():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
    # set color of each pixel to a lighter hue
    setColor(p, makeLighter(getColor(p)))
   repaint(pic) 

# Problem 5:
# Alters the picture so that it is the negative of the original
def makeNegative():
   pic = getPic()
   pixels = getPixels(pic)

   for p in pixels:
    # Find opposite of color by subtracting from max
     r = 255 - getRed(p) 
     g = 255 - getGreen(p) 
     b = 255 - getBlue(p)
     setColor(p, makeColor(r, g, b))
   repaint(pic)

# Problem 6: 
# Alters the picture so that it is grayscale
def BnW():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
    # Find opposite of color by subtracting from max
     newColor =  (getRed(p) + getGreen(p) + getBlue(p)) / 3
     setColor(p, makeColor(newColor, newColor, newColor))
   repaint(pic)
 
# improved grayscale function using weights  
def betterBnW():
   pic = getPic()
   pixels = getPixels(pic)
   for p in pixels:
      # Find opposite of color by subtracting from max and multiply by weight
      newColor =  (getRed(p) * 0.299 + getGreen(p) * 0.587 + getBlue(p) * 0.114) / 3
      setColor(p, makeColor(newColor, newColor, newColor))
   repaint(pic)