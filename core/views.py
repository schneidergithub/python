from django.http import HttpResponse

def home(request):
   text = """<h1>Django python demo with github actions & AWS</h1>"""
   return HttpResponse(text)