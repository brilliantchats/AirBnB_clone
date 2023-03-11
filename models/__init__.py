#!/usr/bin/python3
"""
Initialisation code when the models module is imported
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
