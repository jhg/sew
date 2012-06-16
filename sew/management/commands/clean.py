# -*- encoding: utf-8 -*-
from django.core.management.base import NoArgsCommand
import os

class Command(NoArgsCommand):
    help = "Clean files finish with ~"
    def handle_noargs(self, **options):
        os.system("find ./ -name *~ -exec rm {} \\;")
