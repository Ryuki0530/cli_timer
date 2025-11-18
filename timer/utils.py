import re

def parse_time_string(s: str) -> int:
    """
    "1m30s", "90s", "2m", "45" などを秒に変換する。
    """
    s = s.strip().lower()

    m = re.match(r"(\d+)m(\d+)s", s)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))

    m = re.match(r"(\d+)m$", s)
    if m:
        return int(m.group(1)) * 60

    m = re.match(r"(\d+)s$", s)
    if m:
        return int(m.group(1))

    if s.isdigit():
        return int(s)

    raise ValueError(f"Invalid time format: {s}")
