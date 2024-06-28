import xml.dom.minidom
osm_file = '5.osm'
doc = xml.dom.minidom.parse(osm_file)
places = doc.getElementsByTagName('node')
count=0
count_all=0
for place in places:
    types = place.getElementsByTagName('tag')
    for type in types:
        if(type.getAttribute('k')=="shop"):
            count_all+=1
            if((type.getAttribute('v'))!="supermarket"):
                count+=1
                print(type.getAttribute('v'))
print(count)
print(f"Всего магазинов: {count_all}")