from PIL import Image
import sys
import random

def PNGname_gen(file_path :str) -> str:
    file_id = str(random.randrange(0, 3999, 1))
    if (len(file_id) < 4):
        file_id = str(((4-len(file_id)))*0) + file_id
    file_path = file_path[-1:]
    file_path = file_path[file_path.rfind('\\'):]
    return file_path+ file_id + ".png"
if(len(sys.argv) > 1):
    file_path = sys.argv[1]
    img = Image.open(file_path).convert('L')
    wFile_name = PNGname_gen(file_path)
    if(img.save(wFile_name)):
        print("sucess!")
    else:
        print("failure")
else:
    print("pass the path to the image to this script as an argument")
    print("py script.py path\\to\\file")

