import setuptools

# This is meant to shadow the openxlab pip package.
# So this fork of openxlab is not meant to be registered on pip.
setuptools.setup(
    name="openxlab",
    version="0.1.2.3.12",
    zip_safe=True,
)
