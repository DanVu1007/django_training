import os
import psycopg2


from dotenv import load_dotenv

from django.core.management.base import BaseCommand
from members.models import Category
from members.models import Product
from members.models import Customer




class Command(BaseCommand):
    help = 'A brief description of your custom command'

    all_table = {}

    def connectToDB(self):
        #load from env
        load_dotenv()
        self.all_table = {
                os.getenv("CATEGORY_TABLE_NAME"): {
                    'localTable': Category,
                    'server' : ( 'name', 'slug', 'image_url' ),
                    'dbInUser' : ( 'title', 'slug', 'image_url' )
                },
                os.getenv("PRODUCT_TABLE_NAME"): {
                    'localTable': Product,
                    'server' : ( 'name', 'slug',  'description_short',  'retail_price' ),
                    'dbInUser' : ( 'name', 'slug', 'description', 'price')
                },
                os.getenv("CUSTOMER_TABLE_NAME"): {
                    'localTable': Customer,
                    'server' : ( 'first_name', 'last_name', 'email' ),
                    'dbInUser' : ( 'first_name', 'last_name', 'email' )
                },
            }
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )

        if connection :
            print('Connect successfully...')
            return connection
        else:
            print('FAIL...')
            return False
        
    def handle(self, *args, **options):
        try:    
            print('Begining connecting database...')
            #load from env
            load_dotenv()
            connection = self.connectToDB()
            cursor = connection.cursor()


            for i in self.all_table:
                product_data = []
                query = "SELECT {} FROM {}"
                model = self.all_table[i]['localTable']
                selectColumn = result_string = ','.join(self.all_table[i]['server'])

                query = query.format(selectColumn, i)
                cursor.execute(query)

                data_list = cursor.fetchall()
                for datum in data_list:
                    product = {}
                    for index, value in enumerate(self.all_table[i]['dbInUser']):
                        product[value] = datum[index]
                    product_data.append(product)

                models_to_save = [model(**data) for data in product_data]
                # Use bulk_create to insert the data into the database
                model.objects.all().delete()
                model.objects.bulk_create(models_to_save)

            cursor.close()
            connection.close()
            print('Disconnect server. Apply success')


        except Exception as e:
            print(e)
          
    