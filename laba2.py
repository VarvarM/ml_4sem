import pandas as pd
data = pd.read_csv("adult.data.csv")
print(data['sex'].value_counts())
print('------------')
print(data[data['sex'] == 'Female'].age.describe()[1])
print('------------')
ger_data = data[data['native-country'] == 'Germany']
print(len(ger_data) / len(data))
print('------------')
more50 = data[data['salary'] == '>50K']
less50 = data[data['salary'] == '<=50K']
print('Больше 50к:',more50['age'].mean(), more50['age'].std())
print('Меньше 50к:',less50['age'].mean(), less50['age'].std())
print('------------')
ed = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
print(more50[more50['education'].isin(ed)].education.describe()[0])