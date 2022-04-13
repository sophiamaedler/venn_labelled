from setuptools import setup

setup(name='venn_labelled',
      version="0.0.1",
      description="Functions for plotting sets of strings into venn diagramms",
      long_description="",
      classifiers=[  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 1 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Visualization'
      ],
      platforms=['Platform Independent'],
      keywords='matplotlib plotting charts venn-diagrams string labels',
      author='Sophia Maedler',
      author_email='maedler@biochem.mpg.de',
      url='',
      license='MIT',
      include_package_data=True,
      zip_safe=True,
      install_requires=['matplotlib', "matplotlib_venn", 'numpy'],
      )