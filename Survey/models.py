from django.db import models
from django import forms
from django.forms import ModelForm

# Address
# from "Save Geolocation based on Address" snippet (https://djangosnippets.org/snippets/2976/)
import json, urllib

"""
def getLatLon(address):
	address = urllib.quote_plus(address)
	geo = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % (address))
	return geo.read()

class Address(models.Model):
	street = models.CharField(max_length=40)
	city = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=10)

	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)

	def save(self, *args, **kwargs):
		geo = json.loads(getLatLon("%s,%s,%s" % (self.address, self.city, self.postcode)))
		if geo['status'] == "OK":
			self.latitude = geo['results'][0]['geometry']['location']['lat']
			self.longitude = geo['results'][0]['geometry']['location']['lng']
		super(directory_list, self).save(*args, **kwargs)
		#according to comment on snippet page, 'directory_list' must be 'location'


class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields = ['street', 'city', 'zipcode']
"""

# Personal info
class Personal(models.Model):
	timestamp = models.DateTimeField('date submitted')
	survey_date = models.DateField('date surveyed')
	user_email = models.EmailField(max_length=254)

class PersonalForm(ModelForm):
	class Meta:
		model = Personal
		fields = ['timestamp', 'survey_date', 'user_email']

"""
class Survey(forms.Form):

		# Should the timestamp be somewhere else?
		# auto_now=False, auto_now_add=True
	date_submitted = forms.DateTimeField('date submitted')
	date_surveyed = forms.DateField('date surveyed')
	user_email = forms.EmailField(max_length=254)
		#how to model set this address? there's only documentation on postal address via models, not forms
	user_address = Address

	#mite count
	mite_count1 = forms.IntegerField(label='Hive 1', max_length=3) #validate for number
	mite_count2 = forms.IntegerField(label='Hive 2', max_length=3)
	mite_count3 = forms.IntegerField(label='Hive 3', max_length=3)
	mite_count4 = forms.IntegerField(label='Hive 4', max_length=3)
	mite_count5 = forms.IntegerField(label='Hive 5', max_length=3)
	mite_count6 = forms.IntegerField(label='Hive 6', max_length=3)
	mite_count7 = forms.IntegerField(label='Hive 7', max_length=3)
	mite_count8 = forms.IntegerField(label='Hive 8', max_length=3)

	#action taken
	actions_choices = (
			(nothing, 'Nothing'),
			(drone_comb_removal, 'Drone Comb Removal'),
			(break_brood_cycle, 'Break Brood Cycle'),
			(mite_treatment, 'Mite Treatment'),
		)
	actions_taken = forms.ChoiceField(label='What did you to after sampling?', choice=actions_choices)

	#treatment used
	treatment_choices = (
			(apiguard, 'Apiguard')
			(apistan, 'Apistan')
			(apivar, 'Apivar')
			(apilifevar, 'ApiLifeVar')
			(checkmite, 'CheckMite+')
			(hopguard, 'Hop Guard')
			(mite_away_quick_strips, 'Mite Away Quick Strips')
			(oxalic_acid, 'Oxalic Acid')
			(formic_acid, 'Formic Acid')
			(powdered_sugar, 'Powdered Sugar')
			(other, 'Other')
		)
	treatment_used = forms.ChoiceField()
"""