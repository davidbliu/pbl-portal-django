from django.shortcuts import render
from django.http import HttpResponse
from django.template import  RequestContext, loader

# Create your views here.


def home(request):
	"""
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))
	"""
	context = {'blah': 'hello this is a worthless string'}
	return render(request, 'home.html', context)

def google_auth_test(request):
	context = ""
	return render(request, 'google_auth_test.html', context)