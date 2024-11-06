import PIL as pl
import sys

file_path = sys.argv[1]
img = pl.Image.Ope(file_path).convert('L')
img.save("")



