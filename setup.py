from setuptools import setup, find_packages

setup(
    name='vulnsekurak',
    version='0.1',
    packages=find_packages(),
    description='A simple hardcore Python library example.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/tturba/vulnsekurak',
    author='Omae Mae',
    author_email='tomasz.turba@securitum.pl',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='vulnsekurak',
)
