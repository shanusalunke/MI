from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import forms

def welcome(request):
	'''
	View for welcome screen 
	'''
	# If form is already submitted
	if request.method == 'POST' or request.method =='GET': 
		form = forms.Login(request.POST)
		if form.is_valid(): 
			# Process the data in form.cleaned_data
			responseurl = '/home/' + form.cleaned_data['username'] + '/' ; 
			return HttpResponseRedirect(responseurl)
	else:
        	form = forms.Login() # An unbound form

	return render_to_response('welcome.html', {'form': form}, context_instance=RequestContext(request))

def home(request, user):
	'''
	View for User's Home Page
	Authenticaltion required
	'''
	return render_to_response('home.html', {'Username':user})

def compose(request):
	'''
	View for the compose screen
	Add parameters to take subject and recepients list
	in case of 'reply'
	'''
	#To be added: compose/new and compose/reply

	# If form is already submitted
	if request.method == 'POST' or request.method =='GET': 
		form = forms.Compose(request.POST)
		if form.is_valid(): 
			# Process the data in form.cleaned_data
			return HttpResponseRedirect('/compose/')
	else:
        	form = forms.Login() # An unbound form

	return render_to_response('compose.html', {'form': form}, context_instance=RequestContext(request))


def archives(request):
	'''
	View for the archives
	'''
	return render_to_response('archives.html')

def lists(request):
	'''
	View for rendering all available lists
	? Need user_id to access user's subscribed lists 
	'''
	return render_to_response('lists.html')

def profile(request):
	'''
	View for User Profile
	'''
	return render_to_response('profile.html')

def newuser(request):
	'''
	View for New User Sign Up Sheet
	'''
	if request.method == 'POST': 
		form = forms.SignUp(request.POST)
		if form.is_valid(): 
		    	# Process the data in form.cleaned_data
			return HttpResponseRedirect('/thanks/')
	else:
        	form = forms.SignUp() # An unbound form

	return render_to_response('signup.html', {'form': form}, context_instance=RequestContext(request))

