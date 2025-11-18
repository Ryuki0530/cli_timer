"""
エントリポイント
"""

import argparse
import sys

from .utils import parse_time_string
from .countdown import run_countdown
from .countup import run_countup
from .state import query_status
from .background import launch_background


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("time", nargs="?", help="例: 30, 1m30s。空ならカウントアップモード。")
    ap.add_argument("-b", "--background", action="store_true",
                    help="バックグラウンド実行（カウントダウンのみ）")
    ap.add_argument("-i", "--interval", type=int,
                    help="指定秒ごとに音で通知")
    # ap.add_argument("-q", "--query", action="store_true",
    #                 help="バックグラウンド状態の問い合わせ")

    args = ap.parse_args()

    # # 状態問い合わせ
    # if args.query:
    #     query_status()
    #     return

    # カウントアップ
    if not args.time:
        if args.background:
            print("Count-up cannot run in background.")
            return
        run_countup()
        return

    # 時間文字列変換
    try:
        seconds = parse_time_string(args.time)
    except Exception as e:
        print(f"Error: {e}")
        return

    # バックグラウンド
    if args.background:
        launch_background([sys.argv[0], args.time] + (["-i", str(args.interval)] if args.interval else []))
        print("Timer started in background.")
        return

    # 通常カウントダウン
    run_countdown(seconds, args.interval, background=False)