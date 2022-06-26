from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SerializerTodo
from .models import Todo


def homePage(request):
    return render(request, 'Index.html')
@api_view(['GET', 'POST'])
def task(request):

    if request.method == 'GET':
        tasks = Todo.objects.all()
        serializer = SerializerTodo(tasks, many = True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SerializerTodo(data=request.data)
        if serializer.is_valid() and len(request.data['task']) <= 50 and len(request.data['description']) <= 128:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(f"Error en el post, no debes superar los 50 caracteres para task (enviaste {len(request.data['task'])}) y los 128 para description (enviaste {len(request.data['description'])})")


@api_view(['GET'])
def taskDetail(request, nameTask):
    task = Todo.objects.filter(task__contains=nameTask)
    if  len(task) < 1:
        return Response ("Tarea no encontrada", status=status.HTTP_404_NOT_FOUND)
    

    elif request.method == 'GET':
        serializer = SerializerTodo(task, many = True)
        return Response(serializer.data)
    

@api_view(['GET', 'POST', 'DELETE'])
def taskPK(request, pk):

    try:
        task = Todo.objects.get(id = pk)
    except Todo.DoesNotExist:
        return Response ("Tarea no encontrada",status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SerializerTodo(task, many = False)
        return Response(serializer.data)

    elif request.method == 'POST':
        task = Todo.objects.get(id = pk)
        serializer = SerializerTodo(instance=task, data=request.data)

        if serializer.is_valid() and len(task.task) <= 50 and len(task.description) <= 128:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(f"Error en el post, no debes superar los 50 caracteres para task (enviaste {len(task.task)}) y los 128 para description (enviaste {len(task.description)})") #no logre recuperar el campo models.CharField(max_length=50) y asi no hardcodear el 50 y el 150 en el mensaje


    elif request.method == 'DELETE':
        task = Todo.objects.get(id = pk)
        task.delete()
        return Response("Se elimino correctamente la tarea.")

def notFound(request, exeption):
    return render(request, 'templates/404_Not_Found.html')