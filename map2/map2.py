import folium
import pandas

#Here pandas is used for data analysis
data=pandas.read_csv('ke.csv',encoding="cp1252")

LAT=list(data['LAT'])
LON=list(data['LON'])
name=list(data['NAME'])
population=list(data['capacity'])
website=list(data['website'])
picture=list(data['picture'])

fg=folium.FeatureGroup('my map')
fg.add_child(folium.GeoJson(data=(open('kenya_cities.json','r',encoding='utf-8-sig').read())))

for lt,ln,nm,cp,ws,pic in zip(LAT, LON, name, population, website, picture):
    fg.add_child(folium.Marker(location=[lt,ln],popup="<b>name  : </b>"+nm+ "<br> <b>population : </b> "+str(pp)+"<br><b>wikipidea link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')))


map=folium.Map(location=[1.2921, 36.8219],zoom_start=5)

map.add_child(fg)
map.save('map2.html')
