from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
import overpy
from .serializers import SearchNearbySerialier
# Create your views here.

overpass = overpy.Overpass()


def query_helper(amenity, radius, lat, lon):
	query = '''
[out:json];
(
  // query part for: “aminity=*”
  node["amenity"="{amenity}"](around:{radius},{lat},{lon});

);
out;
>;
out skel qt;
	'''.format(amenity = amenity, radius = radius, lat=lat, lon=lon)	
	return query

def convert_node(node):
	data = {}
	for key in node.tags.keys():
		data[key] = node.tags[key]
	data['lat'] = node.lat
	data['lon'] = node.lon
	return data

class SearchNearby(views.APIView):
	serializer_class = SearchNearbySerialier
	def post(self, request, *args, **kwargs):
		data 		= request.data
		amenity 	= data.get('amenity') # gets the amenity
		lat 		= float(data.get('latitude')) # the location, center of the circle
		lon 		= float(data.get('longitude')) # the location, center of the circle
		radius		= int(data.get('radius'))
		print(amenity, lat, lon, radius)
		query = query_helper(amenity = amenity, radius = radius, lat=lat, lon=lon)
		res = overpass.query(query)
		print(res.nodes)
		info = []
		for node in res.nodes:
			info.append( convert_node(node) )
		return Response(info)

