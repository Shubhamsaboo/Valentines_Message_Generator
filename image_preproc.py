import textwrap
from PIL import Image, ImageFont, ImageDraw 

def generate_card(caption):

    # Load the card template 
    image = Image.open("card_template.png")

    # Wrap the caption text by breaking it into lines
    wrapper = textwrap.TextWrapper(width=45) 
    word_list = wrapper.wrap(text=caption) 
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    # Select the text font & size
    title_font = ImageFont.truetype('font.ttf', 45)

    # Make the image ediatable 
    image_editable = ImageDraw.Draw(image)

    # Add text to the image
    image_editable.multiline_text((1180,1110), caption_new, (0, 0, 0), title_font, align="center", spacing=20)

    return image

