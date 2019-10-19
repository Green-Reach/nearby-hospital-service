from rest_framework import serializers

class SearchNearbySerialier(serializers.Serializer):
	amenity 	= serializers.CharField()
	latitude 		= serializers.CharField()
	longitude 		= serializers.CharField()
	radius		= serializers.CharField()

	'''
	def validate(self, data):
		print("VALIDATING")
		if data.get('amenity') == '' or data.get('latitude') == '' or data.get('longitude') == '' or data.get('radius') == '':
			raise serializer.ValidationError('All fields should not be blank')
		return data

	def validate_latitude(self, value):
		if not int(value) >= 90 or not int(value) <= 90:
			raise serialiers.ValidationError('Latitude should be from -90 to 90')
		return value

	def validate_longitude(self, value):
		if not int(value) >= -180 or not int(value) <= 180:
			raise serialiers.ValidationError('Longitude should be from -180 to 180')
		return value

	'''