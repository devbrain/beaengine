include(GenerateExportHeader)


if (DEFINED BeaEngine_SHARED_LIBS)
    set(BUILD_SHARED_LIBS "${BeaEngine_SHARED_LIBS}")
endif ()


add_library(BeaEngine BeaEngine.c)

generate_export_header(BeaEngine EXPORT_FILE_NAME ${PROJECT_CONFIG_INCLUDE}/beaengine/export.h)

target_compile_options(BeaEngine PRIVATE ${myC_FLAGS})
target_compile_definitions(BeaEngine PUBLIC "$<$<NOT:$<BOOL:${BUILD_SHARED_LIBS}>>:BEAENGINE_STATIC_DEFINE>")
target_include_directories(BeaEngine
  PUBLIC ${BEA_INCLUDE_PATH}
  PRIVATE ${BEA_SRC_ROOT}
  )
target_include_directories(BeaEngine
        PUBLIC
            "$<BUILD_INTERFACE:${PROJECT_INCLUDE}>"
            "$<BUILD_INTERFACE:${PROJECT_CONFIG_INCLUDE}>"
            "$<INSTALL_INTERFACE:include>"

        PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}
        )
add_library(BeaEngine::BeaEngine ALIAS BeaEngine)

set_target_properties(BeaEngine PROPERTIES
        VERSION ${BeaEngine_VERSION}
        SOVERSION ${BeaEngine_VERSION_MAJOR})


