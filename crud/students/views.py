from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Student

from json import loads


# Create your views here.

def index_handler(request):
    return HttpResponse('Hello, DASR!')


def all_students(request):
    all_students_queryset = Student.objects.all()

    all_students_list = list()
    for student in all_students_queryset:
        all_students_list.append([student.id, student.name, student.mark])

    return render(request=request,
                  template_name='students_table.html',
                  context={'students': all_students_list})


def add_student(request):
    if request.method == 'POST':
        student_data = loads(request.body.decode('utf-8'))
        new_student = Student(name=student_data['name'], mark=student_data['mark'])
        new_student.save()
        return JsonResponse({'ok': True, 'data': student_data})
    else:
        raise Http404()


def delete_student(request, student_id):
    if request.method == 'POST':
        Student.objects.get(id=student_id).delete()
        return JsonResponse({'ok': True})
    else:
        raise Http404()


def update_student(request):
    if request.method == 'POST':
        student_data = loads(request.body.decode('utf-8'))
        name = student_data['name']
        mark = student_data['mark']
        student = Student.objects.get(id=student_data['id'])
        student.name = name
        student.mark = mark
        student.save()
        return JsonResponse({'ok': True})
    else:
        raise Http404()
