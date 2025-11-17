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

def clear_state():
    """保存されたタイマーの状態を削除する"""
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
