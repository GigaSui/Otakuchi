cmake_minimum_required(VERSION 3.0.0)

project(project VERSION 0.1.0 LANGUAGES C)

file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS "src/*.c" "src/*.h")
add_executable(project ${SOURCES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
