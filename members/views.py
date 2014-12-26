from django.shortcuts import render
from django.contrib.auth.models import User
from members.models import Member
# Create your views here.


def list_members(request):
	member_list = Member.objects.all()
	context = {'member_list':member_list}
	return render(request, 'members/list_members.html', context)
def view_users(request):
	print "i am running the view users method right now"
	user_list = User.objects.all()
	print user_list
	context = {'user_list': user_list}
	return render(request, 'members/view_users.html', context)

