import os
import psycopg2
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from categories.models import Category
from products.models import Product
from members.models import Customer
from members.management.commands.import_data_helper import ConnectDataBase




class Command(BaseCommand):
    help = 'A brief description of your custom command'

    model = Category
    os_cols = ( 'name', 'slug', 'image_url' )
    in_cols = ( 'title', 'slug', 'image_url' )
    table = ''

    def getTable (self):
        load_dotenv()
        return os.getenv("CATEGORY_TABLE_NAME")

    def handle(self, *args, **options):
        print('Begining connecting database...')
        connection = ConnectDataBase(self.getTable(),self.os_cols, self.in_cols, self.model)
        connection.importDB()
        print('End connecting database...')