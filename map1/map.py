import folium

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('coordinates.json','r',encoding='utf-8-sig').read())))

#adding coordinates of states(nairobi)
fg.add_child(folium.Marker(location=[1.2921, 36.8219],popup="this is were Nairobi is located  "))

#setting focus and zoom level of map
map=folium.Map(location=[1.2921, 36.8219],zoom_start=5)

map.add_child(fg)
map.save("map.html")
