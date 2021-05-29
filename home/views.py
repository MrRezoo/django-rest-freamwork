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
    return Response(ser_data.data)


@api_view()
def person(request, person_id):
    try:
        one_person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "this user does not exists"})

    serial_data = PersonSerializer(one_person)
    return Response(serial_data.data)
