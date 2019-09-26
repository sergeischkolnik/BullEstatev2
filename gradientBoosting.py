import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
from sklearn import ensemble
from sklearn.model_selection import train_test_split

data = pd.read_csv("propiedades1.csv", error_bad_lines=False, engine='python', delimiter=';')

#data['dormitorios'].value_counts().plot(kind='bar')
#plt.title('numero dormitorios')
#plt.xlabel('dormitorios')
#plt.ylabel('frecuencia')
#plt.figure(figsize=(10,10))

x = data['metrosmin'].values
y = data['UF'].values
x = x.astype(np.float)
y = y.astype(np.int)


#plt.scatter(x,y,marker='.')


# Use the 'hue' argument to provide a factor variable
#sns.lmplot(x="m", y="UF", data=data, fit_reg=False, hue='dormitorios', legend=False)

# Move the legend to an empty part of the plot
#plt.legend(loc='lower right')
#plt.title("metros vs UF")
#plt.show()



clfH = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2,
          learning_rate = 0.1, loss = 'huber')

labels = data['UF']
#conv_dates = [1 if values == 2014 else 0 for values in data.date]
#data['date'] = conv_dates

train1 = data.drop(['id', 'id2', 'nombre','fechapublicacion','fechascrap','region','direccion','precio','UF','link'],axis=1)

x_train , x_test , y_train , y_test = train_test_split(train1 , labels , test_size = 0.10,random_state = 2)



clfH.fit(x_train, y_train)
print("-----------")
print("Score Huber:")
print(clfH.score(x_test,y_test))
print("----")

# y_pred = clfH.predict(x_test)
# # print("Real vs Pred")
# # i = 0
# # for real,pred in zip(y_test,y_pred):
# #     if abs((pred-real)/real) > 0.3:
# #         print(str(real) + " vs " + str(int(pred)) + "   delta:" + str(int(100 * ((pred - real) / real))) + "%")
# #         print(x_test.iloc[i,:])
# #     i += 1


y = [[2,2,75,85,1,1,-33.407,-70.574878]]
y_precio = clfH.predict(y)
print(y_precio)