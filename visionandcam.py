from google.cloud import vision
from google.cloud.vision import types
import io
import cv2
import ctypes  # An included library with Python install.   

# capture frame from a video with name "video_test.mp4"

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

vision_client = vision.ImageAnnotatorClient()
count = 0
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    cv2.imwrite("framex.jpg", frame)
    if count == 30:
      file_name = 'framex.jpg'
      with io.open(file_name, 'rb') as image_file:
          content = image_file.read()
          image = types.Image(content=content)
      response = vision_client.face_detection(image=image)
      faces = response.face_annotations
      likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                        'LIKELY', 'VERY_LIKELY')
      for face in faces:
        print(face.sorrow_likelihood)
        if face.sorrow_likelihood == 4 or face.sorrow_likelihood == 5 or face.sorrow_likelihood == 3:
          ctypes.windll.user32.MessageBoxW(0, "If you need a help, please contact: 405-xxx-xxx", "Your title", 0)
          break
        if face.anger_likelihood == 4 or face.anger_likelihood == 5 or face.anger_likelihood == 3:
          ctypes.windll.user32.MessageBoxW(0, "If you need a help, please contact: 405-xxx-xxx", "Your title", 0)
          break
      count = 0
    count+=1
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
