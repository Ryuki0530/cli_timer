"""
現在のタイマーの実行状態を管理するモジュール
"""

import os
import json
from datetime import datetime

STATE_FILE = os.path.join(os.path.expanduser("~"), ".cli_timer_state.json")

def save_state(state: dict):
    """タイマーの状態をファイルに保存する"""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def load_state():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def clear_state():
    """保存されたタイマーの状態を削除する"""
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)

def query_status():
    state = load_state()
    if not state:
        print("No timer is running.")
        return

    if state["mode"] != "countdown":
        print("Unknown timer mode.")
        return

    end_time = datetime.fromisoformat(state["end_time"])
    remain = (end_time - datetime.now()).total_seconds()
    remain = int(remain)

    if remain <= 0:
        print("Timer is already finished.")
        clear_state()
    else:
        print(f"Remaining: {remain} sec")
