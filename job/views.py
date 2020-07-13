from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import ListView,  DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Job, Candidate, Resume, PopularCategorie
from .forms import CandidateForm, JobForm, ResumeForm, JobSearchForm
from django.contrib import messages
from .forms import CandidateForm
from django.db.models import Q




def home(request):
    jobs = Job.objects.all()
    candidates = Candidate.objects.all()
    pop_cat = PopularCategorie.objects.filter(POPCat__iexact="Web development")
   
    context = {
        'jobs': jobs,
        'candidates': candidates,
        'pop_cat': pop_cat,
        
    }
    return render(request, 'job/index.html', context)


def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj, 
        'list': job_list, 
    }
    return render(request, 'job/jobs.html', context)


def job_details(request, slug):
    job_list = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        print('done')
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_list
            my_form = form.save()
            
    
    else:
        form = CandidateForm()


    context = {
        'jobs': job_list,
        'form': form
    }
    return render(request, 'job/job_details.html', context)



def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        print('done')
        if form.is_valid():
            job_form = form.save(commit=False)
            job_form.job = job_list
            job_form = form.save()
            messages.success(request, "Job Added")

            return redirect('/')
            
    
    else:
        form = JobForm()


    context = {
        'jobs': add_job,
        'form': form
    }
    return render(request, 'job/add_job.html', context)


@login_required
def upload_resume(request):
    resume = Resume.objects.all()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        print('done')
        if form.is_valid():
            resume_form = form.save(commit=False)
            resume_form.resume = resume
            resume_form = form.save()
            messages.success(request, "Resume Added")

            return redirect('/')
            
    
    else:
        form = ResumeForm()


    context = {
        'resume': upload_resume,
        'form': form
    }
    return render(request, 'job/upload_resume.html', context)
    



