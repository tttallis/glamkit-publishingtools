from setuptools import setup, find_packages

setup(
    name='glamkit-publishingtools',
    author='Thomas Ashelford',
    author_email='thomas@interaction.net.au',
    version='0.1',
    description='Tools for publishing a model',
    url='http://github.com/glamkit/glamkit-publishingtools',
    packages=find_packages(),
    package_data={},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)