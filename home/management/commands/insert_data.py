from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from ...models import CompanyWebsite, StaffMember, SlideShow, OrganizationURL, NewsArticle
import random
from django.utils import timezone


class Command(BaseCommand):
    help = "Insert dump data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username=self.fake.user_name(),
            email=self.fake.email(),
            password="123456789ab"
        )

        CompanyWebsite.objects.create(
                title=self.fake.company(),
                website_url=self.fake.url(),
                description=self.fake.text(max_nb_chars=300),
                active=True,
                linkedin=self.fake.url(),
                whatsapp=self.fake.phone_number(),
                instagram=self.fake.user_name(),
                telegram=self.fake.user_name(),
                logo="default/website.png"  # Keep default logo or add logic to upload random images
        )
        self.stdout.write(self.style.SUCCESS("Successfully inserted fake data into CompanyWebsite model!"))

        # Insert fake Staff Members
        for _ in range(10):  # Insert 10 fake staff members
            StaffMember.objects.create(
                name=self.fake.name(),
                position=self.fake.job(),
                image='default/StaffMember.png',
                birthday=self.fake.date_of_birth(),
                active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Inserted 10 fake StaffMember entries."))

        # Insert fake SlideShows
        for _ in range(5):  # Insert 5 fake slides
            company_websites = list(CompanyWebsite.objects.filter(active=True))
            if company_websites:
                company_website = random.choice(company_websites)
            else:
                company_website = None
            SlideShow.objects.create(
                company_website=company_website,
                image='default/slides.png',
                active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Inserted 5 fake SlideShow entries."))

        # Insert fake Organization URLs
        for _ in range(10):  # Insert 10 URLs
            OrganizationURL.objects.create(
                url=self.fake.url(),
                description=self.fake.text(max_nb_chars=100),
                active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Inserted 10 fake OrganizationURL entries."))

        # Insert 20 fake NewsArticle entries
        for _ in range(20):  # Adjust number as needed
            NewsArticle.objects.create(
                author=user,
                title=self.fake.sentence(),
                content=self.fake.text(max_nb_chars=1000),
                image='default/article.png',
                active=random.choice([True, False]),
                slug=self.fake.slug(),
                published_date=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS("Successfully inserted 20 fake NewsArticle entries."))