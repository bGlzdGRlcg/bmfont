import os
from PIL import Image, ImageDraw, ImageFont

def generate_char_image(font, char, char_bbox):
    if not char_bbox:
        return None
        
    char_width = max(1, char_bbox[2] - char_bbox[0])
    char_height = max(1, char_bbox[3] - char_bbox[1])
    
    char_image = Image.new("RGBA", (char_width, char_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(char_image)

    draw.text(
        (-char_bbox[0], -char_bbox[1]),
        char,
        font=font,
        fill=(255, 255, 255, 255)
    )

    bbox = char_image.getbbox()
    if not bbox:
        return None
    return char_image.crop(bbox)

def convert_font(ttf_path, font_size, output_dir="font_chars"):
    if not os.path.exists(ttf_path):
        raise FileNotFoundError(f"Font file not found: {ttf_path}")
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    chars = "没救了萝莉控鲲爱莲说炼铜涩好怪早中晚上安哦喵猫小大不要开房出透超怀孕欸嘿喜欢杂鱼幼女穴叶月吃掉够下头病娇把玩坏变成人态笑草萌呜谢神奇干想为戒敏感能那里停耳朵摸华叭咕发情冲动身体睡觉脸和智乃哭具视奸欧金肉棒高潮魅魔白毛精液勃起恋童癖男娘海星老婆"
    font = ImageFont.truetype(ttf_path, font_size)

    for char in chars:
        char_bbox = font.getbbox(char)
        char_image = generate_char_image(font, char, char_bbox)
        if char_image:
            output_path = os.path.join(output_dir, f"{ord(char):04x}.png")
            char_image.save(output_path)

if __name__ == "__main__":
    convert_font("font.ttf", 64)
