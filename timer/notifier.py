"""
タイマー終了時の通知機能
"""

import time
from rich.console import Console
import winsound

import time
console = Console()


def beep(time =300):
    # print("\a", end="", flush=True)
    try:
        winsound.Beep(1000, time)
    except Exception:
        pass
    
def notify_timeup_on_cli():
    console.print("[bold green]Timer Finished![/bold green]")
    for i in range(4):
        beep(700)
        time.sleep(1)
    beep(1500)