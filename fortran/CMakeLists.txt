cmake_minimum_required(VERSION 3.10)

# set the project name
project(FizzBuzz VERSION 1.0)

# enable Fortran
enable_language(Fortran)

add_subdirectory(src)

# add the executable
add_executable(FizzBuzz ${CMAKE_SOURCE_DIR}/driver/main.f90)

target_link_libraries(FizzBuzz PUBLIC utils simple_fizzbuzz)
#target_link_libraries(FizzBuzz PUBLIC simple_fizzbuzz)

target_include_directories(FizzBuzz PUBLIC
                        "${PROJECT_BINARY_DIR}/src"
                        "${PROJECT_SOURCE_DIR}/src"
                        )
