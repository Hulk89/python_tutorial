import wx

import os

# (1) osx의 user data는 보통 ~/Library/Application Support/<app_name> 에 저장한다.
APP_NAME = 'MyApp'
application_support_path = os.path.expanduser('~/Library/Application Support')
USERDATA_PATH = os.path.join(application_support_path, APP_NAME)

if __name__ == '__main__':
    app = wx.App(False) # A Frame is a top-level window.
    if not os.path.exists(USERDATA_PATH):  # (2) path가 존재하지 않으면 초기화
        os.makedirs(USERDATA_PATH, exist_ok=True)
        with open(os.path.join(USERDATA_PATH, 'user_data.txt'), 'w') as f:
            f.write("it's my first user data")
            title = "처음 실행함"
    else:
        with open(os.path.join(USERDATA_PATH, 'user_data.txt')) as f:
            title = f.read().strip()
    frame = wx.Frame(None, wx.ID_ANY, title) # Show the frame.
    frame.Show(True)

    app.MainLoop()
