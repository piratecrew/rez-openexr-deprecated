name = "openexr"

version = "2.1.0"

description = \
    """
    OpenEXR
    """

variants = [
    ["platform-linux"]
]

requires = [
    "ilmbase-2.1.0"
]

uuid = "repository.openexr"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
