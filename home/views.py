from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PersonSerializer


@api_view(['GET', 'POST'])
def one(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({"name": f'my name is {name}'})
    else:
        return Response({"name": 'my name is rezoo'})


@api_view()
def persons(request):
    all_persons = Person.objects.all()
    ser_data = PersonSerializer(all_persons, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
def person(request, person_id):
    try:
        one_person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "this user does not exists"}, status=status.HTTP_404_NOT_FOUND)

    serial_data = PersonSerializer(one_person)
    return Response(serial_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def person_create(request):
    info = PersonSerializer(data=request.data)
    if info.is_valid():
        data = info.validated_data
        # Person(name=data['name'], age=data['age'], email=data['email']).save()
        info.save()
        return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
