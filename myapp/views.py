import random
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from myapp.forms import CertificationAppointmentForm,TrainingAppointmentForm
from .models import Video, Site_sections, Technicians_cources, Videos, Training_parts, Training_chapters, Certification_appointment, Training_shedule, Training_participants, Content, Edu_Results, Cert_Results, Info, QuesModel, QuesModel, Edu_programs
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




def service_advisors_content(request):
    return render(request, 'myapp/sacontent.html')


def pdf_view(request):
    with open('test.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    


@login_required
def get_site_sections(request):
    sections = Site_sections.objects.all()

    data = {
        'sections': sections,

    }

    return render(request, 'myapp/index.html', data)

@login_required
def get_technician_content(request, part_slug):             ## переименовать метод т.к. он не только для механиков

    cources = Technicians_cources.objects.all()
    slug_area = get_object_or_404(Site_sections, slug=part_slug)
    certifications= Certification_appointment.objects.all()
    trainings = Training_shedule.objects.all()
    online_certifications = Edu_programs.objects.all()
    edu_results = Edu_Results.objects.filter(username=request.user)
    cert_results = Cert_Results.objects.filter(user_id=request.user)  

    participants = Training_participants.objects.values('training_id').annotate(the_count=Count('training_id'))

    print (cert_results)
    data = {
        'cources': cources,
        'slug_area': slug_area,
        'certifications': certifications,
        "trainings": trainings,
        "participants": participants,
        'online_certifications': online_certifications,
        'edu_results': edu_results,
        'cert_results': cert_results      

    }

    return render(request, 'myapp/techcont.html', data)


@login_required
def get_education_part(request, part_slug):
    parts = Training_parts.objects.all()
    cources = get_object_or_404(Technicians_cources, slug=part_slug)
    data = {
        'parts': parts,
        'cources': cources,
    }
    print(parts)
    print(cources)


    return render(request, 'myapp/eduparts.html', data)


@login_required
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

    print(cources)
    return render(request, 'myapp/educontent.html', data)



@login_required
def get_content_to_study(request, fin_content_slug):

    parts = Training_chapters.objects.all()
    cources = get_object_or_404(Training_chapters, slug=fin_content_slug)

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






def get_tt_level_content(request):
    return render(request, 'myapp/tt_level.html', {'cources': Technicians_cources.objects.all(), 'videos':Videos.objects.all()})


@login_required
def make_cert_appointment(request,app_id):
    appointment = Certification_appointment.objects.get(pk=app_id)
    if request.method == 'POST':
        form = CertificationAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment.save()
            appointment.is_available = False
            appointment.save()
            messages.success(request, 'some text')

    else:
        form = CertificationAppointmentForm()


    data = {
        'form': form,

    }

    return render(request, 'myapp/certappform.html', data)

@login_required
def make_training_appointment(request,app_id):
    appointment = Training_shedule.objects.get(pk=app_id)
    print(appointment.training_id)
    print(app_id)

    training_id = appointment.training_id
    training_name = appointment.training_name
    training_start_date = appointment.training_start_date
    training_end_date = appointment.training_end_date

    max_participants = appointment.max_participants
    is_published = appointment.is_published
    is_available = appointment.is_available
    print(training_start_date)
    temp = Training_participants(training_id = appointment.training_id, training_name = appointment.training_name, training_start_date = appointment.training_start_date, training_end_date = appointment.training_end_date)

    if request.method == 'POST':
        form = TrainingAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            temp.dlr=form.cleaned_data['dlr']
            temp.employee_id = form.cleaned_data['employee_id']
            temp.employee_name = form.cleaned_data['employee_name']
            temp.employee_last_name = form.cleaned_data['employee_last_name']

            temp.save()

            return redirect ('success_appointment')
    else:
        form = TrainingAppointmentForm()

    data = {
        'form': form,
    }

    return render(request, 'myapp/trainingappform.html', data)


def test_pdf(request):

    temp = Content.objects.all()

    data = {
            'temp': temp
        }
    return render(request, 'myapp/test.html', data)

@login_required
def success_appointment(request):
    return render(request, 'myapp/success_appointment.html')

@login_required
def certification_results(request):
    profile = User.objects.get(username=request.user)
    cert_results = Cert_Results.objects.all()
    data = {
            'cert_results': cert_results,
            'profile': profile
        }

    return render(request, 'myapp/certification_results.html', data)



@login_required
def get_team(request):
    profile = User.objects.get(username=request.user)
    dlr = profile.dlr
    teams = User.objects.filter(dlr=dlr).order_by('last_name')
    print(dlr)
    cert_results = Cert_Results.objects.all()
    
    data = {
            'teams': teams,
            'profile': profile,
            'cert_results': cert_results
        }

    return render(request, 'myapp/team.html', data)


@login_required
def get_info(request):
    info = Info.objects.all()
    data = {
            'info': info,

        }

    return render(request, 'myapp/info.html', data)

@login_required
def get_info_details (request, info_slug):
    concreate_news = Info.objects.filter(slug=info_slug)
    print(concreate_news)
    data = {
        'info': concreate_news,

    }
    return render(request, 'myapp/info_details.html', data)



@login_required
def quiz_start_page(request):
    quantity_of_question = 1 # Тут жестко задаем количество вопросов в тесте
    full_quiz_list =[]
    final_quiz_list = []
    answer_list = []
    quiz = QuesModel.objects.all().values()


    for i in quiz:
        full_quiz_list.append(i)
    # print(full_quiz_list)
    
    for i in range(0, quantity_of_question):               
        question_id = full_quiz_list[random.randint(0, len(full_quiz_list)-1)]
        final_quiz_list.append(question_id)
        full_quiz_list.remove(question_id)

    print('final_quiz_list')
    print(final_quiz_list)


    data = {
        'quiz': final_quiz_list,
        'answer_list': answer_list
    }
    return render(request, 'myapp/quiz_start_page.html', data)




@login_required
def quiz(request, cert_area):
    print(cert_area)
    print ('-'* 200)
    quantity_of_question = 3 # Тут жестко задаем количество вопросов в тесте
    full_quiz_list =[]
    # final_quiz_list = []
    answer_list = []
    # quiz = QuesModel.objects.all().values()
    quiz = QuesModel.objects.filter(cert_area_test = cert_area).values()
    quiz_result = []
    res_dict ={}
    global test
    global final_quiz_list 
    ttl_count = 0
    right_count = 0
    final_score = 0

    cert_result = Cert_Results.objects.filter(user_id=request.user).filter(cerification_name = cert_area).filter(cert_status='Active').count()
    if cert_result == 0:
        # print ('вы уже сдавали тест')
        if request.method == 'GET':
            final_quiz_list = []
            for i in quiz:
                full_quiz_list.append(i)
                    # print(full_quiz_list)
                    
            for i in range(0, quantity_of_question):               
                question_id = full_quiz_list[random.randint(0, len(full_quiz_list)-1)]
                final_quiz_list.append(question_id)
                full_quiz_list.remove(question_id)
            test = final_quiz_list  

            print('final_quiz_list')
            print(final_quiz_list)
            data = {
            'quiz': final_quiz_list,
            'answer_list': answer_list
        }
            return render(request, 'myapp/quiz.html', data)

        if request.method == 'POST':
            for i in test:
                print(i)
                for key,values in i.items():
                    if key == 'id':
                        # print(key)
                        res = values
                        # print(res)
                        obj = QuesModel.objects.get(id=str(res))
                        print(obj)
                        # answer_boxes = request.POST.get(str(obj))
                        # answer_list = request.POST.getlist('question')
                        answer_list = request.POST.get(str(obj.question))
                        # print (str(obj.question))
                        res_dict['id'] = obj.pk
                        # print(obj.pk)
                        res_dict['question'] = obj.question
                        res_dict['user_answer'] = answer_list
                        res_dict['right_answer'] = obj.answer
                        quiz_result.append(res_dict)
                        res_dict ={}


            for i in quiz_result:
                print(i)
                # for key,values in i.items():

                        # print(key)
                user_answer = i['user_answer']
                right_answer = i['right_answer']
                if user_answer == right_answer:
                    print('Вы ответили правильно!')
                    right_count +=1
                else: print ('не верно')
                # print(user_answer)
                # print(right_answer)        
                ttl_count +=1
                final_score = round(((right_count / ttl_count) * 100),1)

                

            # print    
            # print(type(right_count))
            # print(type(ttl_count))
            print(type(final_score))
            print(final_score)

            print('правильных ответов:', right_count)
            print('Всего вопросов:', ttl_count)
            # print('результат:' , final_score)
            print('это результаты')
            print(quiz_result)
            data = {
                'quiz_result': quiz_result,
                'ttl_count': ttl_count,
                'right_count': right_count,
                'final_score': final_score
            }        
            if final_score > 80:
                try:
                    cert_result = Cert_Results.objects.filter(user_id=request.user).get(cerification_name=cert_area)
                    return render(request, 'myapp/quiz_result.html', data)
                except:
                    cert_result = Cert_Results.objects.create(
                        user_id = request.user.username,
                        cerification_name = cert_area,
                        status = 'OK',
                        score = final_score,
                        cert_status = 'Active'
                        
                    )
                    return render(request, 'myapp/quiz_result.html', data)
            else:
                cert_result = Cert_Results.objects.create(
                        user_id = request.user.username,
                        cerification_name = cert_area,
                        status = 'NOK',
                        score = final_score,
                        cert_status = 'Active'
                    )
                return render(request, 'myapp/quiz_result.html', data)
                # print ('поздравляю')
                        # print(answer_boxes)   
                        # answer_list.append(answer_boxes)
            # print('это тест')
            # print(test)



        

        # data = {
        #     'quiz': final_quiz_list,
        #     'answer_list': answer_list
        # }
        return render(request, 'myapp/quiz.html', data)
    else:
        return render(request, 'myapp/quiz_result.html')

    # print('full_quiz_list')
    # print(full_quiz_list)
    

    # ------------------------
    # for i in final_quiz_list:
    #     print(i)
    #     for key,values in i.items():
    #         if key == 'id':
    #             # print(key)
    #             res = values
    #             # print(res)
    #             obj = QuesModel.objects.get(id=str(res))
    #             print(obj)
    #             answer_boxes = request.POST.get(str(obj))
    #                 # print(answer_boxes)
    #             answer_list.append(answer_boxes)
    # ---------------------------




            # print(key, value)
        # obj = QuesModel.objects.get(id=i+1)
        # print(obj)
        # if request.method == 'POST':






    # for i in range(0, len(final_quiz_list)):
    #     obj = QuesModel.objects.get(id=i+1)
    #     print(obj)
    #     # value = getattr(obj, obj.question)
    #     # print(value)
    #     # print(QuesModel.objects.get(id=i+1))
    #     if request.method == 'POST':
    #         # answer_boxes = request.POST.getlist('Вопрос 1')
    #         # print(quiz)
    #         answer_boxes = request.POST.getlist(str(obj))
    #         print(answer_boxes)




