# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from settings_local import DATABASES, PROJECT_DIR
from django.conf import settings
import os


class Command(BaseCommand):
    help = "Create backup of database"
    args = "[database]"

    def handle(self, *args, **options):
        db_settings = DATABASES[args[0]]
        db_type = db_settings['ENGINE'].split('.')[-1].split('_')[0]
        db_file = '/' + args[0] + '.sql'
        # Comando de exportación para SQLite3
        if db_type == 'sqlite3':
            db_command = 'sqlite3 ' + db_settings['NAME'] + ' .dump > ' + \
                settings.PRIVATE_ROOT + db_file
        # Comando de exportación para PostgreSQL
        elif db_type == 'postgresql':
            db_command = 'PGUSER=' + db_settings['USER'] + \
                ' PGPASSWORD=' + db_settings['PASSWORD'] + \
                ' pg_dump ' + db_settings['NAME'] + ' > ' + \
                settings.PRIVATE_ROOT + db_file
        # Comando de exportación para MySQL
        elif db_type == 'mysql':
            db_command = 'mysqldump --opt --user=' + db_settings['USER'] + \
                ' --password=' + db_settings['PASSWORD'] + \
                db_settings['NAME'] + ' > ' + \
                settings.PRIVATE_ROOT + db_file
        # Mantenemos el respaldo anterior con la extensión .old
        os.system('rm -f ' + settings.PRIVATE_ROOT + db_file + '.old')
        try:
            os.system('cp ' + settings.PRIVATE_ROOT + db_file + ' ' + \
                settings.PRIVATE_ROOT + db_file + '.old')
        except:
            pass
        os.system('rm -f ' + settings.PRIVATE_ROOT + db_file)
        # Realizamos la copia de seguridad de la base de datos
        os.system(db_command)
