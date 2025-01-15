import os
from PIL import Image, ImageDraw, ImageFont

def generate_char_image(font, char, char_bbox):
    char_width = char_bbox[2] - char_bbox[0]
    char_height = char_bbox[3] - char_bbox[1]
    
    char_image = Image.new("RGBA", (char_width, char_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(char_image)

    draw.text(
        (-char_bbox[0], -char_bbox[1]),
        char,
        font=font,
        fill=(255, 255, 255, 255)
    )

    return char_image.crop(char_image.getbbox())

def convert_font(ttf_path, font_size, output_dir="font_chars"):
    if not os.path.exists(ttf_path):
        raise FileNotFoundError(f"Font file not found: {ttf_path}")
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    chars = "笨蛋"
    font = ImageFont.truetype(ttf_path, font_size)

    for char in chars:
        char_bbox = font.getbbox(char)
        char_image = generate_char_image(font, char, char_bbox)
        output_path = os.path.join(output_dir, f"{ord(char):04x}.png")
        char_image.save(output_path)

convert_font("font.ttf", 64)