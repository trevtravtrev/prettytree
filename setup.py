from setuptools import setup, find_packages

setup(name='prettytree',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Create a pretty image of your project directory tree.',
    long_description=open('README.md').read(),
    install_requires=['os', 'PIL'],
    url='http://github.com/trevtravtrev/PrettyTree',
    author='Trevor White',
    author_email='trevor.white@wayne.edu')