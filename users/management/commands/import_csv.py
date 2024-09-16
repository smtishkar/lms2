import csv
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r', encoding="utf8") as file:
            csv_reader = csv.DictReader(file)

            
            for row in csv_reader:
                # password=row['password']
                # print(password)
                # Create a new MyModel instance from the CSV data
                u = User.objects.create(
                    password=row['password'],
                    last_login=row['last_login'],
                    is_superuser=row['is_superuser'],
                    username=row['username'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    is_staff=row['is_staff'],
                    is_active=row['is_active'],
                    date_joined=row['date_joined'],
                    date_birth=row['date_birth'],
                    dlr=row['dlr'],
                    job_title=row['job_title'],
                    saba_id=row['saba_id'],
                    access_rights=row['access_rights'],
                    job_title2=row['job_title2'],
                    # Add other fields as needed
                )
                print(u.first_name)
                u.set_password(u.password)
                u.save()
                
                