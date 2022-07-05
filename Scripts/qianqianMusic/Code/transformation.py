from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['music.py', '-D','-w']
    # opts = ['TargetOpinionMain.py', '-F', '-w']
    # opts = ['TargetOpinionMain.py', '-F', '-w', '--icon=TargetOpinionMain.ico','--upx-dir','upx391w']
    run(opts)