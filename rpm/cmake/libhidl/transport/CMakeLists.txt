add_hidl(NAME android.hidl.base@1.0 ROOT android.hidl HEADERS android.hidl.manager_1.0
	 SRCS IBase.hal types.hal)
add_hidl(NAME android.hidl.manager@1.0 ROOT android.hidl LINK android.hidl.base_1.0
	 SRCS IServiceManager.hal IServiceNotification.hal)
add_hidl(NAME android.hidl.manager@1.1 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0
	 SRCS IServiceManager.hal)
add_hidl(NAME android.hidl.manager@1.2 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0 android.hidl.manager_1.1
	 SRCS IServiceManager.hal IClientCallback.hal)
add_hidl(NAME android.hidl.token@1.0 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS ITokenManager.hal)
add_hidl(NAME android.hidl.memory@1.0 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS IMapper.hal IMemory.hal)
add_hidl(NAME android.hidl.allocator@1.0 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS IAllocator.hal)
add_hidl(NAME android.hidl.memory.token@1.0 ROOT android.hidl LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS IMemoryToken.hal)
add_hidl(NAME android.hidl.memory.block@1.0 ROOT android.hidl LINK android.hidl.memory.token_1.0
         SRCS types.hal)

add_library(libhidltransport SHARED
        HidlBinderSupport.cpp
        HidlPassthroughSupport.cpp
        HidlTransportSupport.cpp
        HidlTransportUtils.cpp
        ServiceManagement.cpp
        Static.cpp
        ${android.hidl.base_1.0_srcs} ${android.hidl.manager_1.0_srcs} ${android.hidl.manager_1.1_srcs} ${android.hidl.manager_1.2_srcs}
)

target_include_directories(libhidltransport PUBLIC include)
target_link_libraries(libhidltransport libhidlbase libutils libcutils libhwbinder dl)

add_dependencies(libhidltransport android.hidl.base_1.0_target android.hidl.manager_1.0_target android.hidl.manager_1.1_target android.hidl.manager_1.2_target)
target_include_directories(libhidltransport PRIVATE ${android.hidl.base_1.0_outdir} ${android.hidl.manager_1.0_outdir} ${android.hidl.manager_1.1_outdir} ${android.hidl.manager_1.2_outdir} )

install(TARGETS libhidltransport
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/hidl DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
