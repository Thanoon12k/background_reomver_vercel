from django.shortcuts import render
from django.http import HttpResponse
import os
from .remover import remove_bg

def Index(request):
     if request.method=='GET':
          clean()
          return render(request, 'index.html')
     elif request.method == 'POST':
          print('post:',request.POST)
          if   request.FILES.get('image_file'):
               input_path = request.FILES['image_file']

               file_path = 'media/'+'output.png'
               with open(file_path, 'wb') as f:
                    f.write(input_path.read())
               remove_bg(file_path,'output.png')
               return render(request, 'index.html',{
               'output_image':'media/'+'output.png',
               'input_image':file_path
               })
          elif 'download_image' in request.POST:
               file_path ='media/output.png'
               with open(file_path, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='audio/mp3')
                    response[f'Content-Disposition'] = f'attachment; filename="output.png"'
                    return response
     return render(request, 'index.html')


def clean():
    
    folder_path='media/'
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) :
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path} : {e}")
         