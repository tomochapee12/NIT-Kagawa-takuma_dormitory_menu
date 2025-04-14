import requests
from pdf2image import convert_from_path
import os

PDF_URL = "https://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def download_pdf(url, filename="kondate.pdf"):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = f"page_{i+1}.png"
        image.save(image_path, "PNG")
        image_paths.append(image_path)
    return image_paths

def post_images_to_discord(image_paths, webhook_url):
    for image_path in image_paths:
        with open(image_path, "rb") as f:
            files = {
                "file": (image_path, f, "image/png")
            }
            data = {
                "content": "今週の献立表 🥢"
            }
            response = requests.post(webhook_url, data=data, files=files)
            response.raise_for_status()

if __name__ == "__main__":
    pdf_path = download_pdf(PDF_URL)
    image_paths = convert_pdf_to_images(pdf_path)
    post_images_to_discord(image_paths, WEBHOOK_URL)
