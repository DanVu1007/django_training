import os
import mysql.connector
import psycopg2


from dotenv import load_dotenv

from django.core.management.base import BaseCommand
from members.models import Category
from members.models import Product
from members.models import Customer




class Command(BaseCommand):
    help = 'A brief description of your custom command'

    def printAllTable(self, alltable):
        print(any)

    def handle(self, *args, **options):
        try:    
            print('Begining connecting database...')
            
            #load from env
            load_dotenv()
            all_table = {
                os.getenv("CUSTOMER_TABLE_NAME"): {
                    'server' : {
                        'first_name',
                        'last_name',
                        'email'
                    },
                    'dbInUser' : {
                        'first_name',
                        'last_name',
                        'email'
                    }
                },
                os.getenv("CATEGORY_TABLE_NAME"): {
                    'server' : {
                        'name',
                        'slug',
                        'image_url'
                    },
                    'dbInUser' : {
                        'title',
                        'slug',
                        'image_url'
                    }
                },
                os.getenv("PRODUCT_TABLE_NAME"): {
                    'server' : {
                        'name',
                        'slug', 
                        'description_short', 
                        'retail_price'
                    },
                    'dbInUser' : {
                        'name',
                        'slug',
                        'price',
                        'description'
                    }
                }
            }
            self.printAllTable(all_table)
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

            cursor = connection.cursor()
            print('Connection successfully , begining import...')


            query = "SELECT name, slug, description_short, retail_price FROM %s LIMIT 5;" % product_table
            cursor.execute(query)
            data_list = cursor.fetchall()

            product_data = []
            for row in data_list:
                product = {
                    'name': row[0],
                    'slug': row[1],
                    'description': row[2],
                    'price': row[3],
                }
                product_data.append(product)


            print(product_data)

            # products_to_save = [Product(**data) for data in product_data]
            # # Use bulk_create to insert the data into the database
            # Product.objects.bulk_create(products_to_save)

            print("Successful.")


            cursor.close()
            connection.close()


        except Exception as e:
            print("Error: Unable to connect to the database.")
            print(e)
          
    