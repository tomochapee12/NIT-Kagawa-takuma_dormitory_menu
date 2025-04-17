# NIT-Kagawa-takuma_dormitory_menu
香川高等専門学校詫間キャンパスの寮食献立をDiscordのWebhookを使用して通知するツールです。

是非forkして使ってください。

>[!TIP]
>使用するときは自分のWebhookを入力する必要があります。

## 概要
  * https://www.kagawa-nct.ac.jp/dormitoryE/kondate.pdf に献立のPDFがあるので毎日0時から4時間ごとにURLをGithub Actionsで自動的に確認し、サイトが更新されていたらPDFを画像に変換しDiscordサーバーへ通知を行うスクリプト。

## 使用方法
  1. このリポジトリをForkする（右上のForkボタンを押す）。
  2. Discordで献立を送りたいチャンネルを選び、チャンネルの編集を押す。
  3. 連携サービスのウェブフックを押し、新しいウェブフックボタンを押す。
  4. 作成されたウェブフックを選択し、ウェブフックURLをコピーを押す。
  5. Githubに戻る。リポジトリ内のSettingを押し、Secrets and variables/Actionsを押す。
  6. New repository secretを押し、NameにDISCORD_WEBHOOK_URL、Secretに4でコピーしたウェブフックURLを貼り付ける。
  7. 完成。
