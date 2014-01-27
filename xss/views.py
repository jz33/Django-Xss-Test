import datetime
from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

def current_datetime(request):
	# simple test for Django
	now = datetime.datetime.now()
	html = "<html><body>current time: %s.</body></html>" % now
	return HttpResponse(html)
	
def main(request):
	return render(request, "index_form.html")
	
def xss0(request):# Server side XSS
    if 'q' in request.GET:
        q = request.GET['q'] 
        html = '<script>alert(\''+q+'\')</script>';
        return HttpResponse(html)
    return render(request, 'xss_form0.html')
	
def xss1(request): # Normal Ouput
    if 'q' in request.GET:
        q = request.GET['q'] 
        print 'q: '+q
        fp = '127.0.0.1:8000'+ request.get_full_path();
        return render(request, 'xss_form1.html', {'query': q, 'full_path': fp})
    return render(request, 'xss_form1.html')
    
def xss2(request): # Comprehensive Escape
    if_auto = "off"
    '''
    if 'auto_on' in request.GET:
        if_auto = "on"
        '''
    if 'q' in request.GET:
        q = request.GET['q'] 
        print 'q: '+q
        fp = '127.0.0.1:8000'+ request.get_full_path();
        xss = q
        return render(request, 'xss_form2.html', \
                        {'query': q, 'full_path': fp, 'xss' :xss})
    return render(request, 'xss_form2.html', \
                        )
    
