add_library(libhwbinder SHARED
	Binder.cpp
	BpHwBinder.cpp
	BufferedTextOutput.cpp
	Debug.cpp
	IInterface.cpp
	IPCThreadState.cpp
	Parcel.cpp
	ProcessState.cpp
	Static.cpp
	TextOutput.cpp
)

target_include_directories(libhwbinder PUBLIC include)
target_link_libraries(libhwbinder libutils libcutils libbinderthreadstate pthread)

install(TARGETS libhwbinder
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/hwbinder DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
