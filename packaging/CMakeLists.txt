include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

if (NOT DEFINED BeaEngine_INSTALL_CMAKEDIR)
    set(BeaEngine_INSTALL_CMAKEDIR "${CMAKE_INSTALL_LIBDIR}/cmake/bsw" CACHE STRING "Path to bsw CMake files")
endif ()

install(TARGETS bsw EXPORT BeaEngine_Targets
        RUNTIME COMPONENT BeaEngine_Runtime
        LIBRARY COMPONENT BeaEngine_Runtime
        NAMELINK_COMPONENT BeaEngine_Development
        ARCHIVE COMPONENT BeaEngine_Development
        INCLUDES DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")

install(DIRECTORY
            "${BeaEngine_SOURCE_DIR}/include/"
            "${BeaEngine_BINARY_DIR}/src/include/"
        TYPE INCLUDE
        COMPONENT BeaEngine_Development)

if (BUILD_SHARED_LIBS)
    set(type shared)
else ()
    set(type static)
endif ()

install(EXPORT BeaEngine_Targets
        DESTINATION "${BeaEngine_INSTALL_CMAKEDIR}"
        NAMESPACE bsw::
        FILE bsw-${type}-targets.cmake
        COMPONENT BeaEngine_Development)

write_basic_package_version_file(
    bswConfigVersion.cmake
    COMPATIBILITY SameMajorVersion)

install(FILES
        "${CMAKE_CURRENT_SOURCE_DIR}/bswConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/bswConfigVersion.cmake"
        DESTINATION "${BeaEngine_INSTALL_CMAKEDIR}"
        COMPONENT BeaEngine_Development)

