import cv2

#Changes exactly one frame/image using opencv
def changeColor(s):

    #splits values of the image
    image = s
    b, g, r = cv2.split(image)


    #change the integer values to change bg color, O(1) time
    #for some reason min-maxing uint8 manually is 5ms longer than the function :/
    b = cv2.add(b, 255)
    g = cv2.add(g, 0)
    r= cv2.add(r,0)
    merged = cv2.merge([b,g,r])

    #return modified image
    return merged


    #FOR EMERGENCY: Discarded code for manual changes, O(n^3) time
    #for index0 in range (len(image)):
        #for index1 in range(len(image[0])):
            #for index2 in range(len(image[0][0])):
                #pixel = int(image[index0][index1][2])+255
                #image[index0][index1][2]= np.clip(min(255,pixel), 0, 255).astype(np.uint8)