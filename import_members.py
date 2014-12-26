import os
import yaml
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'portal.settings'
application = get_wsgi_application()

from django.contrib.auth.models import User
from members.models import Member


#
# create members for all members in backup yaml file
#
yaml_input = open("rails_members.yaml", 'r')
yaml_input = yaml.load(yaml_input)

for member in yaml_input:
	#
	# create a new member
	#
	mem = Member(id= int(member['old_id']), name=member['name'], google_id = member['google_uid'])
	mem.save()
	
print type(yaml_input)
