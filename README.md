# free-threading-examples

Python 3.13で実験的に追加されたフリースレッドモードを動かしてみるプログラムです。

- example1.py: 乱数を1千万個生成して/dev/nullに書き込む(スレッドなし)
- example2.py: 乱数を1千万個生成して/dev/nullに書き込む処理を4スレッドで並列に実行
- example3.py: 乱数を1千万個生成してファイルに書き込む処理を4スレッドで並列に実行
- example4.py: 乱数を1千万個生成して/dev/nullに書き込む処理を4プロセスで並列に実行
- example5.py: 乱数を1千万個生成してファイルに書き込む処理を4プロセスで並列に実行
- measure.py: 上記のプログラムの実行時間をtimeコマンドで計測し、平均を表示

実行方法(30回平均の例)

    uv run python -X gil=1 -m free_threading_examples.measure 30
