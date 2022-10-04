from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from testsystem.models import Question,exam_user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import random
def greeting(request):
    return render(request,"testsystem/greeting.html")
def signup(request):
    return render(request,"testsystem/signup.html")
def savedata(request):
    if request.method=='POST':
        formData=request.POST
        cre1=User()
        cre=exam_user()
        cre1.username=formData['username']
        cre1.set_password(formData['password'])
        cre1.save()
        cre.real_name=formData['name']
        cre.user=cre1
        cre.save()
        request.session['username']=formData['username']
        return  HttpResponseRedirect('http://localhost:8000/testsystem/test/')
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return  HttpResponseRedirect('http://localhost:8000/testsystem/test/')
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'testsystem/user_login.html',data)
    else:
        return render(request,'testsystem/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/testsystem/login/')
def test(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/testsystem/login/')
    res=render(request,'testsystem/test.html')
    return res
def question(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/testsystem/login/')  
    s=set()
    while(len(s)<5):
        s.add(random.randint(1,10))
    q={}
    l=[]
    for v in s:
        l.append(v)
    l1=[1,2,3,4,5]
    b={k:v for (k,v) in zip(l1, l)}
    
    for key,value in b.items():
        q[key]=(Question.objects.all()[value])
    o=[1,2,3,4,5]
    q[6]=o
    res=render(request,'testsystem/questions.html',q)
    return res
def result(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/testsystem/login/') 
    """q=request.POST['q1']
    print(q)
    print(list(request.POST.items()),sep="\n")
    s='yo'
    return HttpResponse(s)"""
    
    r=0
    w=0
    a=5
    
    for i in range(1,6):        
        if request.method=="POST":
            v=request.POST.get('q'+str(i))
            print(list(request.POST.items()),sep="\n")
            if v==None:
                a-=1
                continue
            if v==str(request.POST.get("answer"+str(i))):
                r+=1
            else:
                w+=1
    d={
        'a':a,
        'right':r,
        'wrong':w
    }
    return render(request,'testsystem/result.html',d)
def again_test(request):
    return HttpResponseRedirect('http://localhost:8000/testsystem/test/')
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