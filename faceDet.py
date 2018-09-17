from google.cloud import vision
from google.cloud.vision import types
import io

# capture frame from a video with name "video_test.mp4"
import cv2
vidcap = cv2.VideoCapture('video_test.mp4')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frame%d.jpg" % count, image) # save frame as JPEG file 
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

# call google api to detect emotion
vision_client = vision.ImageAnnotatorClient()
for i in range(count):
    file_name = 'frame{}.jpg'.format(i)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = types.Image(content=content)
    response = vision_client.face_detection(image=image)
    faces = response.face_annotations
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    
    for face in faces:
        # print('{} anger: {}'.format(i,likelihood_name[face.anger_likelihood]))
        if face.anger_likelihood == 4 or face.anger_likelihood == 5:
            print('If you need a help, please contact: 405-xxx-xxx')
            break




# vision_client = vision.ImageAnnotatorClient()
# file_name = 'picture.jpeg'

# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#     image = types.Image(content=content)

# response = vision_client.face_detection(image=image)
# faces = response.face_annotations

# likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                        'LIKELY', 'VERY_LIKELY')

# for face in faces:
#     print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#     print('joy: {}'.format(likelihood_name[face.joy_likelihood]))