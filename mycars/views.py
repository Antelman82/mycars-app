from django.shortcuts import render, redirect
from .forms import YearForm, ModelTypeForm
from .models import Year, ModelType


def year_list(request):
    years = Year.objects.all().extra(
        order_by=['model_year']
    )
    return render(request, 'mycars/year_list.html', {'years': years})

def year_detail(request, pk):
    year = Year.objects.get(id=pk)
    return render(request, 'mycars/year_detail.html', {'year': year})

# @login_required
def year_create(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.save()
            return redirect('year_detail', pk=year.pk)
    else:
        form = YearForm()
    return render(request, 'mycars/year_form.html', {'form': form})

# @login_required
def year_edit(request, pk):
    year = Year.objects.get(pk=pk)
    if request.method == "POST":
        form = YearForm(request.POST, instance=year)
        if form.is_valid():
            year = form.save()
            return redirect('year_detail', pk=year.pk)
    else:
        form = YearForm(instance=year)
    return render(request, 'mycars/year_form.html', {'form': form})

# @login_required
def year_delete(request, pk):
    Year.objects.get(id=pk).delete()
    return redirect('year_list')

def modeltype_list(request):
    modeltypes = ModelType.objects.all()
    return render(request, 'mycars/modeltype_list.html', {'modeltypes': modeltypes})

def modeltype_detail(request, pk):
    modeltype = ModelType.objects.get(id=pk)
    return render(request, 'mycars/modeltype_detail.html', {'modeltype': modeltype})

# @login_required
def modeltype_create(request):
    if request.method == 'POST':
        form = ModelTypeForm(request.POST, request.FILES)
        if form.is_valid():
            modeltype = form.save()
            return redirect('modeltype_detail', pk=modeltype.pk)
    else:
        form = ModelTypeForm()
    return render(request, 'mycars/modeltype_form.html', {'form': form})

# @login_required
def modeltype_edit(request, pk):
    modeltype = ModelType.objects.get(pk=pk)
    if request.method == "POST":
        form = ModelTypeForm(request.POST, instance=modeltype)
        if form.is_valid():
            year = form.save()
            return redirect('modeltype_detail', pk=modeltype.pk)
    else:
        form = ModelTypeForm(instance=modeltype)
    return render(request, 'mycars/modeltype_form.html', {'form': form})

# @login_required
def modeltype_delete(request, pk):
    ModelType.objects.get(id=pk).delete()
    return redirect('modeltype_list')
