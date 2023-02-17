from tensorflow.keras import models
import datetime
import pandas as pd


def reverse_scale(value,max,min):
    return value*(max-min) + min
def scale(value,max,min):
    return (value - min)/(max-min)


df = pd.read_excel('data.xlsx')  
# preprocessing data
dataset = df.values
for i in dataset:
    record = i[1]
    i[1] = (record.hour * 60 + record.minute) * 60 + record.second


#load_model
air_cond_model = models.load_model('air_cond_model.h5')
timenow = datetime.datetime.now()

max_temp_bef = 0
min_temp_bef = 100
max_temp_aft = 0
min_temp_aft = 100
max_day = 8
min_day = 2
max_time = 0
min_time = 86399

for i in dataset:
    if i[1] > max_time:
        max_time = i[1]
    if i[1] < min_time:
        min_time = i[1]
    if i[2] > max_temp_bef:
        max_temp_bef = i[2]
    if i[2] < min_temp_aft:
        min_temp_bef = i[2]
    if i[4] > max_temp_aft:
        max_temp_aft = i[4]
    if i[4] < min_temp_aft:
        min_temp_aft = i[4]
print(max_temp_aft)
print(min_temp_aft)
print(max_temp_bef)
print(min_temp_bef)
print(max_time)
print(min_time)
test_input = [[scale(2,max_day,min_day),scale((13 * 60 + 30) * 60 + 0,max_time,min_time),scale(21,max_temp_bef,min_temp_bef)]]
result = air_cond_model.predict(test_input)[0]
if result[0] < 0:
    result[0] = 0
elif result[0] > 1:
    result[0] = 1
else:
    result[0] = round(result[0])
result[0] = int(result[0])
result[1] = int(round(reverse_scale(result[1],max_temp_aft,min_temp_aft)))

print(result)