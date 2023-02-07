# import required libraries
import os
import sys
from PIL import Image
  
# define a function for
# compressing an image
def compressMe(file):
    
    # Get the path of the file
    filepath = os.path.join(os.getcwd(), 
                            file)
    if (os.path.getsize(filepath) > 10000): # TODO: Maybe update this number
        print("Compressing " + filepath)  
        try:
            # open the image
            picture = Image.open(filepath)
                
            # TODO: Avoid files that are too small
              
            # Save the picture with desired quality
            # To change the quality of image,
            # set the quality variable at
            # your desired level, The more 
            # the value of quality variable 
            # and lesser the compression
            picture.save(file, 
                         "JPEG", 
                         optimize = True, 
                         quality = 10)
        except:
            print("...failed to compress")
            pass
  
# Define a main function
def main():
    
    args = sys.argv[1:]
    dirname = args[0]
                      
    # finds current working dir
  
    formats = ('.jpg', '.jpeg')
      
    # looping through all the files
    # in a current directory
    for file in os.listdir(dirname):
        
        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            compressMe(dirname+file)
  
    print("Done")
  
# Driver code
if __name__ == "__main__":
    main()
