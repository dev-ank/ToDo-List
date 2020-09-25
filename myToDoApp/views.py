from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Content
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def home(request):
	datas=Content.objects.all().order_by("-time")
	print(datas)
	stuff_for_frontend={
		"datas":datas
	}
	return render(request,'myToDoListApp/results.html',stuff_for_frontend)


@csrf_exempt
def post_home(request):
	todo=request.POST.get("input",False)
	date=timezone.now()
	s=Content.objects.create(text=todo,time=date)
	return HttpResponseRedirect("/")
    

@csrf_exempt
def delete_post(request,todoid):
	Content.objects.get(id=todoid).delete()
	return HttpResponseRedirect("/")
    