import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id):
    resp =  requests.get(BASE_URL+ENDPOINT+id+'/')
    #if resp.status_code in range(200,300):
    if resp.status_code == requests.codes.ok:           #this also works similar to above if statement
        print(resp.json())
    else:
        print("Something goes wrong")
id = input("Enter some ID : ")
get_resource(id)

def get_all_resource():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
#get_all_resource()

'''
#Status codes are the codes which give the information about page status
#There are 5 category of status codes..
#   1XX --> (100-199)   --->    INFORMATIONAL (eg. - continue, processing)
#   2XX --> (200-299)   --->    SUCCESSFUL
#   3XX --> (300-399)   --->    REDIRECTIONAL
#   4XX --> (400-499)   --->    CLIENT ERROR (eg. - 403 csrf token error, 403 forbidden)
#   5XX --> (500-599)   --->    SERVER ERROR (eg. - server down)
'''
'''
dumpdata concept
python manage.py dumpdata testapp.Employee          #command for get all data of Employee class
python manage.py dumpdata testapp.Employee --indent 4         #for get all data of Employee class with indentation
python manage.py dumpdata testapp.Employee --format formattype --indent 5
formattype may be ---> json/xml
#Even you can save json/xml format in file get_all_resource
python manage.py dumpdata testapp.Employee --format formattype > emp.formattype --indent 5
'''

def create_resource():
    new_emp={
    'eno':500,
    'ename':'shiva',
    'esal':500,
    'eaddr':'Chennai',
    }
    resp=requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def update_resource(id):
    new_emp={
    'esal':6000,
    'eaddr':'Delhi',
    }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(resp.status_code)
    print(resp.json())
delete_resource(7)
