from PyQt5.QtCore import QThread,pyqtSignal
import os
import cv2

class VideoCapture(QThread):
    progress = pyqtSignal(int)
    info = pyqtSignal(str)
    f = pyqtSignal(str)
    def __init__(self,file): # 这里是保存路径 和 文件名(***.mp4)
        self.working = True
        super(VideoCapture,self).__init__()
        self.file = file.split('/')[-1]
        self.dir = os.path.dirname(file)
        if not os.path.exists(self.dir+"/"+self.file[:-4]):
            os.mkdir(self.dir+"/"+self.file[:-4])
        self.output_path = self.dir+"/"+self.file[:-4]
        self.video_path = self.dir + "/" + self.file

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        vc = cv2.VideoCapture(self.video_path)
        # 初始化,并读取第一帧
        # rval表示是否成功获取帧
        # frame是捕获到的图像
        rval, frame = vc.read()
        # 获取视频fps
        fps = vc.get(cv2.CAP_PROP_FPS)
        # 获取每个视频帧数
        frame_all = vc.get(cv2.CAP_PROP_FRAME_COUNT)
        # 获取所有视频总帧数
        self.info.emit("视频FPS: {}".format(fps))
        self.info.emit("视频总帧数: {}".format(frame_all))
        # 每n帧保存一张图片
        frame_interval = 6
        # 统计当前帧
        frame_count = 0
        count = 0
        while rval and self.working:
            rval, frame = vc.read()
            if frame_count % frame_interval == 0:
                if frame is not None:
                    filename = self.output_path + "/0000{}.jpg".format(count)
                    cv2.imwrite(filename, frame)
                    self.f.emit(filename)
                    count += 1
                    # print("保存图片:{}".format(filename))
            frame_count += 1
            self.progress.emit(int(float(frame_count)/float(frame_all)*100.0))

        # 关闭视频文件
        vc.release()
        self.info.emit("总共保存：{}张图片\n".format(count))
        self.info.emit("finish")