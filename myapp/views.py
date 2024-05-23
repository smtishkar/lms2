from django.shortcuts import render
from .models import Video, Site_sections, Technicians_cources, Videos, Training_parts, Training_chapters
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .services import open_file
from django.http import FileResponse, Http404

# Create your views here.

def test (request):
    return render(request, 'myapp/test.html')

def get_list_video(request):
    return render (request, 'myapp/home.html', {'video_list': Video.objects.all()})


def get_video(request,pk: int):
    _video =get_object_or_404(Video, id=pk)
    return render (request, 'myapp/video.html', {'video': _video})
                   

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def entry_page(request):
    return render(request, 'myapp/entrypage.html')


# def technicians_content(request):
#     return render(request, 'myapp/techcont.html')

def service_advisors_content(request):
    return render(request, 'myapp/sacontent.html')

# Скачать pdf
# def pdf_view(request):
#     try:
#         return FileResponse(open('test.pdf', 'rb'), content_type='myapp/pdf.html')
#     except FileNotFoundError:
#         raise Http404()
    
# Показать PDF на странице
def pdf_view(request):
    with open('test.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    
# def pdf_view(request):
#    pdf_url = "test.pdf"
# # Replace with the actual URL of your PDF file
#    return render(request, 'myapp/pdf.html', {'pdf_url': pdf_url})


def get_site_sections(request):
    # w = Site_sections.objects.all()[0]
    # print(w.image.url)
    # print(Technicians_cources.get_absolute_url)
    return render(request, 'myapp/index.html', {'sections': Site_sections.objects.all(), 'videos':Videos.objects.all()  })


def get_technician_content(request):
    # chapters = Training_chapters.objects.filter()
    cources = Technicians_cources.objects.all()
    data = {
        'cources': cources,
        # 'chapters': chapters
    }
    # print(Technicians_cources.get_absolute_url)
    return render(request, 'myapp/techcont.html', data)
    # return render(request, 'myapp/techcont.html', {'cources': Technicians_cources.objects.all()})


def get_education_part(request, part_slug):
    # part = get_object_or_404(Training_parts, slug=part_slug)
    # cources = Technicians_cources.objects.all()
    parts = Training_parts.objects.all()
    cources = get_object_or_404(Technicians_cources, slug=part_slug)
    data = {
        'parts': parts,
        'cources': cources,
    }
    # print(data)
    # print(Training_parts.objects.all())
    # w = Technicians_cources.objects.all()[4]
    # print(w.image.url)
    # print(Technicians_cources.objects.all())
    print(part_slug)

    return render(request, 'myapp/eduparts.html', data)
    # return render(request, 'myapp/eduparts.html', {'parts': Training_parts.objects.all()})


def get_training_content(request, content_slug):

    parts = Training_chapters.objects.all()
    cources = get_object_or_404(Training_parts, slug=content_slug)
    data = {
        'parts': parts,
        'cources': cources,
    }
    print(content_slug)
    print(Training_chapters.objects.all())
    p = Training_chapters.objects.all()[0]
    c = Training_parts.objects.all()[0]
    print(p.chapter)
    print(p.chapter == c.title)
    print(c.title)

    return render(request, 'myapp/educontent.html', data)
    # return render(request, 'myapp/eduparts.html', {'parts': Training_parts.objects.all()})


def get_tt_level_content(request):
    return render(request, 'myapp/tt_level.html', {'cources': Technicians_cources.objects.all(), 'videos':Videos.objects.all()})





# def embed_video(request):
#     videos = Videos.objects.all()

#     context = {
#         'videos': videos
#     }

#     return render(request, 'myapp/index.html', context)