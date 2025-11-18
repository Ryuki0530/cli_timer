"""
でバックグラウンド起動するためのラッパー
"""

import subprocess
import sys

def launch_background(args):
    subprocess.Popen([sys.executable] + args, creationflags=subprocess.CREATE_NO_WINDOW)
