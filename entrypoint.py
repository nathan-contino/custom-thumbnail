import os
import subprocess as sp
import glob
from PIL import Image
import os

### development purpose only ################
# from dotenv import load_dotenv #pip install python-dotenv
# load_dotenv()
#######################

MAX_HEIGHT_WIDTH = os.environ['INPUT_BASE_HEIGHT_WIDTH'] or "500"
INPLACE = os.environ['INPUT_INPLACE'] or "disable"
KEEP_DIR_STRUCTURE = os.environ['INPUT_KEEP_DIR_STRUCTURE'] or "enable"
OVERWRITE_EXISTING_THUMBNAILS = os.environ['INPUT_OVERWRITE_EXISTING_THUMBNAILS'] or "enable"

def main():

    # Recusrively get all the image files (jpg,jpeg,png)

    result = []
    for name in glob.glob('./**/*.png',recursive = True): 
        result.append(name) 

    for name in glob.glob('./**/*.jpg',recursive = True): 
        result.append(name) 

    for name in glob.glob('./**/*.jpeg',recursive = True): 
        result.append(name) 
  

    max_height_width = int(MAX_HEIGHT_WIDTH)
    size = max_height_width,max_height_width
 
    if not os.path.exists('./.thumbnails'):
        os.makedirs('./.thumbnails')

    for entry in result:

        out_file = os.path.basename(entry)
        file_name = os.path.splitext(entry)[0]
        file_ext = os.path.splitext(entry)[1]
        try:
            im = Image.open(entry)
            im.thumbnail(size,Image.ANTIALIAS)
            if INPLACE=="enable":
                im.save(entry)
                print(f"wrote:  {entry} ----> {entry}")
            else:
                if KEEP_DIR_STRUCTURE=="disable":
                    out_path = os.path.abspath(f"./.thumbnails/{out_file}")
                    im.save(out_path)
                else:
                    out_path = os.path.abspath(f"./.thumbnails/{entry}")
                    out_dir = os.path.dirname(out_path)
                    if not os.path.exists(out_dir):
                        os.makedirs(out_dir)
                    # print(out_dir)
                    # print(out_path)
                    if OVERWRITE_EXISTING_THUMBNAILS=="disable":
                        if not os.path.exists(out_path):
                            im.save(out_path)
                    else:
                        im.save(out_path)
                print(f"wrote:  {entry} ----> {out_path}")


        except IOError:
            print(f" ERROR: can't create thumbnail for {entry} Error: {IOError}")



if __name__ == '__main__':
    main()