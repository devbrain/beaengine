set (BEA_SOURCES BeaEngine.c)


if (optBUILD_DLL)
  add_library (BeaEngine SHARED BeaEngine.c)
  set_target_properties (BeaEngine PUBLIC PROPERTIES COMPILE_FLAGS "-DBUILD_BEA_ENGINE_DLL" ${BEA_DEFINITIONS})
  
else ()
  add_library (BeaEngine STATIC BeaEngine.c)
  set_target_properties (BeaEngine PUBLIC PROPERTIES COMPILE_FLAGS "-DBEA_ENGINE_STATIC" ${BEA_DEFINITIONS}) 
endif ()

target_include_directories(BeaEngine PUBLIC ${BEA_INCLUDE_PATH})

