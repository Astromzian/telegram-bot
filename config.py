from enum import Enum

token = '1790892466:AAEo2tiTgaDjpXiA9omYZGKmZHFdLLXaPQY' #Вставить сюда токен
db_file = 'database.vdb'


class States(Enum):h
    S_START = "1"
    S_ENTER_DAY = "2"
    S_COUNTRY_OR_REGION = "3"
    S_ENTER_COUNTRY_OR_REGION = "4"
    S_ENTER_FIELDS_LIST = "5"



