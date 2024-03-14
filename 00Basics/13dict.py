this_dict = {'names':['chenchu',"reddy",'siva', 'krisna','rajia','sai'],
             'age':[23, 24, 25, 26, 27, 28],
            'height':[5.6, 5.7, 5.8, 5.9, 6.0, 6.1],
            'weight':[60, 70, 80, 90, 100, 110]}
#print(this_dict)

print(this_dict['names'])
print("Keys in the dictionary:")
print(this_dict.keys())
print("Values in the dictionary:")
print(this_dict.values())
print("Items in the dictionary:")
print(this_dict.items())
print(len(this_dict))
print(len(this_dict['names']))
print(type(this_dict))
this_dict.update({'names':['Ram',"Bheem",'Lava', 'Kusa','Daana','Veera']})
print(this_dict['names'])
print(this_dict)
print(this_dict.get('names'))
print(this_dict.pop('names'))
print(this_dict)
this_dict['cities']=('Hyderabad','Bangalore','Chennai','Mumbai','Delhi','Kolkata')
this_dict.update({'states':['Telangana','Karnataka','Tamilnadu','Maharashtra','Delhi','West Bengal']})
print(this_dict)
print(this_dict.keys())

# this_dict.update()
# this_dict.pop()
# this_dict.clear()
# this_dict.index()
