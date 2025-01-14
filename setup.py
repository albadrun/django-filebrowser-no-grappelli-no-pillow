import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-filebrowser-no-grappelli-no-pillow',
    version='3.8.2',
    description='Media-Management no Grappelli no Pillow',
    long_description=read('README.rst'),
    url='https://github.com/albadrun/django-filebrowser-no-grappelli-no-pillow',
    download_url='',
    author='Patrick Kranzlmueller, Axel Swoboda (vonautomatisch), Maxim Sukharev',
    author_email='office@vonautomatisch.at, max@smacker.ru',
    maintainer='Ragil Pasaribu',
    maintainer_email='ragil.albadrun@gmail.com',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False,
    install_requires=['six'],
)
