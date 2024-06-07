from PIL import Image, ImageDraw, ImageFont

# Créer une nouvelle image avec un fond coloré
width, height = 800, 600
image = Image.new('RGB', (width, height), 'skyblue')

# Créer un objet de dessin
draw = ImageDraw.Draw(image)

# Dessiner un rectangle
rectangle_start = (50, 50)
rectangle_end = (250, 150)
draw.rectangle([rectangle_start, rectangle_end], outline='black', fill='green')

# Dessiner un cercle
circle_center = (400, 300)
circle_radius = 50
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius, 
              circle_center[0] + circle_radius, circle_center[1] + circle_radius], 
              outline='black', fill='red')

# Ajouter du texte
text = "Hello, NestJS and Angular!"
font_size = 30
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()
text_position = (50, 500)
draw.text(text_position, text, fill='black', font=font)

# Sauvegarder l'image
image_path = "/mnt/data/nestjs_angular_image.png"
image.save(image_path)

image.show()  # Afficher l'image (utile pour un environnement local)

image_path
