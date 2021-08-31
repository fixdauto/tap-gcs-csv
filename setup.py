#!/usr/bin/env python

from setuptools import setup

setup(name='tap-gcs-csv',
      version='0.0.1',
      description='Singer.io tap for extracting CSV files from Google Cloud Storage',
      author='FIXD Automotive',
      url='http://www.fixdapp.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_gcs_csv'],
      install_requires=[
          'pytz>=2018.0',
          'singer-python>=1.5.0',
          'voluptuous==0.10.5',
          'google-cloud-storage==1.42.0',
          'tap-s3-csv @ git+https://github.com/dbt-labs/tap-s3-csv.git@2933c2a5ab7e8dab47f3b5a93cbeea38d062801b',
      ],
      entry_points='''
          [console_scripts]
          tap-gcs-csv=tap_gcs_csv:main
      ''',
      packages=['tap_gcs_csv'])
