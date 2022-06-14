
 '''
import math


#the diameter of the fillament is the nozzle diameter
#ength of the filament used for printing,
def print_hi(dencity,diameter, lenght, price):
    cost=dencity*math.pi*pow((diameter/2),2)*lenght*price
    return cost;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print(print_hi(1,3.8,4.7,67.6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

MATERIAL_VOLUME_USED=24593
 '''