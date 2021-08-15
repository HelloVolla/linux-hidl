add_hidl(NAME android.hardware.sensors@1.0 ROOT android.hardware LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS types.hal ISensors.hal)

add_hidl(NAME android.hardware.sensors@2.0 ROOT android.hardware LINK android.hidl.base_1.0 android.hidl.manager_1.0 android.hardware.sensors_1.0
         SRCS types.hal ISensors.hal ISensorsCallback.hal)

add_hidl(NAME android.hardware.vibrator@1.0 ROOT android.hardware LINK android.hidl.base_1.0 android.hidl.manager_1.0
         SRCS types.hal IVibrator.hal)
