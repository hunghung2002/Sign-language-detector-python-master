from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 36
dataset_size = 50

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Thu thập dữ liệu cho lớp học {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Chuyển frame từ OpenCV (BGR) sang định dạng của Pillow (RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # Vẽ văn bản bằng Pillow
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.truetype("arial.ttf", 30)

        draw.text((100, 50), 'Sẵn sàng chưa? Nhấn "Q" !!!', font=font, fill=(204, 255, 223))

        # Chuyển lại từ Pillow (RGB) sang OpenCV (BGR)
        frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
