import pandas as pd 
import matplotlib.pyplot as plt 

column = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Green Lantern', 'Hawk Girl', 'Martianmanhunter', 'Green Arrow', 'Aquaman', 'Zatana', 'Hawk Man'] # when this is printed you just get a list
column2 = ['1000', '230', '790', '110', '770', '200', '600', '50', '300', '70', '250']

titled_colum = {'Hero': column,
                'Sex': ['M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'M'],
                'Key_Powers': ['Strength Speed Flight Heat Vision', 'Tech Weapons Armour', 'Strength Magic weapons', 'Speed', 'Ring', 'Wings Tech weapon', 'Strength Shapeshifting Flight Ghost', 'Tech Weapons', 'Water control Strength', 'Magic', 'Strength Tech Weapon'],
                'JL_Member': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'N'], 
                'Power_Levels': ['1000', '225', '750', '100', '700', '150', '550', '70', '290', '65', '200'], 'Alt_Power_Levels': column2,
                'Speed_Levels': ['700', '75', '110', '1000', '750', '100', '100', '75', '100', '50', '100'],
                'Stamina_Recovery': ['1000', '100', '800', '200', '600', '200', '350', '90', '320', '75', '210']}      # create a dictionary, add new variable ('titled_column') then insert that variable into DataFrame
                                                                            # this will also create a header name for the column, it will replace the 0

data = pd.DataFrame(titled_colum) # uses pandas to sort data in usable columns, can now work with columns to anyalyze data

select_powers = data['Key_Powers'][3]   # to just select a column, create a new variable 'select_powers' make it = data and use list ['Key_Powers'] adding [] brackets with a number will print specific portion of data
select_JL_Member = data['JL_Member'] 
select_row = data.iloc[7]['JL_Member']     # to select a row, create new variable 'select_row' make it = data.iloc[0], using brackets and pick which row you want, in this case 0
                                               # add second [] with desired column for specific portion

select_row2 = data.iloc[4]['Power_Levels'] # using iloc[4] will print '700' which is 'Power_Levels' column and row 4
select_row3 = data.iloc[5] # using iloc[5] will print entire column 5. So all Hawk Girl info 

#print(data['Power_Levels']) # to access specific column, use data then add specific column using []

Superman_row = data.iloc[0] 
#print(Superman_row) 
Batman_row = data.iloc[1] 
#print(Batman_row) 
WonderWoman_row = data.iloc[2]
#print(WonderWoman_row) 

# Changing data from object to float64
flt_data_chng = data['Power_Levels'] = data['Power_Levels'].astype(float) 
flt_data_chng2 = data['Alt_Power_Levels'] = data['Alt_Power_Levels'].astype(float)  
flt_data_chng3 = data['Speed_Levels'] = data['Speed_Levels'].astype(float) 
flt_data_chng4 = data['Stamina_Recovery'] = data['Stamina_Recovery'].astype(float) 

data_type = data.dtypes 
#print(data_type) 

Hero_Pwr_Level = data[['Hero', 'Power_Levels']] # selects Hero and Power_Levels column
#print(Pwr_Level) 

Compare_Pwr_Lvls = data[['Hero', 'Power_Levels', 'Alt_Power_Levels']]
Pwr_Level = data['Power_Levels'] 
Pwr_Level_Alt = data['Alt_Power_Levels']
Stam_Recover = data['Stamina_Recovery'] 


plt.plot(column, Stam_Recover, 'o')  
plt.xlabel('Heores')
plt.ylabel('Power Levels')
plt.title('D.C. Heroes')
#plt.show() 

Pwr_Level.plot(kind='bar')  
#plt.show() 

print(column2)   
