# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from settings_local import DATABASES, PROJECT_DIR
import os


class Command(BaseCommand):
    help = "Create backup of database"

    def handle(self, *args, **options):
        db_settings = DATABASES[args[0]]
        db_type = db_settings['ENGINE'].split('.')[-1].split('_')[0]
        if db_type == 'sqlite3':
            db_command = 'sqlite3 ' + db_settings['NAME'] + ' .dump > ' + \
                PROJECT_DIR + '/privado/' + args[0] + '.sql'
        elif db_type == 'postgresql':
            db_command = 'PGUSER=' + db_settings['USER'] + \
                ' PGPASSWORD=' + db_settings['PASSWORD'] + \
                ' pg_dump ' + db_settings['NAME'] + ' > ' + \
                PROJECT_DIR + '/privado/' + args[0] + '.sql'
        os.system(db_command)
