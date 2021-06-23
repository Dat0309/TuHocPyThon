#Load du lieu va chia Train, Val, Test 
from numpy import loadtxt
from sklearn.model_selection import train_test_split
from keras.models import Sequential 
from tensorflow.keras.layers import Dense

dataset = loadtxt('ping-indians-diabetes.data.csv', delimiter=',')

# print(dataset)
#DataSet là một ma trận gồm nhiều dòng, mỗi dòng sẽ gồm 2 phần:
#Phần 1: 8 giá trị đầu tiên của người dùng: INPUT.x
#Phần 2:2 giá trị cuối cùng là 0 và 1: OUTPUT.y
x = dataset[:,0:8]
y = dataset[:,8]

#Chia dataset ra, 80% sẽ là TRAIN + VAL, 20% sẽ là TEST
x_train_val, x_test, y_train_val, y_test = train_test_split(x,y,test_size=0.2)
#Lấy phần 80% ra chia tiếp ra 2 phần train và val
x_train, x_val, y_train, y_val = train_test_split(x_train_val,y_train_val,test_size=0.2)

#Xây dựng model
#Mình cho input = 8(8 số đầu), sẽ chạy qua 2 lớp, lớp đầu chứa 16 neural, lớp 2 chứa 8 neural và lớp cuối output sẽ chưa 1 neural
model = Sequential()
#input_dim tức là sẽ có 8 tham số cho mỗi bản ghi
model.add(Dense(16, input_dim=8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) 
model.build(dataset)
model.summary()