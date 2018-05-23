from setuptools import setup, find_packages
setup(
    name="ocperf",
    version="0.1",
    package_dir={'':'.'},
    packages=find_packages('.'),
    scripts=['ocperf.py', 'pmumon.py', 'list-events.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires=['docutils>=0.3'],

    #package_data={
        # If any package contains *.txt or *.rst files, include them:
        #'': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    #},
    include_package_data=True,

    # metadata for upload to PyPI
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    license="PSF",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/"# project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
