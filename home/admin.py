from django.contrib import admin
from .models import CompanyWebsite, NewsArticle, StaffMember, SlideShow, OrganizationURL,\
    SoftwareVersion
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class MySvInline(admin.TabularInline):
    model = SoftwareVersion
    fields = ["name", "active", "software_file", "download_link"]
    extra = 1

class SlideInline(admin.TabularInline):
    model = SlideShow
    fields = ["image", "active"]
    extra = 1


@admin.register(CompanyWebsite)
class CompanyWebsiteAdmin(SummernoteModelAdmin):
    inlines = [MySvInline, SlideInline]
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["title", "website_url", "description", "logo", "linkedin", "whatsapp", "instagram", "telegram", "active"]
    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["title", "active", ]
    def get_search_fields(self, request):
        return ["title", ]
    def get_list_filter(self, request):
        return ["title", ]


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["author", "title", "content", "image", "active",  "slug", "published_date"]
    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["author", "active", "title", "slug","get_jalali_published"]
    def get_search_fields(self, request):
        return ['author', "title"]
    def get_list_filter(self, request):
        return ["title", ]







@admin.register(OrganizationURL)
class OrganizationURLAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["url", "description", "active", ]
    def get_list_display(self, request):
        return ["description", "active", 'get_jalali_create']
    def get_list_filter(self, request):
        return ["active", ]


from django.contrib import admin



@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["name", "position", "active", "birthday" , "image"]
    def get_list_display(self, request):
        return ["name", "position", "active", "creationTime"]
    def get_list_filter(self, request):
        return ["active", ]

