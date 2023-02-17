from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

df = pd.read_excel('data.xlsx')  
# preprocessing data
dataset = df.values
for i in dataset:
    record = i[1]
    i[1] = (record.hour * 60 + record.minute) * 60 + record.second

#scale
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(dataset)

X_train, X_test = train_test_split(X_scale,test_size=0.3,random_state=101)

train_data = X_train[:,:3]
label_data = X_train[:,3:]

test_data = X_test[:,:3]
label_test_data = X_test[:,3:]

print(train_data.shape)
print(label_data.shape)
print(test_data.shape)
print(label_test_data.shape)

model = Sequential()
# input layer
model.add(Dense(3,activation='relu'))

#hidden layer
model.add(Dense(8,activation='relu'))
model.add(Dense(4,activation='relu'))

#output layer
model.add(Dense(2))

model.compile(optimizer='adam',loss='mse')

model.fit(x=train_data,y=label_data,validation_data=(test_data,label_test_data),epochs=50)
model.save('air_cond_model.h5')
