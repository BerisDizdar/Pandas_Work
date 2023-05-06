import pandas as pd 

perform = ['Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']
mydataset = {'cars':["Audi", "BMW", "Mercedes", "VW", "Ford", "Chevy", "Jaguar", "Honda", "Toyota", "Nissan", "Lexus", "Infiniti", "Acura", "Cadilac"],
             'inventory': [5, 3, 4, 11, 9, 7, 2, 12, 9, 6, 3, 2, 2, 3],
             'color':["Silver", "Grey", "Silver", "Black", "Blue", "Red", "Grey", "Silver", "Green", "Grey", "White", "Black", "Red", "Black"],
             'origin': ["Germany", "Germany", "Germany", "Germany", "America", "America", "Britain", "Japan", "Japan", "Japan", "Japan", "Japan", "Japan", "America"],
             'luxury': ["Y", "Y", "Y", "N", "N", "N", "Y", "N", "N", "N", "Y", "Y", "Y", "Y"],
             'performance': perform}   

myvar = pd.DataFrame(mydataset)


car_brand = myvar['cars'][6] # this will print the 'cars' colum, adding [] with a number will print a specific car brand
car_inventory = myvar['inventory'] 
car_color = myvar['color']
car_origin = myvar['origin'] 
car_row = myvar.iloc[7]
#print(mydataset)

print(myvar)   

 