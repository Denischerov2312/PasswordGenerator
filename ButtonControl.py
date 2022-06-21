import webbrowser
from design import UiMainwindow

URL = r'https://goo.su/Gv1QUz'


class ButtonControl:
    def __init__(self):
        pass

    @staticmethod
    def exit(self):
        exit()

    @staticmethod
    def open_url(self, url):
        webbrowser.open(url)


