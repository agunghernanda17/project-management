from django.shortcuts import render
from projects_status.models import Projects_status
from django.http.response import JsonResponse
from django.core import serializers
import urllib.request
import json
from django.http import HttpResponse

#send json data before cleaned
def projects_status_json(request):
	projects_status= Projects_status.objects.all().order_by("task")
	data=serializers.serialize('json',projects_status)
	return HttpResponse(data, content_type="application/json")

#send json data after cleaned
def projects_status_json_cleaned(request):
	url = "http://127.0.0.1:8000/projects_status/json/"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	newdata=[]    
	
	for x in range(len(data)):
		for (k, v) in data[x].items():  
			if k=='fields':
				newkey=[]
				newval=[]
				for (y,z) in v.items():
					newkey.append(y)
					newval.append(z)
				zipbObj = zip(newkey, newval)
				new = dict(zipbObj)
				newdata.append(new)
				
	cleaned_data = { i : newdata[i] for i in range(0, len(newdata) ) }
	return cleaned_data


def project_not_done_yet(request,obj):
	cleaned_data = projects_status_json_cleaned(request)
	#ngambil data project
	data= Projects_status.objects.values(obj)
	temp_data=list()
	new_temp=[]
	new_userreq=[]
	list_temp=[]

	#append data agar bisa diambil via list
	for d in data:
		temp_data.append(d)

	#ngambil valuenya saja dan append lagi
	for x in range(len(temp_data)):    
		for (k, v) in temp_data[x].items():
			 new_temp.append(v)

	#ngambil data project yg belum kelar aja dan append lagi
	for x in range (len(cleaned_data)):
		for (k,v) in cleaned_data[x].items():
			if k=='is_done'and v==False:
				list_temp.append(new_temp[x])

	cleaned_data= { i : list_temp[i] for i in range(0, len(list_temp) ) }

	return cleaned_data

#fungsi buat nampilin data project yg belum kelar ke charts
def chart_admin_title(request):
	
	func=project_not_done_yet(request,'task__project_title')

	return JsonResponse(func)

#fungsi buat nampilin data user_requirements yg belum kelar ke charts
def chart_admin_userreq(request):
	func=project_not_done_yet(request,'user_requirements')

	return JsonResponse(func)

#fungsi buat nampilin data development yg belum kelar ke charts
def chart_admin_dev(request):
	func=project_not_done_yet(request,'development')

	return JsonResponse(func)

#fungsi buat nampilin data sit yg belum kelar ke charts
def chart_admin_sit(request):
	func=project_not_done_yet(request,'sit')

	return JsonResponse(func)

def chart_admin_uat(request):
	func=project_not_done_yet(request,'uat')

	return JsonResponse(func)

def chart_admin_implementation(request):
	func=project_not_done_yet(request,'implementation')

	return JsonResponse(func)

#send data to charts (chart.html)
def chart(request):
	data1= Projects_status.objects.values('task')
	data2= Projects_status.objects.values('user_requirements')
	data3= Projects_status.objects.values('development')
	data4= Projects_status.objects.values('sit')
	data5= Projects_status.objects.values('uat')
	data6= Projects_status.objects.values('implementation')
	data7= Projects_status.objects.values('task__project_title')

	task=list()
	user_requirements_data=list()
	development_data=list()
	sit_data=list()
	uat_data=list()
	implementation_data=list()
	task_data=list()
	
	for x in data1:
		task.append(x)
	for y in data2:
		user_requirements_data.append(y)
	for z in data3:
		development_data.append(z)
	for a in data4:
		sit_data.append(a)
	for b in data5:
		uat_data.append(b)
	for c in data6:
		implementation_data.append(c)
	for d in data7:
		task_data.append(d)
		
	newtask=[]
	new_user_req=[]
	new_dev=[]
	new_sit=[]
	new_uat=[]
	new_imp=[]
	new_data=[]
	
	for x in range(len(task)):    
		for (k, v) in task[x].items():
			 newtask.append(v)

	for x in range(len(user_requirements_data)):    
		for (k, v) in user_requirements_data[x].items():
			 new_user_req.append(v)

	for x in range(len(development_data)):    
		for (k, v) in development_data[x].items():
			 new_dev.append(v)

	for x in range(len(sit_data)):    
		for (k, v) in sit_data[x].items():
			 new_sit.append(v)

	for x in range(len(uat_data)):    
		for (k, v) in uat_data[x].items():
			 new_uat.append(v)

	for x in range(len(implementation_data)):    
		for (k, v) in implementation_data[x].items():
			 new_imp.append(v)

	for x in range(len(task_data)):    
		for (k, v) in task_data[x].items():
			 new_data.append(v)

	return  render(request,'chart.html',{"newtask": newtask,
	"new_user_req": new_user_req,"new_dev": new_dev,
	"new_sit": new_sit,"new_uat": new_uat,"new_imp": new_imp,
	"new_data": new_data
	})

#send data and render template
def projects_status_index(request):
	projects_status= Projects_status.objects.all().order_by("-task")
	context = {"projects_status": projects_status}
	return render(request, "projects_status_index.html", context)


