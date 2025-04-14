from pdf2image import convert_from_path
from PIL import Image
import os

PDF_URL = "https://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def download_pdf(url, filename="kondate.pdf"):
    import requests
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def combine_images_vertically(images):
    # 画像のサイズを取得
    widths, heights = zip(*(i.size for i in images))
    
    # 合計高さと最大幅を計算
    total_height = sum(heights)
    max_width = max(widths)
    
    # 新しい画像を作成
    combined_image = Image.new("RGB", (max_width, total_height))
    
    # 各画像を縦に並べて合成
    current_height = 0
    for img in images:
        combined_image.paste(img, (0, current_height))
        current_height += img.height
    
    return combined_image

def post_image_to_discord(image, webhook_url):
    from io import BytesIO
    from requests import post

    # 画像をメモリに保存
    with BytesIO() as image_binary:
        image.save(image_binary, format="PNG")
        image_binary.seek(0)
        
        files = {
            "file": ("kondate.png", image_binary, "image/png")
        }
        data = {
            "content": "今週の献立表 🥢"
        }
        response = post(webhook_url, data=data, files=files)
        response.raise_for_status()

if __name__ == "__main__":
    # PDFのダウンロードと画像変換
    pdf_path = download_pdf(PDF_URL)
    images = convert_pdf_to_images(pdf_path)

    # 画像を縦に結合
    combined_image = combine_images_vertically(images)

    # Discordに送信
    post_image_to_discord(combined_image, WEBHOOK_URL)
