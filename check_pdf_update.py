import requests
import os
from datetime import datetime

PDF_URL = "https://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf"
LAST_MODIFIED_FILE = "last_modified.txt"

def get_last_modified(url):
    # HTTPヘッダで最終更新日時を取得
    response = requests.head(url)
    if 'Last-Modified' in response.headers:
        return response.headers['Last-Modified']
    return None

def get_saved_last_modified():
    # 保存した最終更新日時を読み込む
    if os.path.exists(LAST_MODIFIED_FILE):
        with open(LAST_MODIFIED_FILE, "r") as file:
            return file.read().strip()
    return None

def save_last_modified(last_modified):
    # 最終更新日時をファイルに保存
    with open(LAST_MODIFIED_FILE, "w") as file:
        file.write(last_modified)

def is_pdf_updated():
    # 現在のPDFの最終更新日時を取得
    current_last_modified = get_last_modified(PDF_URL)
    
    if not current_last_modified:
        print("PDFの最終更新日時が取得できませんでした。")
        return False
    
    # 保存した最終更新日時と比較
    saved_last_modified = get_saved_last_modified()
    if saved_last_modified != current_last_modified:
        save_last_modified(current_last_modified)
        return True  # 更新があった場合
    
    return False  # 更新なし

if __name__ == "__main__":
    if is_pdf_updated():
        print("PDFが更新されました！")
        # ここでPDFの処理を開始する（ダウンロード、画像化、Discord送信など）
    else:
        print("PDFは更新されていません。")
