# IoT Device Specification

> This file acts as a document to IoT Devices.

## IoT Identity (iot_id)

- `IoT Identity` serves as a dict, use to markup an IoT device.


    ### device : string

    > This attribute describes **which kind of IoT device** it is.

    **This can be of these values:**

    - "Raspberry Pi 2 Model B"
    - "Raspberry Pi Zero"
    - Others


    ### label : string

    > This attribute describes **the user-defined label** of an IoT device.

    > It should be *unique*.


    ### tags : list of string

    > This attribute describes the **tags** of the IoT device.

    > It can be seen as **catalogs**.

    For example:

    - idle
    - general
    - remote_controller
    - face_tracer


    ### control-level : int

    > **0 means master**. Others Reserved.

    > Usually high level controlled by low levels.


    ### io : list of *Device IO*

    > It records what **device obtained** by the IoT device.


## Device IO

- `Device IO` is a dict used for record the device info of a device obtained by IoT.


    ### id : string

    > **unique name** for a device


    ### pin : list of int

    > It is used to **record the necessary pins** taken by the device.

    > Notice: A **proper order should match** both the IoT & Device.

    > It is suggested that in order of "GND INPUT(s) OUTPUT(s) VCC"


    ### type : string

    > Which **type of device** it is?

    For example:

    - camera
    - usb_camera
    - screen
    - speaker
    - beeper
    - infrared-emitter   # 红外发射器
    - infrared-receiver  # 红外接收器
    - supersonic-sounding-device  # 超声测距仪
    - digital-sensing-element  # 数字感温元件. 需要数模转换
    - gravity-switch  #  重力开关
    