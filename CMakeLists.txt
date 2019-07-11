cmake_minimum_required(VERSION 3.11)

find_package(fletch REQUIRED)
find_package(kwiver REQUIRED)

include(kwiver-utils)
include(kwiver-setup-python)
include(kwiver-flags)
include(kwiver-configcheck)

set(kwiver_python_output_path "${CMAKE_BINARY_DIR}/lib/${kwiver_python_subdir}")
add_subdirectory(python)

configure_file( ${CMAKE_SOURCE_DIR}/setup_example.sh.in
                ${CMAKE_BINARY_DIR}/setup_example.sh @ONLY )
configure_file( ${CMAKE_SOURCE_DIR}/pipeline/sender-receiver.pipe.in
                ${CMAKE_BINARY_DIR}/pipeline/sender-receiver.pipe @ONLY )
