CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(openexr_version ${OPENEXR_VERSION})

set(url_openexr https://github.com/openexr/openexr.git)
set(tag_openexr v${openexr_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# Just Clone and checkout the right tag.
# The build is made in the next External Command.
ExternalProject_add(
  openexr
  GIT_REPOSITORY ${url_openexr}
  GIT_TAG ${tag_openexr}
  PREFIX openexr
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)

#ExternalProject_add(
#    pyilmbase
#    DEPENDS ilmbase
#    PREFIX pyilmbase
#    DOWNLOAD_COMMAND ""
#    PATCH_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/patch_pyilmbase_cmake.sh CMakeLists.txt #Don't really know why i need to do this
#    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/PyIlmBase
#    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF -DBoost_DEBUG=1 -DILMBASE_PACKAGE_PREFIX=${CMAKE_INSTALL_PREFIX} -DBoost_PYTHON_LIBRARY=boost_python -DPYTHON_INCLUDE_DIR=${python_INCLUDE_DIRS} -DPYTHON_LIBRARY=${python_LIBRARIES}
#    BUILD_IN_SOURCE 1
#)

ExternalProject_add(
    openexr_build
    DEPENDS openexr
    DOWNLOAD_COMMAND ""
    PREFIX openexr_build
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/OpenEXR
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DNAMESPACE_VERSIONING=OFF -DILMBASE_PACKAGE_PREFIX=$ENV{REZ_ILMBASE_ROOT}
    #UPDATE_COMMAND ./bootstrap
    #CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --disable-ilmbasetest --with-ilmbase-prefix=$ENV{REZ_ILMBASE_ROOT}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)

rez_install_files(
    cmake/openexr.cmake
    DESTINATION .
)
