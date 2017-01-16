try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'Ex46',
    'author': 'WangNan',
    'url': 'www.jadesouth.cn',
    'download_url': 'www.jadesouth.cn',
    'author_email': 'wangnanphp@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wangnan'],
    'scripts': [],
    'name': 'ex46'
]

setup(**config)
