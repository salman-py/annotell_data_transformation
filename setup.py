import setuptools
from os.path import splitext
from glob import glob


with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
setuptools.setup(
    name="annotell_data_transformation",
    description="transformation of data",
    long_description=long_description,
    long_description_content_type="text/markdown", # required as pypi expects reStructuredText by default
    version='0.1.1',
    author="Mohammad Salman",
    author_email="salman81190@gmail.com",
    url="https://github.com/salman-py/annotell_data_transformation",
    keywords=['python', 'command-line'],
    packages=setuptools.find_packages('src'),  # why providing src
    install_requires=[REQUIREMENTS],
    scripts=['src/main.py'],
    package_dir={'':'src'},
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=2.7',

)