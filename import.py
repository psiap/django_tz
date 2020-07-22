import csv, sys, os

project_dir = "C:/Users/dom/PycharmProjects/tz/tz"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()



data = csv.reader(open("C:/Users/dom/PycharmProjects/tz/deals.csv",encoding='utf-8'), delimiter=',')

from todo.models import DealsFile
for row in data:
    if row[0] != 'create_date':
        dealsFile = DealsFile()
        dealsFile.customer = row[0]
        dealsFile.item = row[1]
        dealsFile.total = row[2]
        dealsFile.quantity = row[3]
        dealsFile.date = row[4]
        dealsFile.save()
