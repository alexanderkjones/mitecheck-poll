from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Personal

# FormView vs render()?
class PersonalView(FormView):
	template_name = 'index.html'
	form_class = PersonalForm
	success_url = '/results/'

	def form_valid(self, form):
		# What is the syntax and components here?
		return super(PersonalView, self).form_valid(form)
