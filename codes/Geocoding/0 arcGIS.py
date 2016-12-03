
# coding: utf-8

# In[2]:

import geocoder
add_list = list(open('address'))
print len(add_list)

geo_file = open('geo_file-Start from 3113','w')
geo_file.write('LineID' + '	' + 'OrignalAddress' + '	' + 'NewAddress' + '	' + 'Coordinates' + '	' + 'City' + '	' + 'State' + '	' + 'Postal' + '\n')


# In[9]:

for i in xrange(3113, len(add_list)):
    print i
    arcResult = geocoder.arcgis(add_list[i].decode('utf8'))
    print arcResult
    coordinates = arcResult.latlng
    address = arcResult.address
    gooResult = geocoder.google(coordinates, method = 'reverse')
    print gooResult
    city = gooResult.city
    postal = gooResult.postal
    state = gooResult.state
    if arcResult.status == 'OK' and gooResult.status == 'OK':
        geo_file.write(str(i) + '	' + add_list[i].strip('\n') + '	' + 
                       address + '	' + 
                       str(coordinates) + '	' + 
                       city + '	' + 
                       state  + '	' + 
                       str(postal) + '\n')
    if arcResult.status != 'OK' or gooResult.status != 'OK':
        geo_file.write(str(i) + '	' + 'NON' + '	' + 
                       'NON' + '	' + 
                       'NON' + '	' + 
                       'NON' + '	' + 
                       'NON'  + '	' + 
                       'NON' + '\n')

print 'address converting completed'
geo_file.close()

