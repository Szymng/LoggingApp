from django.shortcuts import redirect, render
from .models import File
from .forms import FileForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

# Create your views here.

@login_required
def file_list(request):
    files = File.objects.all()
    return render(request, 'uploader/filelist.html', {'files': files})

@login_required
def UploadFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/uploader/filelist')
    else:
        form = FileForm()
    return render(request, 'uploader/fileupload.html', {'form': form})

@login_required
def DeleteFile(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk = pk)
        file.delete()
    return redirect('/uploader/filelist')
    
    
