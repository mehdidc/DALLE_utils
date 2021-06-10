from setuptools import setup

description = "utilities for DALL-E"

setup(
    name="dalle_utils",
    version="0.1.0",
    author="Mehdi Cherti",
    description=description,
    license="MIT",
    url="https://github.com/mehdidc/DALLE_utils",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['dalle_utils'],
    include_package_data=True,
    install_requires=['clize'],
)

