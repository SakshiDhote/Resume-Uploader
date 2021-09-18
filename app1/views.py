from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .forms import ResumeForm
from .models import ResumeModel

# Create your views here.

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=ResumeModel.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})

    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('myapp/home.html')
        return HttpResponse("Invalid")
class CandidateView(View):
    def get(self,request,pk):
        candidate=ResumeModel.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})
