import os
import random
from PIL import Image

def open_random_dinomeme(dir):
    memes = os.listdir(dir)
    selected_memes = [meme for meme in memes if meme.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    the_meme = random.choice(selected_memes)
    
    meme_dir = os.path.join(dir, the_meme)
    
    finally_the_meme = Image.open(meme_dir)
    finally_the_meme.show()

memes_dir = './memes/'

open_random_dinomeme(memes_dir)