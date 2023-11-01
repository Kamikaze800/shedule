# main2.py в другой директории

import sys
import os
#
# # Определите путь к папке `registration` и базе данных
# registration_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'registration'))
# database_path = os.path.join(registration_path, 'handler')  # Замените 'handler' на фактическое имя папки с базой данных
#
# # Добавьте путь к папке `registration` и базе данных
# sys.path.append(registration_path)
# sys.path.append(database_path)
#
# # Импортируйте и выполните main.py из папки registration
# from registration import main
# main.main()
os.system(f'python registration/main.py')