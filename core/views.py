from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import AboutMe, Skill, Project, Certificate, ContactMessage
from .forms import AboutMeForm, SkillForm, ProjectForm, CertificateForm

# ==========================================
# PUBLIC VIEWS
# ==========================================
def home(request):
    about_me = AboutMe.objects.first()
    frontend_skills = Skill.objects.filter(category='Frontend')
    backend_skills = Skill.objects.filter(category='Backend')
    other_skills = Skill.objects.filter(category='Tools')
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please fill in all required fields.")
    
    context = {
        'about': about_me,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'other_skills': other_skills,
        'projects': projects,
        'certificates': certificates,
    }
    return render(request, 'core/home.html', context)

# ==========================================
# AUTHENTICATION
# ==========================================
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    # Apply glassmorphism styling to auth form
    for field in form.fields.values():
        field.widget.attrs['class'] = 'glass-input'
        
    return render(request, 'core/dashboard/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# ==========================================
# ADMIN DASHBOARD
# ==========================================
@login_required(login_url='admin_login')
def admin_home(request):
    context = {
        'message_count': ContactMessage.objects.filter(is_read=False).count(),
        'project_count': Project.objects.count(),
        'cert_count': Certificate.objects.count(),
    }
    return render(request, 'core/dashboard/index.html', context)

@login_required(login_url='admin_login')
def admin_about(request):
    about_me = AboutMe.objects.first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=about_me)
        if form.is_valid():
            form.save()
            messages.success(request, "About Me detailed updated.")
            return redirect('admin_home')
    else:
        form = AboutMeForm(instance=about_me)
    return render(request, 'core/dashboard/form.html', {'form': form, 'title': 'Edit About Me'})

# --- Projects ---
@login_required(login_url='admin_login')
def admin_projects(request):
    projects = Project.objects.all()
    return render(request, 'core/dashboard/list.html', {'items': projects, 'title': 'Projects', 'type': 'project'})

@login_required(login_url='admin_login')
def admin_project_form(request, pk=None):
    if pk:
        project = get_object_or_404(Project, pk=pk)
        title = "Edit Project"
    else:
        project = None
        title = "Add Project"
        
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"Project {title.lower()}ed successfully.")
            return redirect('admin_projects')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'core/dashboard/form.html', {'form': form, 'title': title})

@login_required(login_url='admin_login')
def admin_project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, "Project deleted.")
    return redirect('admin_projects')

# --- Certificates ---
@login_required(login_url='admin_login')
def admin_certificates(request):
    certs = Certificate.objects.all()
    return render(request, 'core/dashboard/list.html', {'items': certs, 'title': 'Certificates', 'type': 'certificate'})

@login_required(login_url='admin_login')
def admin_certificate_form(request, pk=None):
    if pk:
        cert = get_object_or_404(Certificate, pk=pk)
        title = "Edit Certificate"
    else:
        cert = None
        title = "Add Certificate"
        
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=cert)
        if form.is_valid():
            form.save()
            messages.success(request, f"Certificate {title.lower()}ed successfully.")
            return redirect('admin_certificates')
    else:
        form = CertificateForm(instance=cert)
    return render(request, 'core/dashboard/form.html', {'form': form, 'title': title})

@login_required(login_url='admin_login')
def admin_certificate_delete(request, pk):
    cert = get_object_or_404(Certificate, pk=pk)
    cert.delete()
    messages.success(request, "Certificate deleted.")
    return redirect('admin_certificates')

# --- Skills ---
@login_required(login_url='admin_login')
def admin_skills(request):
    skills = Skill.objects.all()
    return render(request, 'core/dashboard/list.html', {'items': skills, 'title': 'Skills', 'type': 'skill'})

@login_required(login_url='admin_login')
def admin_skill_form(request, pk=None):
    if pk:
        skill = get_object_or_404(Skill, pk=pk)
        title = "Edit Skill"
    else:
        skill = None
        title = "Add Skill"
        
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f"Skill {title.lower()}ed successfully.")
            return redirect('admin_skills')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'core/dashboard/form.html', {'form': form, 'title': title})

@login_required(login_url='admin_login')
def admin_skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.success(request, "Skill deleted.")
    return redirect('admin_skills')

# --- Messages ---
@login_required(login_url='admin_login')
def admin_messages(request):
    msgs = ContactMessage.objects.all().order_by('-created_at')
    # Mark as read
    ContactMessage.objects.filter(is_read=False).update(is_read=True)
    return render(request, 'core/dashboard/messages.html', {'messages_list': msgs})

@login_required(login_url='admin_login')
def admin_message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    messages.success(request, "Message deleted.")
    return redirect('admin_messages')
