# countup.py
# カウントアップ動作（プログレスバーなし）

import time
from datetime import datetime
from rich.console import Console

console = Console()

def _format_hms(total_seconds: int) -> str:
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def _format_ms(total_seconds: int) -> str:
    m = total_seconds // 60
    s = total_seconds % 60
    return f"{m:02d}:{s:02d}"

def run_countup():
    console.print("[bold green]Count-up mode started (Ctrl+C to stop)[/bold green]")
    start = datetime.now()

    try:
        while True:
            elapsed = datetime.now() - start
            sec = int(elapsed.total_seconds())

            hms = _format_hms(sec)
            ms = _format_ms(sec)
            print(f"\rElapsed: {sec} sec  |  {ms}  |  {hms}", end="", flush=True)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print()
        console.print(f"[bold cyan]Stopped at {sec} sec ({_format_ms(sec)} / {_format_hms(sec)})[/bold cyan]")

if __name__ == "__main__":
    run_countup()