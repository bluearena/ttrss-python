from distutils.core import setup

setup(
        name='ttrss-python',
        version='0.1',
        description='A python library for the Tiny Tiny RSS web API',
        author='Markus Wiik',
        author_email='markus.wiik@gmail.com',
        packages=['ttrss'],
        requires=['requests (>=1.1.0)'],
        provides=['ttrss'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            ],
        )
