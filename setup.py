from setuptools import setup, find_packages

setup(
    name='refinery',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'cachetools'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for Kratos and Oathkeeper integration.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/refinery',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)