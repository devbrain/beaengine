cmake_minimum_required (VERSION 3.24)
project (BeaEngine VERSION 5.3.0)


set (CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
set (CMAKE_VERBOSE_MAKEFILE ON)

option (optHAS_OPTIMIZED "Turn Optimizations ON"    OFF)
option (optHAS_SYMBOLS   "Build with debug Symbols" ON)
option (optBUILD_64BIT   "Build 64 bits executable" OFF)
option (optBUILD_DLL     "Build Shared Objects"     OFF)
option (optBUILD_STDCALL "Build using stdcall"      OFF)
option (optBUILD_LITE	 "Build without text disassembly"      OFF)
option (USE_CLANG "build application with clang" OFF)


# determine BEA_COMPILER
if (NOT BEA_COMPILER)
  if (${CMAKE_SYSTEM_NAME} STREQUAL Linux)
    if (WATCOM)
      set (BEA_COMPILER watcom)
    else ()
      if (USE_CLANG)
        set (BEA_COMPILER clang)
      else ()
        set (BEA_COMPILER gnu)
      endif()
    endif ()
  endif ()
  if (${CMAKE_SYSTEM_NAME} STREQUAL FreeBSD)
    set (BEA_COMPILER gnu)
  endif ()
  if (${CMAKE_SYSTEM_NAME} STREQUAL SunOS)
    set (BEA_COMPILER suncc)
  endif ()
  if (${CMAKE_SYSTEM_NAME} STREQUAL Windows)
    if (MINGW OR MSYS)
      set (BEA_COMPILER gnu)
    else ()
      if (CYGWIN)
	set (BEA_COMPILER gnu)
      else ()
	if (BORLAND)
	  set (BEA_COMPILER borland)
	else ()
	  if (MSVC)
	    set (BEA_COMPILER msvc)
	  else ()
	    if (WATCOM)
	      set (BEA_COMPILER watcom)
	    endif ()
	  endif ()
	endif ()
      endif ()
    endif ()
  endif ()
endif ()
# =========================================
# clang configuration
# =========================================
if (BEA_COMPILER STREQUAL clang)
  set (CMAKE_C_COMPILER   clang)
  set (CMAKE_CXX_COMPILER clang++)
  set (BEA_WARNINGS -Wall -W -Wextra -Wconversion -Wno-long-long  -Wshadow  -Wpointer-arith -Wcast-qual  -Wcast-align -Wwrite-strings)
endif ()
# =========================================
# gcc configuration
# =========================================
if (BEA_COMPILER STREQUAL gnu)
  set (CMAKE_C_COMPILER   gcc)
  set (CMAKE_CXX_COMPILER g++)
  set (BEA_WARNINGS -Wall -W -Wextra -Wconversion -Wno-long-long  -Wshadow  -Wpointer-arith -Wcast-qual  -Wcast-align -Wwrite-strings)
  set (BEA_FLAGS    -pedantic -ansi -pipe -fno-common -fshort-enums )
  set (BEA_DEFINITIONS "")
  if (optHAS_SYMBOLS)
    list (APPEND BEA_FLAGS -g)
  endif ()
  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS -fomit-frame-pointer -O2)
  endif ()
  if (optBUILD_64BIT)
    list (APPEND BEA_FLAGS -m64)
  endif ()
  if (optBUILD_STDCALL)
    list (APPEND BEA_DEFINITIONS "-DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    list (APPEND BEA_DEFINITIONS "-DBEA_LIGHT_DISASSEMBLY")
  endif ()
endif ()
# =========================================
# SunStudio configuration
# =========================================
if (BEA_COMPILER STREQUAL suncc)
  set (CMAKE_C_COMPILER   cc)
  set (CMAKE_CXX_COMPILER CC)
  list (APPEND BEA_FLAGS "-xmemalign=ab")
endif ()
# =========================================
# Visual Studio configuration
# =========================================
if (BEA_COMPILER STREQUAL msvc)
  set (CMAKE_C_COMPILER   cl)
  set (CMAKE_CXX_COMPILER cl)
  set (BEA_DEFINITIONS "/DBEA_LACKS_SNPRINTF /D_CRT_SECURE_NO_WARNINGS")

  if (optBUILD_STDCALL)
    set (BEA_DEFINITIONS "${BEA_DEFINITIONS} /DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    set (BEA_DEFINITIONS "${BEA_DEFINITIONS} /DBEA_LIGHT_DISASSEMBLY")
  endif ()
  if (MSVC60)
	set (BEA_WARNINGS /W3)
  else ()
	if (NOT MSVC90)
		set (BEA_WARNINGS /W3 /Wp64)
	else ()
		set (BEA_WARNINGS /W4)
	endif ()
  endif ()

  list (APPEND BEA_FLAGS /Zi)

  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS /O2)
    list (APPEND BEA_DEFINITIONS "/DNDEBUG")
  else ()
    list (APPEND BEA_DEFINITIONS "/D_DEBUG")
  endif ()

  #generate PDB for Debug/RelWithDebInfo builds
  if (optHAS_SYMBOLS)
    if (optBUILD_DLL)
      set (BEA_SHARED_LINKER_FLAGS "${BEA_SHARED_LINKER_FLAGS} /DEBUG /OPT:REF,ICF")
    endif ()
  endif ()

  # determine code generation model
  if (optHAS_OPTIMIZED)
    if (optBUILD_DLL)
      list (APPEND BEA_FLAGS /MD)
    else ()
      list (APPEND BEA_FLAGS /MT)
    endif ()
  else ()
    if (optBUILD_DLL)
      list (APPEND BEA_FLAGS /MDd)
    else ()
      list (APPEND BEA_FLAGS /MTd)
    endif ()
  endif ()
endif ()
# =========================================
# Intel Compiler configuration
# =========================================
if (BEA_COMPILER STREQUAL intel)
  set (CMAKE_C_COMPILER   icc)
  set (CMAKE_CXX_COMPILER icpc)
  set (BEA_WARNINGS -Wall -Wcheck -Wp64 -wd981 -wd1419 -wd1418)
  set (BEA_FLAGS    -ansi -pipe)
  set (BEA_DEFINITIONS "")
  if (optHAS_SYMBOLS)
    list (APPEND BEA_FLAGS -g)
  endif ()
  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS -fomit-frame-pointer -O3 -ip)
  endif ()
  if (optBUILD_64BIT)
    list (APPEND BEA_FLAGS -m64)
  endif ()
  if (optBUILD_STDCALL)
    list (APPEND BEA_DEFINITIONS "-DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    list (APPEND BEA_DEFINITIONS "-DBEA_LIGHT_DISASSEMBLY")
  endif ()
endif ()

# =========================================
# Borland C configuration
# =========================================
if (BEA_COMPILER STREQUAL borland)
  set (CMAKE_C_COMPILER   bcc32)
  set (CMAKE_CXX_COMPILER bcc32)

  set (BEA_WARNINGS -w -wamb -wdef -wnod -wnak -wcln -wsig -wucp)
  set (BEA_FLAGS    -pc -p- -H- -b -d -Hu-)
  set (BEA_DEFINITIONS "")
  if (optHAS_SYMBOLS)
    list (APPEND BEA_FLAGS -v -y -R)
  endif ()
  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS -O2)
  endif ()
  if (optBUILD_64BIT)
	set (BEA_DEFINITIONS "-D_WIN64")
  else ()
	set (BEA_DEFINITIONS "-D_WIN32")
  endif ()
  if (optBUILD_STDCALL)
    list (APPEND BEA_DEFINITIONS "-DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    list (APPEND BEA_DEFINITIONS "-DBEA_LIGHT_DISASSEMBLY")
  endif ()
endif ()
# =========================================
# Watcom C configuration
# =========================================
if (BEA_COMPILER STREQUAL watcom)
  set (CMAKE_C_COMPILER   wcl386)
  set (CMAKE_CXX_COMPILER wcl386)
  set (BEA_DEFINITIONS "-DBEA_STL_CONTAINER_REQUIRES_DEFAULT_CTOR")
  set (BEA_WARNINGS -w2 -wx )
  set (BEA_FLAGS    -q -fpi -fpi87 "-bt=nt" -zq -6r -mf)
  if (optHAS_SYMBOLS)
    list (APPEND BEA_FLAGS -db -d2 )
  endif ()
  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS -ox -s -ors )
  endif ()
  if (optBUILD_64BIT)
#    list (APPEND BEA_FLAGS -m64)
  endif ()

  if (optBUILD_STDCALL)
    set (BEA_DEFINITIONS "${BEA_DEFINITIONS} -DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    set (BEA_DEFINITIONS "${BEA_DEFINITIONS} -DBEA_LIGHT_DISASSEMBLY")
  endif ()
  set (BEA_SHARED_LINKER_FLAGS "-l=nt")
endif ()

# =========================================
# Pelles C configuration
# =========================================
if (BEA_COMPILER STREQUAL pelles)
  set (CMAKE_C_COMPILER   pocc)
  #set (CMAKE_CXX_COMPILER pocc)

  set (BEA_WARNINGS /W2)
  set (BEA_FLAGS    /Gm /Gn)
  set (BEA_DEFINITIONS "")
  if (optHAS_SYMBOLS)
    list (APPEND BEA_FLAGS /Zi )
  endif ()
  if (optHAS_OPTIMIZED)
    list (APPEND BEA_FLAGS /Ox )
  endif ()
  if (optBUILD_64BIT)
#    list (APPEND BEA_FLAGS -m64)
  endif ()
  if (optBUILD_STDCALL)
    list (APPEND BEA_DEFINITIONS "/DBEA_USE_STDCALL")
  endif ()
  if (optBUILD_LITE)
    list (APPEND BEA_DEFINITIONS "/DBEA_LIGHT_DISASSEMBLY")
  endif ()
endif ()




# ============================================
# construct compiler flags
# ============================================
set (myC_FLAGS "")
set (myCXX_FLAGS "")

foreach (flag ${BEA_FLAGS})
  set (myC_FLAGS ${myC_FLAGS} ${flag})
endforeach ()

foreach (flag ${BEA_WARNINGS})
  set (myC_FLAGS ${myC_FLAGS} ${flag})
endforeach ()

foreach (flag ${BEA_FLAGS})
  set (myCXX_FLAGS ${myCXX_FLAGS} ${flag})
endforeach ()

foreach (flag ${BEA_WARNINGS})
  set (myCXX_FLAGS ${myCXX_FLAGS} ${flag})
endforeach ()


# ======================================
# set output dirs
# ======================================
set(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(PROJECT_INCLUDE_PRIVATE ${PROJECT_ROOT}/src)
set(PROJECT_INCLUDE ${PROJECT_ROOT}/include)
set(PROJECT_CONFIG_INCLUDE ${CMAKE_CURRENT_BINARY_DIR}/include)

add_subdirectory(src)

if (BeaEngine_INCLUDE_PACKAGING)
    add_subdirectory(packaging)
endif ()