from setuptools import setup, find_packages

setup(
    name='simplelib',
    version='0.1',
    packages=find_packages(),
    description='A simple Python library example.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/username/simplelib',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='simplelib',
)
