import os
import psycopg2
from dotenv import load_dotenv

class ConnectDataBase:

    os_table = ''    
    os_cols = {}
    in_cols = {}
    model = None

    def __init__(self, os_table, os_cols, in_cols, model):
        self.os_table = os_table
        self.os_cols = os_cols
        self.in_cols = in_cols
        self.model = model
    
    def importDB(self):
        try:
            cusmtoms_data = []
            model = self.model
            connection = self.connectDb()
            cursor = connection.cursor()
            query = "SELECT {} FROM {}".format(','.join(self.os_cols), self.os_table)
            cursor.execute(query)
            data_list = cursor.fetchall()
            print('Get all data successfully ...')

            for datum in data_list:
                cusmtoms = {}
                for index, value in enumerate(self.in_cols):
                    cusmtoms[value] = datum[index]
                cusmtoms_data.append(cusmtoms)

            models_to_save = [model(**data) for data in cusmtoms_data]
            model.objects.all().delete()
            model.objects.bulk_create(models_to_save)

            cursor.close()
            connection.close()
            print('Apply success...Disconnect server.')
            
        except Exception as e:
            print('FAIL...')
            print(e)


    def connectDb(self):
        load_dotenv()
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
            return connection
            
        else:
            print('Connect FAIL...')
            return False
