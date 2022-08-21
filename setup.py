import os
from setuptools import setup, Extension, find_packages

package_name = "edsdk-python"
version = "0.1"

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = ""


_DEBUG = True
_DEBUG_LEVEL = 0

extra_compile_args = []
if _DEBUG:
    extra_compile_args += ["/W4", "/DDEBUG=%s" % _DEBUG_LEVEL]
else:
    extra_compile_args += ["/DNDEBUG"]


EDSDK_PATH = "dependencies"
# EDSDK_PATH = "dependencies/EDSDK_13.13.41_Win/"

extension = Extension(
    "edsdk.api",
    libraries=["EDSDK"],
    include_dirs=[os.path.join(EDSDK_PATH, "EDSDK/Header")],
    library_dirs=[os.path.join(EDSDK_PATH, "EDSDK_64/Library")],
    depends=["edsdk/edsdk_python.h", "edsdk/edsdk_utils.h"],
    sources=["edsdk/edsdk_python.cpp","edsdk/edsdk_utils.cpp"],
    extra_compile_args=extra_compile_args,
)

setup(
    name=package_name,
    version=version,
    author="Francesco Leacche",
    author_email="francescoleacche@gmail.com",
    url="https://github.com/jiloc/edsdk-python",
    description="Python wrapper for Canon EDSKD Library",
    long_description=long_description,
    ext_modules = [extension],
    install_requires=[
        'pywin32 >= 228 ; platform_system=="Windows"'
    ],
    setup_requires=["wheel"],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "edsdk": ["py.typed", "api.pyi"],
    },
    data_files = [("Lib/site-packages/edsdk", [
        EDSDK_PATH + "/EDSDK_64/Dll/EDSDK.dll",
        EDSDK_PATH + "/EDSDK_64/Dll/EdsImage.dll"])],
    python_requires=">=3.8.0",
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB)",
        "Typing :: Stubs Only",
    ],
    keywords=["edsdk", "canon"],
    license="MIT",
)
