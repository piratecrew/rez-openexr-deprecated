name = "openexr"

version = "2.1.0"

description = \
    """
    OpenEXR
    """

variants = [
    ["platform"]
]

build_requires = [
    "ilmbase-2.1.0"
]

requires = [
    "ilmbase-2.1.0"
]

uuid = "repository.openexr"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
