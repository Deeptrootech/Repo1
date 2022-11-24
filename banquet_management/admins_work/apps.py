"""
Just an alternate way to update your application related configuration when you create new app
"""

from django.apps import AppConfig


class AdminsWorkConfig(AppConfig):
    """
    Describes created new application
    """
    name = 'admins_work'
