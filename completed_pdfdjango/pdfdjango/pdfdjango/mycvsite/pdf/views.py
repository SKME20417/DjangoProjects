from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        priviouswork = request.POST.get("priviouswork", "")
        skills = request.POST.get("skills", "")
        certifications = request.POST.get("certifications", "")
        profile = Profile(name = name, phone = phone, email = email, summary = summary,
                 degree = degree, school = school, university = university,
                priviouswork = priviouswork, skills = skills, certifications = certifications)
        profile.save()
    return render(request, "pdf/index.html")


def resume(request, id):
    userprofile = Profile.objects.get(pk = id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"userprofile":userprofile})
    options = {
        'page-size': 'A4',
        'margin-top': '0.7in',
        'margin-right': '0.7in',
        'margin-bottom': '0.7in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",}
    pdf = pdfkit.from_string(html,False,options=options)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename='resume.pdf'
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, "pdf/list.html",{'profiles':profiles})