from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import json

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submitorder(request):
    #print "got order %s"%request
    print "Data %s"%request.POST['xml']
    print "Email %s"%request.POST['email']
    try:
        send_mail('FDA Test Server', '%s'%request.POST['xml'], 'mamurray@uvic.ca', ['%s'%request.POST['email']], fail_silently=False)
    except Exception as e:
        print "Exception occured %s"%e
    return HttpResponse(json.dumps({"result":"submitted"}))
