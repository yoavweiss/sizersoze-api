from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
import subprocess

def run(request):
    viewports = request.GET.get('viewports')
    ignore_invisibles = request.GET.get('ignore_invisibles')
    target_url = request.GET.get('target_url')
    postback_url = request.GET.get('postback_url')
    if not viewports or not ignore_invisibles or not target_url:
        return HttpResponseBadRequest("Need parameters, man!")
    viewport_list = viewports.split(',')
    processes = []
    if not postback_url:
        postback_url=""
    for viewport in viewport_list:
	processes.append(subprocess.Popen(["/opt/projects/sizersoze_api/sizersoze_api/Sizer-Soze/sizer_json.py", 
					  target_url, viewport, ignore_invisibles, postback_url],
					  stdout=subprocess.PIPE,
                   			  stderr=subprocess.PIPE))
    output = "["
    error = ""
    first = True
    for process in processes:
        out, err = process.communicate()
        if not first:
            output += ","
	first = False
        output += out
        error += err
    output += "]"

        
    #if not error:
    return HttpResponse(output, content_type="application/json")
    return HttpResponseServerError("Sorry! failed to run :'( " + error)
