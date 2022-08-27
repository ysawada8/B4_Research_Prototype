import io
import sys

# ファイルの内容を文字列で返す
def skip_line_1(file):
    with io.StringIO() as f:
    # 標準出力を f に切り替える。
        sys.stdout = f
    # ファイルの内容を print で出力
        with open(file) as i:
            for line in i:
                print(line.strip("\n"))
        # f に出力されたものを文字列として取得
            file_str = f.getvalue()
        # 標準出力をデフォルトに戻す
            sys.stdout = sys.__stdout__
            return file_str

# ファイルの内容（2行目以降）を文字列で返す
def skip_line_2(file):
    with io.StringIO() as f:
        sys.stdout = f
        with open(file) as i:
            # 1行飛ばす
            next(i)
            for line in i:
                print(line.strip("\n"))
            file_str = f.getvalue()
            sys.stdout = sys.__stdout__
            return file_str

# ファイルの内容（3行目以降）を文字列で返す
def skip_line_3(file):
    with io.StringIO() as f:
        sys.stdout = f
        with open(file) as i:
            next(i)
            next(i)
            for line in i:
                print(line.strip("\n"))
            file_str = f.getvalue()
            sys.stdout = sys.__stdout__
            return file_str

# next(i) を増やすことで4行目以降の拡張が可能