from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

from .models import Visit, Study, GroupSet, Group, SampleType
from .forms import VisitForm, StudyForm, GroupForm, SampleTypeForm, GroupSetForm

# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated:
        study = Study.objects.all()
        visits = Visit.objects.all().order_by('order')
        sampletypes = SampleType.objects.all()
        groups = Group.objects.all()
        groupsets = GroupSet.objects.all()
        visitcount = Visit.objects.all().count()
        return render(request, 'index_fabric.html', {'visits':visits, 'study':study, 'visitcount':visitcount, 'sampletypes':sampletypes, 'groups':groups, 'groupsets':groupsets})
        
@login_required
def new_visit(request):
    if request.method == "POST":
        visit = Visit(number=1)
        form = VisitForm(instance=visit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VisitForm()
    return render(request, "new_visit_form.html", {'form': form})

@login_required
def edit_visit(request, pk):
    obj = get_object_or_404(Visit, pk=pk)
    form = VisitForm(request.POST or None, instance=obj)
    
    if request.method == "POST":
        
        if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                form.save_m2m()
                return redirect('index')
    
    else:
        form = VisitForm(instance=obj)
        
    return render(request, 'edit_visit_form.html', {"form": form})
    
def remove_visit(request, pk):
    object = get_object_or_404(Visit, pk=pk)
    object.delete()
    
    return render(request, 'confirm_deletion.html')
    
@login_required
def edit_study(request, pk):
    obj = get_object_or_404(Study, pk=pk)
    form = StudyForm(request.POST or None, instance=obj)
    
    if request.method == "POST":
        
        if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                return redirect('index')
    
    else:
        form = StudyForm(instance=obj)
        
    return render(request, 'edit_study_form.html', {"form": form})
    
@login_required
def edit_sampletp(request, pk):
    obj = get_object_or_404(SampleType, pk=pk)
    form = SampleTypeForm(request.POST or None, instance=obj)
    
    if request.method == "POST":
        
        if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                form.save_m2m()
                return redirect('index')
    
    else:
        form = SampleTypeForm(instance=obj)
        
    return render(request, 'edit_sampletype_form.html', {"form": form})
    
def remove_sampletp(request, pk):
    object = get_object_or_404(SampleType, pk=pk)
    object.delete()
    
    return render(request, 'confirm_deletion.html')
    
@login_required
def new_sampletp(request):
    if request.method == "POST":
        sampletype = SampleType()
        form = SampleTypeForm(instance=sampletype, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SampleTypeForm()
    return render(request, "new_sampletype_form.html", {'form': form})
    
@login_required
def new_group(request):
    if request.method == "POST":
        group = Group()
        form = GroupForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GroupForm()
    return render(request, "new_group_form.html", {'form': form})
	
@login_required
def edit_group(request, pk):
    obj = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=obj)
    
    if request.method == "POST":
        
        if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                form.save_m2m()
                return redirect('index')
    
    else:
        form = GroupForm(instance=obj)
        
    return render(request, 'edit_group_form.html', {"form": form})
	
def remove_group(request, pk):
    object = get_object_or_404(Group, pk=pk)
    object.delete()
    
    return render(request, 'confirm_deletion.html')