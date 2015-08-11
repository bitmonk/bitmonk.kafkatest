from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='bitmonk.kafkatest',
      version=version,
      description="basic kafka producer / consumer for testing a cluster",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='kafka',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bitmonk'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pykafka',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
