from setuptools import setup, find_packages

with open("README-cn.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name="pixiver",
    version="0.0.2-alpha",
    author="darkchii",
    author_email="darkchii@qq.com",
    description="A free python library for crawling and downloading works on the pixiv website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['beautifulsoup4', 'requests', 'pillow'],
    packages=find_packages(),
    url='https://github.com/darkchii/pixiver',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ]
)