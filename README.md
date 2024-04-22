An executable of Flask app which built with Flask, BeautifulSoup, Selenium, sqlite3 and Matplotlib

Compatible with Chrome version  123.x.xxxx.xx to 124.x.xxxx.xx.

Create Executable of Python Script using PyInstaller
```
pyinstaller -F --add-binary "chromedriver.exe";"." --add-data=".\\flask.db;." --add-data=".\\TaipeiSansTCBeta-Regular.ttf;." --add-data=".\\templates\\*;.\\templates" --add-data=".\\static\\css\\*;.\\static\\css" main.py
```

[Example videos](https://youtu.be/LE5ereQ6W5U)
