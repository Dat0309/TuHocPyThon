import os
import cv2 as cv
import numpy as np

#Nên để các file cần đọc ở chung ổ đĩa cài đặt python, trong quá trình đọc file sẽ không bị lỗi!

#Tạo một mảng chứa tên của các đối tượng cần định dạng, tên này phải trùng với tên tệp chứa ảnh của mấy thằng đó
people= ['Hai', 'Trong Dat', 'stranger', 'Tri']
#Đường dẫn tới tệp chứa tất cả ảnh
DIR=r'C:\Users\ADMIN\Desktop\face'

#Đường dẫn tới file haar cascade, là thư viện dùng để nhận diện khuôn mặt
haar_cascade = cv.CascadeClassifier(r'C:\Users\ADMIN\Desktop\haar_face.xml')

#Tạo 2 mảng, 1 mảng chứa đặc điểm nhận dạng của mỗi đối tượng (feature), một mảng chứa tên của các đối tượng (label)
features = []
labels = []

def create_train():
    #Đọc từng đường dẫn của các thư mục có tên trong mảng people, thêm tên vào mảng label
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        #Trả về một danh sách chứa tên của các thư mục trong thư mục được đưa ra bởi đường dẫn
        for img in os.listdir(path):
            img_path= os.path.join(path,img)

            #đọc ảnh trong các thư mục có trong đường dẫn
            img_array = cv.imread(img_path)
            #chuyển màu ảnh thành màu xám để tiến hành nhận dạng
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            #Sử dụng thư viện haar_cascade.detectMultiScale(image, scaleFactor, minNeighbor)
            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)


            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

#Xuất thông báo đang training :))
print('training done ..........................')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train
face_recognizer.train(features,labels)

#mã hóa các tệp đã train để sử dụng trong file main
face_recognizer.save('face_trained.yml')
np.save('feature.npy', features)
np.save('labels.npy',labels)