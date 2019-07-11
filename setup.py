try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

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

setup(
    name='srv6_tracert',
    version='0.0.1',
    url='https://github.com/vmag/srv6_tracert',
    license='MIT',
    author="Virginijus Magelinskas",
    author_email="virginijus@noia.network",
    description="SRv6 compatible traceroute",
    long_description="SRv6 compatible traceroute (runs alongside ICMP traceroute). Also supports running from a config file, and several Scapy verbosity levels",
    scripts=["srv6_traceroute.py"],
    packages=["srv6_tracert"],
    python_requires='>=3',
    zip_safe=False
)
