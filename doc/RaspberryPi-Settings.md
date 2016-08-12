# Raspberry Pi Settings


## Set the resolution

In `/boot/config.txt`:

hdmi_force_hotplug=1

#increase HDMI signal strength (just a black screen if not set!)
# config_hdmi_boost=4

#remove black borders
# disable_overscan=1

#set specific CVT mode
hdmi_cvt 800 480 60 6 0 0 1

#set CVT as default, sometimes it will cause a problem
#hdmi_group=2
#hdmi_mode=87



hdmi_cvt=<width> <height> <framerate> <aspect> <margins> <interlace> <rb>
width        width in pixels
height       height in pixels
framerate    framerate in Hz
aspect       aspect ratio 1=4:3, 2=14:9, 3=16:9, 4=5:4, 5=16:10, 6=15:9
margins      0=margins disabled, 1=margins enabled
interlace    0=progressive, 1=interlaced
rb           0=normal, 1=reduced blanking