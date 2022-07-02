from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from testapp.models import Employee,testapp_user
from django.contrib.auth import authenticate,login, logout
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return  HttpResponseRedirect('http://localhost:8000/testapp/show-employee/')
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'testapp/user_login.html',data)
    else:
        return render(request,'testapp/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/testapp/login/')
def newEmployee(request):
    res=render(request,'testapp/new_employee.html')
    return res
def saveEmployee(request):
    if request.method=='POST':
        formData=request.POST
        emp=Employee()
        emp.eno=formData['eno']
        emp.ename=formData['ename']
        emp.esal=formData['esal']
        emp.eprofile=formData['eprofile']
        emp.save()
    s='http://localhost:8000/testapp/show-employee/'
    return HttpResponseRedirect(s)
def employee_info(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/testapp/login/')
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/show_employee.html',data)
    return res
def greeting(request):
    s="<h1>Good Evening Students</h1>"
    return HttpResponse(s)
def about(request):
    s="""<h1>About</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Debitis autem non unde provident, sed, laboriosam vitae quibusdam veniam ullam molestias iusto eveniet, recusandae est placeat incidunt. Dicta consequatur facere inventore cupiditate culpa saepe. Sapiente nostrum consequuntur nesciunt, ratione tenetur quidem saepe mollitia tempore quasi suscipit, facere doloribus animi voluptatibus dignissimos!
    </p>"""
    return HttpResponse(s)
def showContact(request):
    s="""<table>
            <tr>
                <td>Address</td>
                <td>73,Arjun Complex,Shivaji Nagar,Mumbai</td>
            </tr>
            <tr>
                <td>Email</td>
                <td>contact@xyz.com</td>
            </tr>
            <tr>
                <td>Phone</td>
                <td>022-6387912</td>
            </tr>
        </table>"""
    return HttpResponse(s)



