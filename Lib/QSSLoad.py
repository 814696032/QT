class QSSLoad:  # 加载样式文件
    def __init__(self):
        pass
    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r', encoding='UTF-8') as file:
            return file.read()