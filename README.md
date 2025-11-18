# CLI Timer
Windows 用コマンドラインタイマーです。

カウントダウン、カウントアップ、インターバル通知、バックグラウンド実行に対応しています。

---

## ✨ 機能

### ✔ カウントダウンモード
- 進行バー表示  
- 残り時間の表示  
- 指定間隔でのビープ通知（`-i`）  
- 時間到達時にビープ音で通知

### ✔ カウントアップモード
- 経過時間のみを表示  
- Ctrl+C で終了  
- バックグラウンドモードでは使用できません。

### ✔ バックグラウンド実行（カウントダウンのみ）
- カウントダウンタイマーをバックグラウンドプロセスとして生成します。  
- CLIは実行後即座に解放されます。

---

## 📁 プロジェクト構成

```
cli-timer/
├─dist/
│  └─ timer.exe
│
├─ timer/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ countdown.py
│  ├─ countup.py
│  ├─ state.py
│  ├─ notifier.py
│  ├─ utils.py
│  └─ background.py
│
├─ run_timer.py
├─ requirements.txt
└─ README.md
```

---

## 📦 開発用インストール

```bash
pip install -r requirements.txt
```

`requirements.txt` の内容：

```
pyinstaller>=6.0
rich>=13.7
```
また、distディレクトリ内にビルド済みの実行ファイル `timer.exe` があります。
シェルのPATHに追加すれば、どこからでも `timer` コマンドで実行できます。
---

## 🚀 使い方

### ▶ カウントダウン

```bash
python run_timer.py 30
```

```bash
python run_timer.py 1m30s
```

### ▶ インターバル通知

```bash
python run_timer.py 1m --interval 10
```

10秒ごとにビープ通知が鳴ります。

### ▶ カウントアップ（引数なし）

```bash
python run_timer.py
```

Ctrl+C で停止。

### ▶ バックグラウンド実行（カウントダウンのみ）

```bash
python run_timer.py 60 --background
```

バックグラウンドで静かに動作します。  
（残り時間の問い合わせ機能はありません）

---


---

## 🔊 通知仕様

### 時間到達時
- 5回ビープ  
- 赤／黄色の点滅アニメーション

### インターバル通知
- 1回ビープ

---

## 📜 ライセンス — MIT
MIT License
詳しくは、 LICENSE ファイルをご覧ください。

## 🙌 コントリビューション
PR・Issue を歓迎します。  

