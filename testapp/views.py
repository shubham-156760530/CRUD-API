from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from testapp.models import Employee
from testapp.utils import is_json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.mixins import SerializeMixin, HttpResponseMixin
from testapp.forms import EmployeeForm
import json


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailCBV(View, HttpResponseMixin):
    def get_object_by_id(self, id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource is not available'})
            return self.render_to_http_response(json_data, status=404)
        #for sending data to another web application data should be JSON format
        #firstly data should be in dictionary form then this dictionary data would be converted into JSON data
        #Converting Python dictionary to Json object is called serialization
        #Here we have only one record so it is easy to serialize data manually but what when you have to serialize 1000 records
        #for all records to serialize there is a module named serialializer inside that serialize() method
        else:
            json_data=self.serialize([emp,])
            #emp_data={
            #'eno':emp.eno,
            #'ename':emp.ename,
            #'esal':emp.esal,
            #'eaddr':emp.eaddr,
            #}                               #To converting an object from one form to another form is called serialization
            #json_data=json.dumps(emp_data)  #like here --> emp object is converting in python dictionary then in json form
        return self.render_to_http_response(json_data)
    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No matched resource found to perform updation'})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json data only'})
            return self.render_to_http_response(json_data, status = 400)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance = emp)
        if form.is_valid():
            form.save(commit=true)
            json_data = json.dumps({'msg':'resource updated'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status = 400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No matched resource found to perform deletion'})
            return self.render_to_http_response(json_data, status=404)
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Resource deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'Unable to delete....Please try again'})
        return self.render_to_http_response(json_data)



'''
<<<<<<<<<<<<<<<<<<-------------------using serialializer--------------------->>>>>>>>>>>>>>>>>
SYNTAX OF SERIALIZER >>>>>>>>> serialializer.serialize('json', queryset, fields)
FIELDS ARE OPTIONAL. FIELDS ARE USED TO SPECIFY WHICH FIELD YOU WANT TO GET
eg. - serialializer.serialize('json', qs, fields=('eno', 'ename', 'esal'))
from django.core.serialializers import serialize
def get(self, request, id, *args, **kwargs):
    emp = Employee.objects.get(id=id)
    json_data=serialize('json', [emp,])
    return HttpResponse(json_data, content_type='application/json')
'''

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(View, SerializeMixin, HttpResponseMixin):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        json_data = self.serialize(emp)
        '''json_data=serialize('json', emp)    #this will contain all the info like id, model, fields everthing
        #so for just providing fields we have to do following process
        pdict = json.loads(json_data)
        final_list = []
        for obj in pdict:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)'''
        return self.render_to_http_response(json_data)
    def post(self, request, *args, **kwargs):
        json_data=json.dumps({'msg':'this is from post'})
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json data only'})
            return self.render_to_http_response(json_data, status = 400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=true)
            json_data = json.dumps({'msg':'resource created'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status = 400)
        #return self.render_to_http_response(json_data)
        #you can give status code when return HttpResponse---> return HttpResponse(json_data, content_type='application/json', status=200)
# Create your views here.
