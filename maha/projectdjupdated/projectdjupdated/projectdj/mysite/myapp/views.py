from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from myapp.forms import Postt,student_registration,posttt
from . models import ContactMessage,post
from django.contrib import messages

def home(request):
    # if request.method =='POST':
    #  fm= Postt(request.POST)
    #  if fm.is_valid():
    #     tt= fm.cleaned_data['title']
    #     bb= fm.cleaned_data['blog']
    #     # print(tt)
    #     # print(bb)

    #     reg= Post(title=tt, blog=bb)
    #     reg.save()
    #  return render(request, 'home.html', {"form":fm, "success":"Data saved successfully!"})
    # else:
    #     fm=Postt()  
    return render(request, 'home.html')
def product(request):
    posts= post.objects.all()
    return render(request,'product.html',{"posts":posts})

def aboutus(request):
    fom = student_registration()
    return render(request,'aboutus.html', {"form":fom })

def contact_view(request):
    if request.method == 'POST':
        form = Postt(request.POST)
        if form.is_valid():
            # Save the form data to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            # Render the page with a success message
            return render(request, 'contact.html', {'form': Postt(), 'success': True})
    else:
        form = Postt()

    return render(request, 'contact.html', {'form': form})


def delete(request, id):
    posts = post.objects.filter( id=id)
    if request.method == 'POST':
     posts.delete()
     messages.success(request, "Post deleted successfully!")
     if request.method != 'POST':
      messages.error(request, "Deletion must be confirmed via POST.")
     
     return HttpResponseRedirect('product.html')
    else:
     return render(request, 'delete.html', {'post': posts})
    

def addpost(request):
 
  
    if request.method == 'POST':
        form = posttt(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, "Post added successfully!")
            if not form.is_valid():
               print(form.errors)
            return HttpResponseRedirect('dashboard.html')  
       
    else:
        form = posttt()
    return render(request, 'addpost.html', {'form': form})

def updatepost(request):
    if request.method == 'POST':
        form = posttt(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, "Post added successfully!")
            if not form.is_valid():
               print(form.errors)
            return HttpResponseRedirect('dashboard.html')  
       
    else:
     form = posttt()
    
    return render(request, 'updatepost.html', {'form': form})


