from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE_DIR = Path(__file__).resolve().parent.parent
GENERATED_DIR = BASE_DIR / "static" / "generated"
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def get_font(size: int):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def create_comic_page(title: str, panels: list, output_name: str):
    width = 1200
    panel_width = 560
    panel_height = 420
    margin = 40
    title_height = 100

    rows = (len(panels) + 1) // 2

    height = title_height + rows * (panel_height + margin) + margin

    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)

    title_font = get_font(42)
    panel_font = get_font(24)
    small_font = get_font(20)

    draw.text(
        (margin, 25),
        title,
        fill="black",
        font=title_font,
    )

    for index, panel in enumerate(panels):
        row = index // 2
        column = index % 2

        x = margin + column * (panel_width + margin)
        y = title_height + margin + row * (panel_height + margin)

        draw.rectangle(
            (x, y, x + panel_width, y + panel_height),
            outline="black",
            width=4,
        )

        draw.text(
            (x + 15, y + 15),
            f"Panel {panel.panel_number}",
            fill="black",
            font=panel_font,
        )

        scene_text = panel.scene[:180]
        dialogue_text = panel.dialogue[:180]
        caption_text = panel.caption[:120]

        draw.text(
            (x + 15, y + 65),
            "Scene:",
            fill="black",
            font=small_font,
        )

        draw.text(
            (x + 15, y + 95),
            scene_text,
            fill="black",
            font=small_font,
        )

        draw.text(
            (x + 15, y + 220),
            f"Dialogue: {dialogue_text}",
            fill="black",
            font=small_font,
        )

        draw.text(
            (x + 15, y + 320),
            f"Caption: {caption_text}",
            fill="black",
            font=small_font,
        )

    output_path = GENERATED_DIR / output_name
    canvas.save(output_path)

    return str(output_path)