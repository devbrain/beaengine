set (BEA_SOURCES BeaEngine.c)


if (optBUILD_DLL)
  add_library (BeaEngine SHARED BeaEngine.c)
  set (BEA_DLL_DEF "-DBUILD_BEA_ENGINE_DLL")
  
else ()
  add_library (BeaEngine STATIC BeaEngine.c)
  set (BEA_DLL_DEF "-DBEA_ENGINE_STATIC") 
endif ()

#target_compile_options(BeaEngine PRIVATE ${myC_FLAGS})
target_compile_definitions(BeaEngine PUBLIC ${BEA_DLL_DEF} ${BEA_DEFINITIONS}) 
target_include_directories(BeaEngine
  PUBLIC ${BEA_INCLUDE_PATH}
  PRIVATE ${BEA_SRC_ROOT}
  )

