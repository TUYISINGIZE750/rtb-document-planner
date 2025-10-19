from PIL import Image, ImageDraw, ImageFont
import os

def create_rtb_logo():
    # Create a placeholder RTB logo
    width, height = 200, 100
    
    # Create image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw RTB text
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Draw border
    draw.rectangle([5, 5, width-5, height-5], outline='black', width=2)
    
    # Draw RTB text
    text = "RTB"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 10
    
    draw.text((x, y), text, fill='black', font=font)
    
    # Draw subtitle
    try:
        small_font = ImageFont.truetype("arial.ttf", 12)
    except:
        small_font = ImageFont.load_default()
    
    subtitle = "Rwanda Technical Board"
    bbox = draw.textbbox((0, 0), subtitle, font=small_font)
    text_width = bbox[2] - bbox[0]
    
    x = (width - text_width) // 2
    y = y + 30
    
    draw.text((x, y), subtitle, fill='black', font=small_font)
    
    # Save the logo
    img.save('rtb_logo.png')
    print("RTB logo created: rtb_logo.png")

if __name__ == "__main__":
    create_rtb_logo()