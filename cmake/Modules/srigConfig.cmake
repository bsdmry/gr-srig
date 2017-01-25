INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SRIG srig)

FIND_PATH(
    SRIG_INCLUDE_DIRS
    NAMES srig/api.h
    HINTS $ENV{SRIG_DIR}/include
        ${PC_SRIG_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SRIG_LIBRARIES
    NAMES gnuradio-srig
    HINTS $ENV{SRIG_DIR}/lib
        ${PC_SRIG_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SRIG DEFAULT_MSG SRIG_LIBRARIES SRIG_INCLUDE_DIRS)
MARK_AS_ADVANCED(SRIG_LIBRARIES SRIG_INCLUDE_DIRS)

