import subprocess
import sys

import pandas as pd


def _run_time_v(cmd: str) -> dict:
    """コマンドをtime -vで実行して結果をパースする。"""

    # time -vでコマンドを実行し、標準エラー出力をキャプチャ
    c = subprocess.run(
        f"time -v {cmd}",
        stderr=subprocess.PIPE,
        shell=True,
        text=True,
    )

    # 行に分割
    time_lines = c.stderr.split("\n")

    # "Elapsed (wall clock) time (h:mm:ss or m:ss): 0:07.47" のような形式を
    # キーとバリューに分ける
    time_lines_kv = [line.split(": ") for line in time_lines if ":" in line]

    # キーとバリューを辞書にして返却
    return {k.strip(): v.strip() for k, v in time_lines_kv}


def _mss_to_seconds(m_ss: str) -> float:
    """分:秒.ミリ秒形式を秒に変換する。"""
    m, ss = m_ss.split(":")
    s, ms = ss.split(".")
    return float(m) * 60 + float(s) + float(f"0.{ms}")


def _run_sample(with_gil: bool, script_name: str, n_tries: int = 10) -> None:
    """1パターンを繰り返し実行してtime -vの出力をDataFrameに変換する。

    Args:
        with_gil(bool) : GIL有効の場合、True
        script_name(str) : 同パッケージ内のテスト対象モジュール名("example1"等)
        n_tries (int) : 繰り返し実行回数
    """
    gil = "1" if with_gil else "0"
    df = None
    for i in range(n_tries):
        time_dict = _run_time_v(
            f"uv run python -X gil={gil} -m free_threading_examples.{script_name}"
        )
        if df is None:
            df = pd.DataFrame(time_dict, index=[i])
        else:
            # 縦連結する
            df = pd.concat([df, pd.DataFrame(time_dict, index=[i])])

    # 型の変換
    df["user time"] = df["User time (seconds)"].astype(float)
    df["system time"] = df["System time (seconds)"].astype(float)
    df["elapsed"] = df["Elapsed (wall clock) time (h:mm:ss or m:ss)"].apply(
        _mss_to_seconds
    )

    topics = [
        # "User time (seconds)",
        "user time",
        # "System time (seconds)",
        "system time",
        # "Elapsed (wall clock) time (h:mm:ss or m:ss)",
        "elapsed",
    ]
    for topic in topics:
        print(f"  {topic}: {df[topic].mean():.2f}")


def main():
    n_tries = int(sys.argv[1])
    print("GIL: on, example1")
    _run_sample(True, "example1", n_tries)
    print("GIL: off, example1")
    _run_sample(False, "example1", n_tries)
    print("GIL: on, example2")
    _run_sample(True, "example2", n_tries)
    print("GIL: off, example2")
    _run_sample(False, "example2", n_tries)
    print("GIL: on, example3")
    _run_sample(True, "example3", n_tries)
    print("GIL: off, example3")
    _run_sample(False, "example3", n_tries)


if __name__ == "__main__":
    main()
