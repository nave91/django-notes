# -*- coding: utf-8 -*-
from notes.models import Note
from django.contrib import admin
from django.contrib.contenttypes import generic


class NoteInline(generic.GenericTabularInline):
    model = Note

admin.site.register(Note)
