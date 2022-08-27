import subprocess
from timeout_decorator import timeout, TimeoutError # python3 -m pip install timeout-decorator または conda install -c conda-forge timeout-decorator

id = 0

def func():
    cmd = './a.out'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if proc.poll() is None:
        global id
        id = proc.pid
    out = proc.communicate()
    out = out[0]
    out = str(out, 'utf-8')
    return out

def ex_func():
    subprocess.run('kill ' + str(id),shell=True) # 子プロセスを終了させる
    #subprocess.run('ps -l',shell=True) # 実行中のプロセス一覧を表示
    out = 'timeout'
    return out

@timeout(1) # タイムアウトの時間設定
def main():
    try:
        out_str = func()
        return out_str
    except TimeoutError:
        out_str = ex_func()
        return out_str

if __name__ == "__main__":
    main()