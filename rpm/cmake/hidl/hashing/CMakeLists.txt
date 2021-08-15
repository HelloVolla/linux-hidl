add_library(libhidl-gen-hash SHARED
    Hash.cpp
)
target_include_directories(libhidl-gen-hash PUBLIC include)
target_include_directories(libhidl-gen-hash PRIVATE include/hidl-hash)
target_link_libraries(libhidl-gen-hash libutils libcutils libbase ${CRYPTO_LIBRARIES})

install(TARGETS libhidl-gen-hash
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)
