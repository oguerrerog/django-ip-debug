#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-ip-debug',
    version='0.1.0',
    description='Middleware para habilitar DEBUG solo para ciertas IPs en proyectos Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oguerrero/django-ip-debug',
    author='Oscar Guerrero G.',
    author_email='oguerrerog@gmail.com',
    license='MIT license',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'ipaddress',
    ],
    python_requires='>=3.7',
)
