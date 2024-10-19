from django.shortcuts import render,redirect,get_object_or_404
from .models import Study
from .forms import StudyForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

@login_required
def main_view(request):
    studies = Study.objects.all()
    return render(request,'studies/main_view.html',{'studies':studies})

def add_study(request):
    if request.method == 'POST':
        study_form=StudyForm(request.POST)
        if study_form.is_valid():
            study_form.save()
            return redirect("main_view")
    else:
        study_form=StudyForm()
    return render(request,'studies/add_study.html',{'study_form':study_form})

def edit_study(request,pk):
    study= get_object_or_404(Study,pk=pk)
    if request.method=='POST':
        edit_form=StudyForm(request.POST,instance=study)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('main_view')
    else:
        edit_form = StudyForm(instance=study)
    return render(request,'studies/edit_study.html', {'edit_form':edit_form})
# Create your views here.
def view_study(request,pk):
    study= get_object_or_404(Study,pk=pk)
    return render(request,'studies/view_study.html',{"st":study})
def delete_study(request,pk):
    study= get_object_or_404(Study,pk=pk)
    study.delete()
    return redirect('main_view')





