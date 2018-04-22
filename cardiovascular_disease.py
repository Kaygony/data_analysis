import numpy as np
import pandas as pd

df = pd.read_csv('data/mlbootcamp5_train.csv', sep=';', index_col='id')

df.head()
print(df.shape)
print(df.columns)

# вопрос 1
print("Вопрос 1:")
if df[df['gender'] == 1]['height'].mean() > df[df['gender'] == 2]['height'].mean():
    print("1 = man  , 2 = women")
else:
    print("1 = women , 2 = man")


# вопрос 2
print("Вопрос 2:")
if df[df['gender'] == 1]['height'].mean() > df[df['gender'] == 2]['height'].mean():
    print("more women drinking alcohol")
else:
    print("more man drinking alcohol")

# вопрос 3
print("Вопрос 3:")
smoke_proc = df[df['gender'] == 2]['smoke'].mean()/ df[df['gender'] == 1]['smoke'].mean()
print("smoke_proc = ", round(smoke_proc))

# вопрос 4
print("Вопрос 4:")
no_smoke_age = df[df['smoke'] == 0]['age'].mean()
smoke_age = df[df['smoke'] == 1]['age'].mean()
print("age difference = ", round((no_smoke_age - smoke_age)/30))

# вопрос 5
print("Вопрос 5:")
df['age_years'] = df['age']/365
first_sample = df[(df['age_years'] <= 64) & (df['age_years'] >= 60) & (df['ap_hi'] < 120) & (df['cholesterol'] == 1)]['cardio']
first_sample_count = len(first_sample.index)
print(first_sample_count)
second_sample = df[(df['age_years'] <= 64) & (df['age_years'] >= 60) & (df['ap_hi'] < 180) & (df['ap_hi'] >= 160) & (df['cholesterol'] == 3)]['cardio']
second_sample_count = len(second_sample.index)
print(second_sample_count)
dif = round(first_sample_count/second_sample_count)
print('difference = ', dif)

# вопрос 6
print("Вопрос 6:")