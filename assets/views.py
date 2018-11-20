from django.shortcuts import get_object_or_404, render, redirect
from django.forms import ModelForm
# Create your views here.
from django.http import HttpResponse
from .models import Asset, Manufacturer, Office, Organization

# class Assetmodel(models.Asset):
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['organization_id', 'office_id', 'manufacturer_id', 'part_number', 'description', 'date_implemented', 'maint_notes']

def index(request):
    asset_list = Asset.objects.all()
    man_list = Manufacturer.objects.all()
    office_list = Office.objects.all()
    org_list = Organization.objects.all()
    context = {'assets': asset_list, 'manufacturers': man_list, 'offices': office_list, 'organizations': org_list}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at the assets.")

def assets(request):
    list = Asset.objects.order_by('-date_implemented')
    # list = Asset.objects.order_by('-date_implemented')[:5]
    context = {'list': list}
    return render(request, 'assets.html', context)

def search(request):
    try:
        q = request.GET['q']
        results = Asset.objects.filter(description__contains=q)
        return render(request, 'results.html', {'results': results})
    except KeyError:
        return redirect(index)

def detail(request, asset_id):
    print("detail")
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'detail.html', {'a': asset})

def edit(request, asset_id):
    print("editing")
    asset = get_object_or_404(Asset, pk=asset_id)
    form = AssetForm(request.POST or None, instance=asset)
    if form.is_valid():
        form.save()
        return redirect(index)
    return render(request, 'edit.html', {'form':form})

def delete(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    if request.method=='POST':
        asset.delete()
        return redirect(index)
    return render(request, 'delete.html', {'a': asset})