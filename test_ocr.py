from paddleocr import PaddleOCR

ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_server_det",
    text_recognition_model_name="PP-OCRv5_server_rec",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

image_path = "pre3.jpg"

result = ocr.predict(image_path)

for res in result:

    # Get OCR data
    data = res.json

    if callable(data):
        data = data()

    ocr_data = data["res"]

    texts = ocr_data["rec_texts"]
    boxes = ocr_data["rec_polys"]

    # -----------------------------------
    # Create OCR items
    # -----------------------------------

    items = []

    for text, box in zip(texts, boxes):

        x1 = min(point[0] for point in box)
        y1 = min(point[1] for point in box)

        x2 = max(point[0] for point in box)
        y2 = max(point[1] for point in box)

        items.append({
            "text": text,
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2),
            "center_y": (float(y1) + float(y2)) / 2
        })

    # -----------------------------------
    # Sort top → bottom
    # -----------------------------------

    items.sort(key=lambda x: x["center_y"])

    # -----------------------------------
    # Group into lines
    # -----------------------------------

    lines = []

    Y_THRESHOLD = 12

    for item in items:

        matched_line = None

        for line in lines:

            if abs(item["center_y"] - line["center_y"]) <= Y_THRESHOLD:
                matched_line = line
                break

        if matched_line:

            matched_line["items"].append(item)

            matched_line["center_y"] = sum(
                i["center_y"] for i in matched_line["items"]
            ) / len(matched_line["items"])

        else:

            lines.append({
                "center_y": item["center_y"],
                "items": [item]
            })

    # -----------------------------------
    # Sort each line LEFT → RIGHT
    # -----------------------------------

    for line in lines:
        line["items"].sort(key=lambda x: x["x1"])

    # -----------------------------------
    # Print structured output
    # -----------------------------------

    print("\n==============================")
    print("STRUCTURED OCR TEXT")
    print("==============================")

    for line in lines:

        parts = []

        for item in line["items"]:
            parts.append(item["text"])

        print("    ".join(parts))

    # -----------------------------------
    # Confidence
    # -----------------------------------

    scores = ocr_data["rec_scores"]

    if len(scores) > 0:

        average_confidence = sum(scores) / len(scores)

        print("\n==============================")
        print(
            f"Average OCR Confidence: "
            f"{average_confidence * 100:.2f}%"
        )
        print(f"Text Regions: {len(scores)}")
        print("==============================")