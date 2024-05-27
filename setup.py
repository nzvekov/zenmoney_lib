from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='zenmoney',
    version="0.0.1",
    description='Library for zenmoney.ru API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cooper30/zenmoney_lib.git',
    license='MIT',
    author='Nikita Zvekov',
    author_email='cooper30@mail.ru',
    install_requires=requires,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires="~=3.12",
)
