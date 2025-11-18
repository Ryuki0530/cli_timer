# CLI Timer
A command-line timer for Windows.

It supports countdown, count-up, interval notifications, and background execution.

---

## ✨ Features

### ✔ Countdown Mode
- Progress bar display  
- Remaining time display  
- Optional interval beep notifications (`-i`)  
- Beep alert when the countdown finishes

### ✔ Count-Up Mode
- Displays elapsed time only  
- Stop with Ctrl+C  
- Cannot be used in background mode

### ✔ Background Execution (Countdown Only)
- Runs the countdown timer as a background process  
- The CLI returns immediately after starting

---

## 📁 Project Structure

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

## 📦 Installation (Development)

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pyinstaller>=6.0
rich>=13.7
```

A prebuilt executable `timer.exe` is also available in the `dist` directory.  
Add the directory to your system PATH to run it from anywhere using `timer`.

---

## 🚀 Usage

### ▶ Countdown

```bash
python run_timer.py 30
```

```bash
python run_timer.py 1m30s
```

### ▶ Interval Notifications

```bash
python run_timer.py 1m --interval 10
```

A beep will sound every 10 seconds.

### ▶ Count-Up Mode (no arguments)

```bash
python run_timer.py
```

Stop with Ctrl+C.

### ▶ Background Execution (Countdown Only)

```bash
python run_timer.py 60 --background
```

Runs silently in the background.  
(No remaining-time query function)

---

## 🔊 Notification Behavior

### When Time Is Up
- 5 beeps  
- Red/Yellow flashing animation

### Interval Notification
- 1 beep

---

## 📜 License — MIT
MIT License
See the LICENSE file for details.
---

## 🙌 Contributions
Pull requests and issues are welcome.
