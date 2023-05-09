
import random
file = open("cars.csv")

header = file.readline()

cost = int(input("Enter the budget ($): "))
car_cost = 0
brand = ['Acura', 'Alfa', 'AM', 'Aston', 'Audi', 'Bentley', 'BMW', 'Buick', 'Cadillac', 
         'Chevrolet', 'Chrysler', 'Dodge', 'Ferrari', 'FIAT', 'Fisker', 'Ford', 
         'Freightliner', 'Genesis', 'Geo', 'GMC', 'Honda', 'HUMMER', 'Hyundai',
         'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Lamborghini', 'Land', 'Lexus',
         'Lincoln', 'Lotus', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 
         'Mercury', 'MINI', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 
         'Porsche', 'Ram', 'Rolls-Royce', 'Saab', 'Saturn', 'Scion', 'smart', 'Subaru',
         'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']
carlist = []
for data in file:
    
    datalist = data.split(',')
    car = int(datalist[0])
    year = datalist[1]
    model = datalist[7]
    make = datalist[6]

    if car <= cost and car >= car_cost:
       car_cost = car
       if car_cost < cost and car_cost >= cost * .80 :
           carlist.append (str(str(car_cost) + " " + year + " " + make + " " + model))
for choices in range(5):
    print("$" + (str(random.choice(carlist))))

    car_cost = 0


