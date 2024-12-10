from django.contrib.auth.models import User
from django.db import models
from persiantools.jdatetime import JalaliDate
from django.utils.text import slugify
from .image_settings.tools import UploadToPathAndRename
from .image_settings.setting_models import MainModel
# Create your models here.



class CompanyWebsite(MainModel):
    title = models.CharField(max_length=255)
    website_url = models.URLField(max_length=500)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    logo = models.ImageField(upload_to = UploadToPathAndRename("home/"), default = 'default/website.png')
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    creationTime = models.DateTimeField(auto_now_add=True)
    modificationTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "CompanyWebsite"  # Custom table name
        verbose_name = "CompanyWebsite"
        verbose_name_plural = "CompanyWebsite"
        ordering = ["creationTime"]  # Default ordering


class SoftwareVersion(models.Model):
    sv = models.ForeignKey(CompanyWebsite, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    software_file = models.FileField(upload_to="uploads/software/", blank=True, null=True)
    download_link = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)
    creationTime = models.DateTimeField(auto_now_add=True)
    modificationTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SoftwareVersion"  # Custom table name
        verbose_name = "SoftwareVersion"
        verbose_name_plural = "SoftwareVersion"
        ordering = ["creationTime"]  # Default ordering


class NewsArticle(MainModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    title = models.CharField(max_length=255, blank=True, null=True)  # The title of the news article
    content = models.TextField(blank=True, null=True)  # The main content of the news article
    image = models.ImageField(upload_to = UploadToPathAndRename("home/"), default = 'default/article.png'
                              ,blank=True, null=True)
    active = models.BooleanField(default=False)  # Whether the article is active or archived
    slug = models.SlugField(null=True,blank=True,unique=True)
    published_date = models.DateTimeField(null=False)
    creationTime = models.DateTimeField(auto_now_add=True)
    modificationTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "NewsArticle"  # Custom table name
        verbose_name = "NewsArticle"
        verbose_name_plural = "NewsArticle"
        ordering = ["creationTime"]  # Default ordering


    def get_jalali_published(self):
        return JalaliDate(self.published_date).strftime('%Y/%m/%d')

    get_jalali_published.short_description = "تاریخ انتشار"


    def get_snipped(self):
        # Safely get the first 10 characters and append '...' if content is longer than 10 characters
        return f'{self.content[:10]}...'

class StaffMember(MainModel):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    position = models.CharField(max_length=255, verbose_name="Position")
    image = models.ImageField(upload_to = UploadToPathAndRename("home/"), default = 'default/StaffMember.png')
    birthday = models.DateField(verbose_name = "Birthday",)
    active = models.BooleanField(default=False)
    creationTime = models.DateTimeField(auto_now_add=True)
    modificationTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "StaffMember"  # Custom table name
        verbose_name = "StaffMember"
        verbose_name_plural = "StaffMember"
        ordering = ["creationTime"]  # Default ordering

    def __str__(self):
        return f"{self.name} - {self.position}"

    def get_jalali_birthday(self):
        # تبدیل تاریخ میلادی به شمسی
        return JalaliDate(self.birthday).strftime('%m/%d')



class SlideShow(MainModel):
    company_website = models.ForeignKey(
        CompanyWebsite,
        on_delete=models.CASCADE,
        related_name="slides",
        default = 1,
    )
    image = models.ImageField(upload_to = UploadToPathAndRename("home/"), default = 'default/slides.png')
    active = models.BooleanField(default=False, )
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modificationTime = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    class Meta:
        db_table = "SlideShow"  # Custom table name
        verbose_name = "SlideShow"
        verbose_name_plural = "SlideShows"
        ordering = ["creationTime", ]  # Default ordering

    def __str__(self):
        return f"SlideShow for {self.company_website}"

    def get_jalali_create(self):
        # تبدیل تاریخ میلادی به شمسی
        return JalaliDate(self.creationTime).strftime('%Y/%m/%d')

    get_jalali_create.short_description = "تاریخ ایجاد"

class OrganizationURL(models.Model):
    url = models.URLField(verbose_name="URL")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")
    active = models.BooleanField(default=True, verbose_name="Is Active")
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modificationTime = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    def __str__(self):
        return f"{self.description} - {self.url}"

    class Meta:
        db_table = "OrganizationURL"  # Custom table name
        verbose_name = "OrganizationURL"
        verbose_name_plural = "OrganizationURL"
        ordering = ["creationTime", ]  # Default ordering

    def get_jalali_create(self):
        # تبدیل تاریخ میلادی به شمسی
        return JalaliDate(self.creationTime).strftime('%Y/%m/%d')
    get_jalali_create.short_description = "تاریخ ایجاد"
