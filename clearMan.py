from PIL import Image

def findOddMedian(RGBVals):
    RGBLength = len(RGBVals) # counts the total number of individual red, green, and blue pixels in the picture
    sortRGBPixels = sorted(RGBVals) # sorts the values of the pixels from least to greatest
    oddMedian = ( (RGBLength + 1) / 2) - 1 # calculates the location of the middle value (Subtract one because of zero index)
    return sortRGBPixels[oddMedian] # returns the median value of the pixels

origImgs = [] # creating lists
redPixelList = []
greenPixelList = []
bluePixelList = []

for i in range (9): # for loop opens the images vs typing out "open image1, image2, etc"
    origImgs.append(Image.open(str(i+1) + ".png"))
    
picW, picH = origImgs[0].size # getting the size of the pic and sets it to "width, height" order
newImg = Image.new("RGB", (picW, picH)) # the function .new takes in a mode and width/height

for x in range (picW): # moves horizontally across the image/ checks the width
    for y in range (picH): # moves vertically across the image/ checks the height
        for myImage in origImgs:  # getting the values of red, green, and blue
            myRed, myGreen, myBlue = myImage.getpixel((x,y)) # gets the pixels
            
            redPixelList.append(myRed) # storing myRed values in the redPixelList
            greenPixelList.append(myGreen) # storing myGreen values in the greenPixelList
            bluePixelList.append(myBlue) # storing myBlue values in the bluePixelList
            
            newImg.putpixel((x,y), (findOddMedian(redPixelList), findOddMedian(greenPixelList), findOddMedian(bluePixelList)))
            #findOddMedian(*color*) returns the median for said color and puts it into the new image
            
        del redPixelList [:] # deletes the values from the append list in the loop
        del greenPixelList [:]
        del bluePixelList [:]
        
newImg.save("FinalizedImage.png") # saving the picture w/o the man
