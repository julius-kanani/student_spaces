#!/usr/bin/env python3
"""Initializes the models package"""

from os import getenv

storage_type = getenv("SS_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

    storage.reload()
