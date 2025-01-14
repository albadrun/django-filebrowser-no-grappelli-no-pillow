# coding: utf-8

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import re


# Main FileBrowser Directory. Relative to site.storage.location.
# DO NOT USE A SLASH AT THE BEGINNING, DO NOT FORGET THE TRAILING SLASH AT THE END.
DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

# EXTENSIONS AND FORMATS
# Allowed Extensions for File Upload. Lower case is important.
EXTENSIONS = getattr(settings, "FILEBROWSER_EXTENSIONS", {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.docx'],
    'Video': ['.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.wav', '.aiff', '.midi', '.m4p']
})
# Define different formats for allowed selections.
# This has to be a subset of EXTENSIONS.
# e.g., add ?type=image to the browse-URL ...
SELECT_FORMATS = getattr(settings, "FILEBROWSER_SELECT_FORMATS", {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
})

# EXTRA SETTINGS

# Exclude files matching any of the following regular expressions
EXTENSION_LIST = []
for exts in EXTENSIONS.values():
    EXTENSION_LIST += [re.escape(ext) for ext in exts if ext]
EXCLUDE = getattr(settings, 'FILEBROWSER_EXCLUDE',
                  (r'_(%(exts)s)_.*_q\d{1,3}\.(%(exts)s)' % {'exts': ('|'.join(EXTENSION_LIST))},))
# Max. Upload Size in Bytes.
MAX_UPLOAD_SIZE = getattr(settings, "FILEBROWSER_MAX_UPLOAD_SIZE", 10485760)
# Normalize filename and remove all non-alphanumeric characters
# except for underscores, spaces & dashes.
NORMALIZE_FILENAME = getattr(settings, "FILEBROWSER_NORMALIZE_FILENAME", False)
# Convert Filename (replace spaces and convert to lowercase)
CONVERT_FILENAME = getattr(settings, "FILEBROWSER_CONVERT_FILENAME", True)
# Max. Entries per Page
# Loading a Sever-Directory with lots of files might take a while
# Use this setting to limit the items shown
LIST_PER_PAGE = getattr(settings, "FILEBROWSER_LIST_PER_PAGE", 50)
# Default Sorting
# Options: date, filesize, filename_lower, filetype_checked
DEFAULT_SORTING_BY = getattr(
    settings, "FILEBROWSER_DEFAULT_SORTING_BY", "date")
# Sorting Order: asc, desc
DEFAULT_SORTING_ORDER = getattr(
    settings, "FILEBROWSER_DEFAULT_SORTING_ORDER", "desc")
# regex to clean dir names before creation
FOLDER_REGEX = getattr(settings, "FILEBROWSER_FOLDER_REGEX", r'^[\w._\ /-]+$')
# Traverse directories when searching
SEARCH_TRAVERSE = getattr(settings, "FILEBROWSER_SEARCH_TRAVERSE", False)
# Default Upload Permissions
DEFAULT_PERMISSIONS = getattr(
    settings, "FILEBROWSER_DEFAULT_PERMISSIONS", 0o755)
# Overwrite existing files on upload
OVERWRITE_EXISTING = getattr(settings, "FILEBROWSER_OVERWRITE_EXISTING", True)
# Add fake model to show filebrowser in admin dashboard
SHOW_IN_DASHBOARD = getattr(settings, "FILEBROWSER_SHOW_IN_DASHBOARD", True)

# UPLOAD

# Directory to Save temporary uploaded files (FileBrowseUploadField)
# Relative to site.storage.location.
UPLOAD_TEMPDIR = getattr(settings, 'FILEBROWSER_UPLOAD_TEMPDIR', '_temp')

# EXTRA TRANSLATION STRINGS

# The following strings are not available within views or templates
_('Folder')
_('Image')
_('Video')
_('Document')
_('Audio')


# Overwrite admin_site.
# Example:
# in file: apps.core.admin define this code.

# from django.contrib import admin
# class CustomAdmin(admin.AdminSite):
#     site_header = site_title = 'Custom Admin'
#     index_title = 'Custom Administration'

# admin_general = CustomAdmin(name='admin_general')

# In settings:
# FILEBROWSER_CUSTOM_ADMIN = 'apps.core.admin.admin_general'

ADMIN_CUSTOM = getattr(settings, 'FILEBROWSER_CUSTOM_ADMIN', None)
