import requests

PDF_URL = "https://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf"
WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # GitHub ActionsでSECRETにする

def download_pdf(url, filename="kondate.pdf"):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename

def post_to_discord(filename, webhook_url):
    with open(filename, "rb") as f:
        files = {
            "file": (filename, f, "application/pdf")
        }
        data = {
            "content": "今週の献立表です 📅"
        }
        response = requests.post(webhook_url, data=data, files=files)
        response.raise_for_status()

if __name__ == "__main__":
    pdf_file = download_pdf(PDF_URL)
    post_to_discord(pdf_file, WEBHOOK_URL)
