
# 처음 build 시...

`pyinstaller app.py --add-data 'assets/*.*:assets' --windowed --noconsole --onefile`

# 그 다음...

`pyinstaller app.spec`
