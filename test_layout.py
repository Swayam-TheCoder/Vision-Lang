from paddlex import create_model
from PIL import Image, ImageDraw

image_path = "pre2.jpg"

# Load layout model
model = create_model("PP-DocLayout-L")

# Run layout detection
output = model.predict(image_path)

# Open image
image = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(image)

for res in output:
    data = res.json

    if callable(data):
        data = data()

    boxes = data["res"]["boxes"]

    for box in boxes:
        label = box["label"]
        score = box["score"]
        x1, y1, x2, y2 = box["coordinate"]

        # Draw rectangle
        draw.rectangle(
            [float(x1), float(y1), float(x2), float(y2)],
            outline="red",
            width=3
        )

        # Draw label
        draw.text(
            (float(x1), float(y1) - 20),
            f"{label} ({score:.2f})",
            fill="red"
        )

        print(
            f"{label} | "
            f"confidence: {score:.2f} | "
            f"box: {x1}, {y1}, {x2}, {y2}"
        )

# Save result
output_path = "layout_result.jpg"
image.save(output_path)

print("\n==============================")
print("Saved:", output_path)
print("==============================")