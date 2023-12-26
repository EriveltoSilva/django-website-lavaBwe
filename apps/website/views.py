from django.db import models
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .emails import send_email_contact, send_email_confirm_newletters
#from .models import FrequentQuestion, Team, Contact, Carrocel, Galeria, New, NewsCategory, Comment, NewletterAssinature

def team_member(request, slug):
    # member = get_object_or_404(Team, slug=slug)
    # return render(request, "website/team-member-detail.html", {"page_name":"candidacy", "member":member})
    return render(request, "website/team-member-detail.html", {"page_name":"candidacy"})



def services(request):
    # carrocel = Carrocel.objects.filter(local="CANDIDATURA")
    # team_members = Team.objects.all()
    # return render(request, "website/candidacy.html", {"page_name":"candidacy","carrocel":carrocel,"team_members":team_members, "page_name":"candidacy"})
    # return render(request, "website/candidacy.html", {"page_name":"candidacy","carrocel":carrocel,"team_members":team_members, "page_name":"candidacy"})
    return render(request, "website/candidacy.html", {"page_name":"candidacy"})

def filter_by_category(request, slug):
    # category = get_object_or_404(NewsCategory, slug=slug)
    # carrocel = Carrocel.objects.filter(Q(local="NOTICIAS"))
    # news = New.objects.filter(published=True,category=category)
    # return render(request, "website/news.html", {"page_name":"news","carrocel":carrocel, "news":news})
    return render(request, "website/news.html", {"page_name":"news"})

def index(request):
    # carrocel = Carrocel.objects.filter(local="HOME")
    # image_about = Carrocel.objects.filter(local="SOBRE")[0]
    # galeria = Galeria.objects.filter(published=True)[:10]
    # news = New.objects.filter(published=True)[:10]
    # return render(request, "website/home.html", {"page_ntame":"home", "carrocel":carrocel, "image_about":image_about, "galeria":galeria, "news": news})
    return render(request, "website/home.html", {"page_ntame":"home"})


def faqs(request):
    # list_faqs = FrequentQuestion.objects.filter(published=True)
    # paginator = Paginator(list_faqs, 10)
    # page = request.GET.get('page')
    # faqs = paginator.get_page(page)
    # return render(request, "website/faq.html", {"faqs":faqs, "page_name":"faqs"})
    return render(request, "website/faq.html", {"faqs":faqs, "page_name":"faqs"})

def blog(request):
    # carrocel = Carrocel.objects.filter(Q(local="NOTICIAS"))
    # list_news = New.objects.filter(published=True)
    # paginator = Paginator(list_news, 20)
    # page = request.GET.get('page')
    # news = paginator.get_page(page)
    # return render(request, "website/news.html", {"page_name":"news","carrocel":carrocel, "news":news})
    return render(request, "website/news.html", {"page_name":"news"})




def blog_article(request, slug):
    # new = get_object_or_404(New, slug=slug)

    # if request.method=="POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     comment = request.POST['comment']
    #     if comment == None or comment=="":
    #         messages.error(request, f"O comentário está vázio")
    #     elif name == None or name=="":
    #         messages.error(request, f"O seu nome não foi inserido.")
    #     elif email == None or email=="":
    #         messages.error(request, f"O seu email não foi inserido.")
    #     else:
    #         messages.success(request, f"Comentário Públicado")
    #         comment = Comment(new=new, email=email,name=name, content=comment)
    #         comment.save()

    # categories = NewsCategory.objects.filter(published=True)
    # recent_news = New.objects.filter(published=True)[:10]
    # comments = Comment.objects.order_by('-created_at').filter(published = True, new=new).annotate(num_comments = models.Count('new'))
    # num_comments = len(comments)

    # return render(request, "website/news-single.html", {"page_name":"news", "num_comments":num_comments,"new": new, "categories":categories, "comments":comments, "recent_news":recent_news}) 
    return render(request, "website/news-single.html", {"page_name":"news"}) 


def newsletter(request):
    if request.method == 'POST':
        referer =  request.META.get('HTTP_REFERER') 
        try:
            email = request.POST['email']

            if email == None:
                messages.error(request, f"Preencha o seu email por favor!")
                return redirect (f"{referer}?mess=True")

            if NewletterAssinature.objects.filter(email__icontains=email).exists():
                
                print(f"Este email já possui uma assinatura da nossa newletter!\nReferer:{referer}")
                messages.error(request, f"Este email já possui uma assinatura da nossa newletter!")
                return redirect (f"{referer}?mess=True")
                        
            subscription  = NewletterAssinature(email=email)
            subscription.save()
            if send_email_confirm_newletters(email):
                messages.success(request, f"Subscrição de Newletter realizada com Sucesso!")
                return redirect (f"{referer}?mess=True")
            else: 
                messages.error(request, f"Erro enviando Email!")
                print('Erro enviando o email')
        except Exception as e:
            print(f"Erro:{e=}")
            messages.error(request, f"Ocorreu um erro no servidor! Tenta mais tarde ou contacte a equipe da hss!")
            return redirect (f"{referer}?mess=True")

        finally:
            return redirect (f"{referer}?mess=True")
    return redirect (f"{referer}?mess=True")



def about_us(request):
    # image = Carrocel.objects.filter(local="SOBRE")[0]
    # return render(request, "website/about_me.html", {"page_name":"about_me", "image":image})
    return render(request, "website/about_us.html", {"page_name":"about_us"})

def contacts(request):
    # if request.method == "POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     contact = Contact(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    #     send_email_contact(name=name, email=email, subject=subject, message=message)
    #     messages.success(request, f"Email Enviado com Sucesso! Entraremos em contacto o mais breve possível")
    #     return render(request, 'website/contacts.html', {"page_name":"contacts", "message":messages})
    # return render(request, "website/contacts.html", {"page_name":"contacts"})
    return render(request, "website/contacts.html", {"page_name":"contacts"})
