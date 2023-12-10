import os
import comfy
import folder_paths
import base64
from io import BytesIO

class Text2Image_jru:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput":False,"default":"","multiline": False}),
                "width": ("INT", {"default": 512, "min": 1, "max": 9999, "step": 1}),
                "height": ("INT", {"default": 512, "min": 1, "max": 9999, "step": 1}),
                "font": ("STRING", {"forceInput":False,"default":"/fonts/Geneva.ttf","multiline": False}),
                "size": ("INT", {"default": 24, "min": 1, "max": 9999, "step": 1}),
                "color": ("STRING", {"forceInput":False,"default":"#ffffff"}),
                "bgcolor": ("STRING", {"forceInput":False,"default":"rgba(0,0,0,0)"}),
                "align": (["lt", "rt", "mm", "lb", "rb"], {"default": "mm"}),
            }
        }
    RETURN_NAMES = ("IMAGE", )
    RETURN_TYPES = ("IMAGE", )
    OUTPUT_NODE = False
    FUNCTION = "text2img"

    CATEGORY = "JaRue"
    def text2img(self, text, width, height, font, size, color, bgcolor, align):
        from PIL import Image, ImageFont, ImageDraw
        from PIL import ImageOps
        import numpy as np
        import torch
        import textwrap
        ttf = font#r'/Users/jamestrue/AI/fonts/Geneva.ttf'
#        width = 600
#        height = 400
#        bgcolor = (255, 255, 0, 0)
        font_size = size
        font_color = color#(250, 0, 0)
        unicode_font = ImageFont.truetype(ttf, font_size)  
        txt = text#'caption here that is super long too caption here that is super long too caption here that is super long too'
        img = Image.new(mode="RGB", size=(width, height), color=bgcolor)
        draw = ImageDraw.Draw(img)  
        textbbox_val = draw.textbbox((0,0), txt, font=unicode_font)
        if (align == "lt"):
            draw.text((0,0), txt, font=unicode_font, anchor="lt")
        if (align == "rt"):
            draw.text((width,0), txt, font=unicode_font, anchor="rt")
        if (align == "mm"):
            draw.text((width/2, height/2), txt, font=unicode_font, anchor="mm")
        if (align == "lb"):
            draw.text((0, height), txt, font=unicode_font, anchor="lb")
        if (align == "rb"):
            draw.text((width, height), txt, font=unicode_font, anchor="rb")
        text = txt
#        i = Image.open('/Users/jamestrue/AI/aioracle.jpg')
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img = np.array(img).astype(np.float32) / 255.0
        img = torch.from_numpy(img)[None,]
        return (img,1)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Text2Image_jru": Text2Image_jru
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Text2Image_jru": "Text 2 Image"
}

