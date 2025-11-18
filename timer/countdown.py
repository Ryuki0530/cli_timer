# countdown.py

import time
from datetime import datetime, timedelta
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TextColumn
from rich.console import Console

from .state import save_state, clear_state
from .notifier import beep, notify_timeup_on_cli

console = Console()

def run_countdown(seconds: int, interval: int, background: bool):
    start = datetime.now()
    end = start + timedelta(seconds=seconds)

    if background:
        save_state({
            "mode": "countdown",
            "end_time": end.isoformat(),
            "interval": interval,
        })
        return

    console.print(f"[bold green]Countdown started ({seconds} seconds)[/bold green]")

    last_notify = time.time()

    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        expand=True,
        console=console,
    ) as progress:

        task = progress.add_task("TIMER", total=seconds)

        while not progress.finished:
            now = datetime.now()
            remain = (end - now).total_seconds()

            # ここでは終了処理を行わずループだけ回す
            progress.update(task, completed=seconds - int(max(remain, 0)))

            if interval and time.time() - last_notify >= interval:
                beep()
                last_notify = time.time()

            time.sleep(0.1)


        progress.update(task, completed=seconds)
        
    notify_timeup_on_cli()
    clear_state()

if __name__ == "__main__":
    run_countdown(10, 5, False)  # テスト用に10秒カウントダウン、5秒ごとに通知
