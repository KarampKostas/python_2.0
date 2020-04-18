from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm , LoginStudentForm
from .models import Student
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages

# def student_create_view(request):
#    my_form = RawStudentForm()
#    if request.method =="POST":
#         το request.POST κανει το validation απο μονο του δωσμενο
#         απο την django
#         my_form = RawStudentForm(request.POST)
#        if my_form.is_valid():
#            print(my_form.cleaned_data)
#             τα ** κανουν τη φορμα να περασει σαν arguments
#            Student.objects.create(**my_form.cleaned_data)
#        else: 
#            print(my_form.errors)
#    context = {
#        "form":my_form
#    }        
#    return render(request, 'studentcreation.html', context)
def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()

    context = {
        'form':form

    }    
    return render(request, "studentcreation.html", context)

 
# παιρνει το id μεσω του object και δινει πληροφορια
#για το συγκεκριμενο object μεσω της σελιδα του student
# με χρηση href βλεπε στα html
def student_grade_view(request, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        "object": obj
    }
    return render(request, 'vathmologia.html', context)

#αναπαρασταση στοιχειων σε λιστα και μεταφορα σε μια 
# συγκεκριμενη σελιδα μεσω της λιστας    (στην html σελιδα ο τροπος)
 
def student_list_view(request):
    queryset = Student.objects.all()#lista stoixwn
    context = {
        "object_list" : queryset
    }
    return render(request, 'student.html', context)

#αν θελησω να διαγραψω ενα αντικειμενο απο  τη βαση μου

def student_delete_view(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {
        "object": obj
    }    

    return render(request, "delete.html", context)

def home_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Hello World </h1>")
    return render(request, "home.html",)

def add(request, id):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result =  int(val1 + val2)
   
    obj = get_object_or_404(Student, id=id)
    context = {
        "object": obj,
        "res":result
       }
    
    return render(request ,'vathmologia.html', context)

def teacher_view(request,*args, **kwargs):
    return render(request, "teacher.html")  

def login_view(request):
    #next = request.GET.get('next')
    form = LoginStudentForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        # if next:
        #     return redirect(next)
        return redirect('/')     

    context = {
        'form' : form
    }           

    return render(request, "login.html", context)  

# def logout_view(request):
#     auth.logout(request)   
#     return redirect('/')    


def student_view(request,*args, **kwargs):
    my_students = {
        "name": "mj",
        "my_list": ["asd", "fasd", "afsd"]
    }
    return render(request, "student.html", my_students)