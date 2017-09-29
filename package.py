name = "openexr"

version = "2.2.0"

description = \
    """
    OpenEXR
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "os-*.*"]
    return [expand_requires(*requires)]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
    	env.CMAKE_MODULE_PATH.append("{root}/cmake")
