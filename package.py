name = "openexr"

version = "2.2.0"

description = \
    """
    OpenEXR
    """

variants = [
    ["platform-linux"]
]

requires = [
    "ilmbase-2.2.0"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
    	env.CMAKE_MODULE_PATH.append("{root}/cmake")
