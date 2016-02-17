find_package(PkgConfig)
set( ENV{PKG_CONFIG_PATH} $ENV{PKG_CONFIG_PATH}:$ENV{REZ_OPENEXR_ROOT}/lib/pkgconfig)
pkg_check_modules (OPENEXR REQUIRED OpenEXR)
set(openexr_INCLUDE_DIRS    ${OPENEXR_INCLUDE_DIRS})
set(openexr_LIBRARY_DIRS    ${OPENEXR_LIBRARY_DIRS})
set(openexr_LIBRARIES       ${OPENEXR_LIBRARIES})

