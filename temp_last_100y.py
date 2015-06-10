
import matplotlib.pyplot as plt
from pprint import pprint
import wbpy

c_api = wbpy.ClimateAPI()
iso_and_basin_codes = ["PE","CL","BO"]
dataset = c_api.get_instrumental(data_type="tas", interval="year", locations=iso_and_basin_codes)
dataset

colors = list("cbg")

for data_dict in dataset.as_dict().values():
   x = data_dict.keys()
   y = data_dict.values()
   plt.scatter(x,y,s=25, marker='s', color=colors.pop())

plt.legend(dataset.as_dict().keys())

plt.xlabel('Tiempo')
plt.ylabel('Temperatura Promedio (Grados Centigrados)')

plt.xlim(1901,2012)
plt.ylim(6,30)
plt.show()


