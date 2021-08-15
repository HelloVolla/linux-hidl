add_library(libhidlbase SHARED
        HidlInternal.cpp
        HidlSupport.cpp
        Status.cpp
        TaskRunner.cpp
)

target_include_directories(libhidlbase PUBLIC include)
target_link_libraries(libhidlbase libutils libcutils base)
