# Fix encoding issue by removing the arrow symbol and retry with default font for compatibility
#  python test for visuals

from PIL import Image, ImageDraw, ImageFont

# Create image with larger size for wallpaper
width, height = 1800, 1000
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Load fonts (fallback to default)
try:
    font_title = ImageFont.truetype("arial.ttf", 70)
    font_sub = ImageFont.truetype("arial.ttf", 50)
    font_text = ImageFont.truetype("arial.ttf", 40)
except:
    font_title = font_sub = font_text = ImageFont.load_default()

# Colors
colors = {
    "purple": (148, 0, 211),
    "blue": (0, 102, 204),
    "green": (0, 153, 76),
    "pink": (255, 20, 147),
    "orange": (255, 140, 0),
    "gray": (80, 80, 80)
}

# Title
draw.text((width//2 - 300, 40), "MY SUCCESS ROADMAP", font=font_title, fill=colors["purple"])

# Sections with color blocks
sections = [
    ("PHASE 1 (Now to Dec)", [
        "✅ Build Beyond MVP",
        "✅ Hunt for Jobs & Grants",
        "✅ Daily 90-Day Plan Execution",
        "Goal: Stability + First Users"
    ], colors["blue"]),

    ("PHASE 2 (Jan to Mar)", [
        "✅ Scale Beyond MVP",
        "✅ Apply for Grants & Funding",
        "✅ Start Basic Marketing",
        "Goal: Traction + Small Funding"
    ], colors["green"]),

    ("PHASE 3 (Apr to Jun)", [
        "✅ Launch Beauty Brand Concept",
        "✅ Add Booking Features",
        "✅ Seek Strategic Investors",
        "Goal: Growth + Brand Presence"
    ], colors["orange"]),

    ("NEXT STEP", [
        "✅ Explore Forex / Other Income Streams",
        "✅ Expand Business Portfolio",
        "Goal: Financial Freedom"
    ], colors["pink"])
]

# Draw sections
x_start = 80
y_start = 200
box_width = 800
box_height = 170
spacing_y = 200

for i, (title, items, color) in enumerate(sections):
    y = y_start + i * spacing_y
    draw.rectangle([x_start, y, x_start + box_width, y + box_height], outline=color, width=5)
    draw.text((x_start + 20, y + 10), title, font=font_sub, fill=color)
    for j, item in enumerate(items):
        draw.text((x_start + 30, y + 60 + j * 40), item, font=font_text, fill=colors["gray"])

# Save updated roadmap
output_path = "/mnt/data/success_roadmap_colorful_v2.png"
img.save(output_path)
output_path