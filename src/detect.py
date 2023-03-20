import os
import subprocess
import re
import cv2
import numpy as np
from PIL import Image



img_formats = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng']
vid_formats = ['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv']

ansi_escape = re.compile(r'''
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
''', re.VERBOSE)



class Truck:
    def __init__(self, source, project = './', output = '', conf = 0.7):
        self.source = source
        extension = os.path.splitext(source)[-1]
        if extension == "":
            raise Exception('Folder types are not supported.')
        
        if (extension not in img_formats) and (extension not in vid_formats):
            raise Exception(f'File type [{extension}] is not supported by this model.')
        

        if output == '':
            output = os.path.basename(source).replace('.', '_')
        
        detect = "../models/yolov5/detect.py"
        weightpt = "../models/yolov5m_result10/weights/best.pt"
        code = f"python {detect} --weights {weightpt} --source {source} --project {project} --name {output} --conf {conf} --save-txt --save-conf"
        process = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.process_output = process.communicate()[0].decode("utf-8")
        match1 = re.search(r"Results saved to (\S+)", self.process_output)
        self.savedloc = ansi_escape.sub('', match1.group(1))
        self.savedloc_file = os.path.join(self.savedloc, os.path.basename(source))

        return
    def cmd_output(self, plain = 1):
        result = self.process_output
        if plain:
            result = ansi_escape.sub('', result)
        return result

    def show(self, detected = 0):
        fileloc = self.savedloc_file if detected else self.source
        extension = os.path.splitext(fileloc)[-1]

        if extension in img_formats:
            img=cv2.imread(fileloc)
            cv2.imshow('rectangle',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif extension in vid_formats:
            vid = cv2.VideoCapture(fileloc)
            frameTime = 10
            while(vid.isOpened()):
                ret, frame = vid.read()
                cv2.imshow('frame',frame)
                if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                    break
            vid.release()
            cv2.destroyAllWindows()
        else:
            raise Exception('file type error')
        return
    
    def info(self, detected = 0):
        fileloc = self.savedloc_file if detected else self.source
        extension = os.path.splitext(fileloc)[-1]
        if extension in img_formats:
            image = Image.open(fileloc)
            print(f"format : {image.format}")
            print(f"mode : {image.mode}")
            print(f"size : {image.size}")
            return {"filename":image.filename,"format":image.format, 'mode':image.mode, 'size':image.size}
        
        elif extension in vid_formats:
            vid = cv2.VideoCapture(fileloc)
            h = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            w = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            print(f"format : {extension}")
            print(f"size : {(w,h)}")
            return {"filename":fileloc,"format":extension, 'size':(w,h)}
        else:
            raise Exception('file type error')
    

        


        


    








        
    
    


    
    



