#!/usr/bin/python3
"""init package(method for models directory)"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
