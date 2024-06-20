from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from myapp.forms import CertificationAppointmentForm,TrainingAppointmentForm
from .models import Video, Site_sections, Technicians_cources, Videos, Training_parts, Training_chapters, Certification_appointment, Training_shedule, Training_participants, Content, Edu_Results
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .services import open_file
from django.http import FileResponse, Http404
from django.contrib import messages
from django.db.models import Count
from users.models import User

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

@login_required
def get_site_sections(request):
    sections = Site_sections.objects.all()
    # section_slug = get_object_or_404(Technicians_cources, slug=part_slug)
    # section_slug = Technicians_cources.objects.all()
    data = {
        'sections': sections,
        # 'section_slug': section_slug,
    }
    # print(w.image.url)
    # print(Technicians_cources.get_absolute_url)
    # return render(request, 'myapp/index.html', {'sections': Site_sections.objects.all(), 'videos':Videos.objects.all()  })
    return render(request, 'myapp/index.html', data)


def get_technician_content(request, part_slug):             ## переименовать метод т.к. он не только для механиков
    # chapters = Training_chapters.objects.filter()
    cources = Technicians_cources.objects.all()
    slug_area = get_object_or_404(Site_sections, slug=part_slug)
    certifications= Certification_appointment.objects.all()
    trainings = Training_shedule.objects.all()
    # trainings = Training_shedule.objects.order_by().values('training_id').distinct()
    participants = Training_participants.objects.values('training_id').annotate(the_count=Count('training_id'))
    # print (trainings)
    # print (participants)
    data = {
        'cources': cources,
        'slug_area': slug_area,
        'certifications': certifications,
        "trainings": trainings,
        "participants": participants
        # 'chapters': chapters
    }
    # print(data)
    # print(w.image.url)
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
    print(parts)
    print(cources)
    # print(data)
    # print(Training_parts.objects.all())
    # w = Technicians_cources.objects.all()[4]
    # print(w.image.url)
    # print(Technicians_cources.objects.all())
    # print(part_slug)

    return render(request, 'myapp/eduparts.html', data)
    # return render(request, 'myapp/eduparts.html', {'parts': Training_parts.objects.all()})


def get_training_content(request, content_slug):

    parts = Training_chapters.objects.all()
    cources = get_object_or_404(Training_parts, slug=content_slug)
    contents = Content.objects.all()
    edu_results_list = Edu_Results.objects.filter(username=request.user)


    data = {
        'parts': parts,
        'cources': cources,
        'contents': contents,                   # Не понятно зачем это тут
        'edu_results_list': edu_results_list
    }
    # print(content_slug)
    # print(Training_chapters.objects.all())
    # p = Training_chapters.objects.all()[0]
    # c = Training_parts.objects.all()[0]
    # print(p.chapter)
    # print(p.chapter == c.title)
    # print(c.title)
    print(cources)
    return render(request, 'myapp/educontent.html', data)
    # return render(request, 'myapp/eduparts.html', {'parts': Training_parts.objects.all()})



def get_content_to_study(request, fin_content_slug):

    parts = Training_chapters.objects.all()
    cources = get_object_or_404(Training_chapters, slug=fin_content_slug)
    # print(cources)
    contents = Content.objects.all()
    try:
        edu_results_list = Edu_Results.objects.filter(username=request.user).get(title=fin_content_slug)
    except:
        edu_results_list = Edu_Results.objects.create(
            username = request.user.username,
            title = fin_content_slug,
            )
        edu_results_list.save()
        print('запись добавлена')
    edu_results_list = Edu_Results.objects.filter(username=request.user)
    data = {
        'cources': cources,
        'contents': contents,
        'parts': parts,
        'edu_results_list': edu_results_list
    }
    return render(request, 'myapp/content.html', data)
    # return render(request, 'myapp/eduparts.html', {'parts': Training_parts.objects.all()})





def get_tt_level_content(request):
    return render(request, 'myapp/tt_level.html', {'cources': Technicians_cources.objects.all(), 'videos':Videos.objects.all()})



def make_cert_appointment(request,app_id):
    appointment = Certification_appointment.objects.get(pk=app_id)
    if request.method == 'POST':
        form = CertificationAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            # appointment.job_title = request.POST.get('job_title')
            appointment.save()
            appointment.is_available = False
            appointment.save()
            messages.success(request, 'some text')
            # return redirect('/', pk=appointment.pk)
    else:
        form = CertificationAppointmentForm()
        # messages.error(request, 'Что-то пошло не так!!!')

    data = {
        'form': form,
        # 'messages': messages
        # 'cert_data': cert_data
    }

    return render(request, 'myapp/certappform.html', data)


def make_training_appointment(request,app_id):
    appointment = Training_shedule.objects.get(pk=app_id)
    print(appointment.training_id)
    print(app_id)

    training_id = appointment.training_id
    training_name = appointment.training_name
    training_start_date = appointment.training_start_date
    training_end_date = appointment.training_end_date
    # actual_num_participants = 
    max_participants = appointment.max_participants
    is_published = appointment.is_published
    is_available = appointment.is_available
    print(training_start_date)
    temp = Training_participants(training_id = appointment.training_id, training_name = appointment.training_name, training_start_date = appointment.training_start_date, training_end_date = appointment.training_end_date)
    # temp = Training_shedule(training_id = appointment.training_id, training_name = appointment.training_name, training_start_date = appointment.training_start_date, training_end_date = appointment.training_end_date, is_published = appointment.is_published, is_available = appointment.is_available, max_participants=appointment.max_participants)
    # appointment = Training_shedule.objects.get()
    if request.method == 'POST':
        form = TrainingAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            temp.dlr=form.cleaned_data['dlr']
            temp.employee_id = form.cleaned_data['employee_id']
            temp.employee_name = form.cleaned_data['employee_name']
            temp.employee_last_name = form.cleaned_data['employee_last_name']
            # appointment.job_title = request.POST.get('job_title')
            temp.save()
            # form.save()
            # appointment.save()
            # appointment.actual_num_participants = appointment.actual_num_participants+1
            # appointment.save()
            messages.success(request, 'some text')
            # return redirect('/', pk=appointment.pk)
    else:
        form = TrainingAppointmentForm()
        # messages.error(request, 'Что-то пошло не так!!!')

    data = {
        'form': form,
        # 'messages': messages
        # 'cert_data': cert_data
    }

    return render(request, 'myapp/trainingappform.html', data)


# def embed_video(request):
#     videos = Videos.objects.all()

#     context = {
#         'videos': videos
#     }

#     return render(request, 'myapp/index.html', context)

def test_pdf(request):

    temp = Content.objects.all()

    data = {
            'temp': temp
        }
    return render(request, 'myapp/test.html', data)

