from PIL import Image, ImageDraw, ImageFont
import numpy as np
from sklearn.cluster import KMeans
import os

def extract_colors(image_path, num_colors):
    image = Image.open(image_path)
    image = image.convert("RGB")

    image_array = np.array(image)

    pixels = image_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)

    return colors

def generate_color_palette(colors):
    palette = []
    for color in colors:
        palette.append((color[0], color[1], color[2]))

    return palette

def save_color_palette(palette, output_path):
    with open(output_path, "w") as f:
        for color in palette:
            f.write(f"{color[0]} {color[1]} {color[2]}\n")

    print(f"Color palette saved to {output_path}")

def save_palette_image(palette, image_output_path, swatch_size=100):
    num_colors = len(palette)
    palette_image = Image.new("RGB", (swatch_size * num_colors, swatch_size))

    for i, color in enumerate(palette):
        color_rgb = tuple(int(c) for c in color)
        for x in range(i * swatch_size, (i+1) * swatch_size):
            for y in range(swatch_size):
                palette_image.putpixel((x, y), color_rgb)
    
    palette_image.save(image_output_path)
    print(f"Palette image saved to {image_output_path}")

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    num_colors = int(input("Enter the number of colors to extract: "))
    save_same_folder = input("Do you want to save the palette in the same folder as this script? (y/n): ").strip().lower()

    if save_same_folder == 'y':
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "palette_output.txt")
    else:
        output_path = input("Enter the full path (including filename) to save the color palette file: ")
    
    colors = extract_colors(image_path, num_colors)
    palette = generate_color_palette(colors)
    save_color_palette(palette, output_path)
    image_output_path = os.path.splitext(output_path)[0] + "_image.png"
    save_palette_image(palette, image_output_path)

    input("Press Enter to exit...")

    os.startfile(output_path)
    os.startfile(image_output_path)

    exit()