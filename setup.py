try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

links = []
requires = []

try:
    requirements = parse_requirements('requirements.txt', session=False)
except:
    requirements = parse_requriements('requirements.txt', session=pip.download.PipSession())

for item in requirements:
    if getattr(item, 'url', None):
        links.append(str(item.url))
    if getattr(item, 'link', None):
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

with open('README.rst', 'r') as long_description_file:
    long_description = long_description_file.read()

setup(
    name='srv6_tracert',
    version='0.0.8',
    url='https://github.com/vmag/srv6_tracert',
    bugtrack_url='https://github.com/vmag/srv6_tracert/issues',
    license='MIT',
    author="Virginijus Magelinskas",
    author_email="virginijus@noia.network",
    description="SRv6 compatible traceroute",
    long_description=long_description,
    scripts=["srv6_traceroute.py"],
    packages=["srv6_tracert"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3',
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    dependency_links=links
)
