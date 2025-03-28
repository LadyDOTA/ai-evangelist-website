from PIL import Image, ImageDraw, ImageFont
import os
import random

def create_testimonial_image(filename, initials, bg_color):
    # Create a 200x200 image with the specified background color
    img = Image.new('RGB', (200, 200), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font that's available on the system
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
    except IOError:
        try:
            font = ImageFont.truetype("Arial.ttf", 80)
        except IOError:
            # If no TrueType fonts are available, use the default bitmap font
            font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_width, text_height = draw.textsize(initials, font=font) if hasattr(draw, 'textsize') else (80, 80)
    position = ((200 - text_width) // 2, (200 - text_height) // 2)
    
    # Draw the initials in white
    draw.text(position, initials, fill="white", font=font)
    
    # Save the image
    img.save(filename)
    print(f"Created testimonial image: {filename}")

# Create testimonial images
create_testimonial_image("testimonial-1.jpg", "SJ", "#4B0082")  # Sarah Johnson - Indigo
create_testimonial_image("testimonial-2.jpg", "JW", "#006400")  # James Wilson - Dark Green
create_testimonial_image("testimonial-3.jpg", "ET", "#8B0000")  # Emma Thompson - Dark Red

print("All testimonial images created successfully!")
