
# coding: utf-8

# In[4]:



import geocoder
add_list = list(open('address'))
print len(add_list)

geo_file = open('geo_file-left','w')
geo_file.write('LineID' + '	' + 'OrignalAddress' + '	' + 'NewAddress' + '	' + 'Coordinates' + '	' + 'City' + '	' + 'State' + '	' + 'Postal' + '\n')

LeftIDList = list(open('Left LineID', 'r'))

for i in LeftIDList:
    i = int(i.strip())
    print i
    gooGeoResult = geocoder.google(add_list[i].decode('utf8'))
    print gooGeoResult
    coordinates = gooGeoResult.latlng
    address = gooGeoResult.address
    gooReverse = geocoder.google(coordinates, method = 'reverse')
    print gooReverse
    city = gooReverse.city
    postal = gooReverse.postal
    state = gooReverse.state
    if gooGeoResult.status == 'OK' and gooReverse.status == 'OK':
        geo_file.write(str(i) + '	' + add_list[i].strip('\n') + '	' + 
                       str(address) + '	' + 
                       str(coordinates) + '	' + 
                       str(city) + '	' + 
                       str(state)  + '	' + 
                       str(postal) + '\n')
    if gooGeoResult.status != 'OK' or gooReverse.status != 'OK':
        geo_file.write(str(i) + '	' + add_list[i].strip('\n') + '	' + 
                       'NON' + '	' + 
                       'NON' + '	' + 
                       'NON' + '	' + 
                       'NON'  + '	' + 
                       'NON' + '\n')

print 'address converting completed'
geo_file.close()


# In[ ]:



