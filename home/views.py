from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, timedelta
from .models import CompanyWebsite, SlideShow, OrganizationURL, NewsArticle, StaffMember,\
    SoftwareVersion
# Create your views here.


class PortalPageView(View):
    template_name = "home/index.html"
    def get(self, request, *args, **kwargs):
        urls = OrganizationURL.objects.filter(active=True)
        slides = SlideShow.objects.filter(active=True)
        companies = CompanyWebsite.objects.get(active=True)
        software_version = SoftwareVersion.objects.filter(active=True)
        articles_list = NewsArticle.objects.filter(active=True, published_date__lte=timezone.now())
        paginator = Paginator(articles_list, 3)  # Show 5 articles per page

        page_number = request.GET.get('page')  # Get the page number from the request
        try:
            articles = paginator.page(page_number)  # Get the articles for that page
        except PageNotAnInteger:
            articles = paginator.page(1)  # If page is not an integer, deliver first page
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page

        # Calculate the current date and the range for 5 days before and after
        today = datetime.now().date()
        five_days_before = today - timedelta(days=10)
        five_days_after = today + timedelta(days=10)

        # Filter birthdays, ignoring the year
        members = StaffMember.objects.filter(
            active=True
        ).filter(
            Q(birthday__month=today.month, birthday__day__gte=five_days_before.day) |
            Q(birthday__month=today.month, birthday__day__lte=five_days_after.day) |
            Q(birthday__month=five_days_after.month, birthday__day__lte=five_days_after.day) |
            Q(birthday__month=five_days_before.month, birthday__day__gte=five_days_before.day)
        )

        content = {
          "urls": urls,
          "slides":slides,
          "companies":companies,
          "members":members,
          "articles":articles,
          "softwares":software_version,
        }
        return render(request, self.template_name, content)

class PostDetailsView(View):
    template_name = 'home/details.html'
    def get(self,request,*args, **kwargs):
        post = get_object_or_404(NewsArticle,pk=kwargs['news_id'])
        companies = CompanyWebsite.objects.get(active=True)
        content = {
            "article":post,
            "companies": companies,
        }
        return render(request, self.template_name, content)



class HomePageView(View):
    template_name = "home/Portal/index.html"
    def get(self, request):
        return render(request, self.template_name)
