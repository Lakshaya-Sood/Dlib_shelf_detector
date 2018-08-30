import cv2
vidcap = cv2.VideoCapture('1.mp4')
# To get the version of opencv using
#(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
vidcap.set(cv2.CAP_PROP_FPS,10.00)
fps = vidcap.get(cv2.CAP_PROP_FPS)
size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(fps,size)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1