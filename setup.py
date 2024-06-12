from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='zenmoney-py',
    version="1.0.3",
    description='Library for zenmoney.ru API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cooper30/zenmoney_lib.git',
    license='MIT',
    author='Nikita Zvekov',
    author_email='cooper30@mail.ru',
    install_requires=['requests'],
    packages=['zenmoney'],
    package_dir={'': 'src'},
    package_data={
        'zenmoney': ['py.typed'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires="~=3.12",
)
