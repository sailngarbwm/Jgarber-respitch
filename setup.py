
from setuptools import setup, find_packages



setup(    
    name = "jgarber_respitch",
    description='functions for python respitch demonstration', 
    #version = pkg_resources.get_distribution('mamua').version,
    url='https://github.com/sailngarbwm/Jgarber-respitch',
    project_urls={
        "Code": "https://github.com/sailngarbwm/Jgarber-respitch",
    },
    packages=find_packages(where='.',exclude=('test','test.t_util')),
    long_description= open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Jonathan Garber Research Computing Services and Melbourne Data Analytics Platform',
    author_email='info@mdap.unimelb.edu.au',
    classifiers=[ 
        'Development Status :: 1 - Prod',
        'Intended Audience :: Learners',
        'Topic :: Software Development :: Build Tools',
        #'Programming Language :: Python :: 3.7',
        #'Programming Language :: Python :: 3.8',
    ],
    #python_requires=' ~=3.7, <4',
    include_package_data=True,
)