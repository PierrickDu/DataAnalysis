from Analysis import Analysis
from File import File
import matplotlib.pyplot as plt

test = File("Clients_test.csv")
test.cleaning()
anal = Analysis(test)
print(anal.desc)
#anal.plot('sexe')
#anal.plot('age')
print(test.df['age'].values)
test.df.plot(x='age', y='taux', kind='bar')
#test.df.plot.scatter(x='age', y='taux', c = 'red')
plt.show()

