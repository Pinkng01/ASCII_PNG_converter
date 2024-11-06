from PIL import Image
import sys
import random


file_id = str(random.randrange(0, 3999, 1))
if (len(file_id) < 4):
    file_id = str(((4-len(file_id)))*0) + file_id
print(file_id)
file_path = sys.argv[1]
print(file_path)
img = Image.open(file_path).convert('L')
wFile_name = file_path[:file_path.rfind('\\')]
img.save(wFile_name+file_id+".png")

print(wFile_name+file_id+".png")



