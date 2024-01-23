import pytest
from camera_API import Camera_API

cam_node = 0
check_hidcam = False
streaming_duration = None
streaming_show_FPS = None
set_resolution_width = None
set_resolution_height = None
set_resolution_format = None
set_resolution_fps = None
uvc_var_parameter_name = None
uvc_var_min = -10
uvc_var_max = 10
uvc_var_step = 5
uvc_multiple_var_parameter_name1 = "brightness"
uvc_multiple_var_min1 = -10
uvc_multiple_var_max1 = 10
uvc_multiple_var_step1 = 5
uvc_multiple_var_parameter_name2 = "zoom"
uvc_multiple_var_min2 = 100
uvc_multiple_var_max2 = 800
uvc_multiple_var_step2 = 100
hid_var_min = 1
hid_var_max = 4
hid_var_step = 1
byte_number = 2
cam_ID = None
get_parameter_ID = None
set_parameter_ID = None
set_parameter_value_ID = None
hold = 2
image_save = False
save_format = "png"


#==================================================================================

ex_open_camera = "0"
ex_pid = "c130"
ex_vid = "2560"
ex_get_device_path = None
ex_get_firmware_version = None
ex_getting_unique_ID = None
ex_get_supported_resolution = None
ex_getting_supported_uvc_parameter = None
ex_streaming = None
ex_set_resolution = None
ex_uvc_var = None
ex_uvc_multiple_var = None
ex_get_hid = None
ex_set_hid = None
ex_hid_var = None
ex_set_hid_default = None


data_set = {"open_camera":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e",TypeError),   # invalid cam_node (same datatype)
                    (0.0,"e",TypeError),  # invalid cam_node (diff datatype - "float")
                    ("0","e",TypeError),   # invalid cam_node (diff datatype - "str")
                    (False,"e",TypeError)    # invalid cam_node (diff datatype - "bool")
                ],
            "get_pid":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,None,TypeError),  # invalid cam_node (diff datatype - "float")
                    ("0",None,TypeError),   # invalid cam_node (diff datatype - "str")
                    (False,None,TypeError)    # invalid cam_node (diff datatype - "bool")
                ],
            "get_vid":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "get_device_path":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "get_firmware_version":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "getting_unique_ID":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "get_supported_resolution":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "getting_supported_uvc_parameter":
                [# Format : (cam_node, expected_error_code, expected_error_type),
                    (cam_node, 0, None),     #valid input

                    (-1,"e","et"),   # invalid cam_node (same datatype)
                    (0.0,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0","e","et"),   # invalid cam_node (diff datatype - "str")
                    (False,"e","et")    # invalid cam_node (diff datatype - "bool")
                ],
            "streaming":
                [# Format : (cam_node, duration, show_FPS, expected_error_code, expected_error_type),
                    (cam_node, streaming_duration, streaming_show_FPS, 0, None),     #valid input
                    # need to add one more valid data for duration "0" after implementation for streaming end.

                    (-1, streaming_duration, streaming_show_FPS,"e","et"),   # invalid cam_node (same datatype)
                    (0.0, streaming_duration, streaming_show_FPS,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", streaming_duration, streaming_show_FPS,"e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, streaming_duration, streaming_show_FPS,"e","et"),    # invalid cam_node (diff datatype - "bool")

                    (cam_node, -1, streaming_show_FPS,"e","et"),   # invalid streaming_duration (same datatype)
                    (cam_node, 5.0, streaming_show_FPS,"e","et"),  # invalid streaming_duration (diff datatype - "float")
                    (cam_node, "5", streaming_show_FPS,"e","et"),   # invalid streaming_duration (diff datatype - "str")
                    (cam_node, True, streaming_show_FPS,"e","et"),    # invalid streaming_duration (diff datatype - "bool")

                    (cam_node, streaming_duration, 1.0,"e","et"),  # invalid streaming_show_FPS (diff datatype - "float")
                    (cam_node, streaming_duration, "1","e","et"),   # invalid streaming_show_FPS (diff datatype - "str")
                    (cam_node, streaming_duration, 1,"e","et"),    # invalid streaming_show_FPS (diff datatype - "int")

                    (-1, -1, None,"e","et"),                      # All invalid values (instead of bool values None was used)

                ],
            "set_resolution":
                [# Format : (cam_node, width, height, format, fps, expected_error_code, expected_error_type),
                    (cam_node, set_resolution_width, set_resolution_height, set_resolution_format, set_resolution_fps, 0, None),     #valid input

                    (-1, set_resolution_width, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),   # invalid cam_node (same datatype)
                    (0.0, set_resolution_width, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", set_resolution_width, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, set_resolution_width, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),    # invalid cam_node (diff datatype - "bool")

                    (cam_node, -1, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),   # invalid set_resolution_width (same datatype)
                    (cam_node, 1280.0, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),  # invalid set_resolution_width (diff datatype - "float")
                    (cam_node, "1280", set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),   # invalid set_resolution_width (diff datatype - "str")
                    (cam_node, True, set_resolution_height, set_resolution_format, set_resolution_fps,"e","et"),    # invalid set_resolution_width (diff datatype - "bool")

                    (cam_node, set_resolution_width, -1, set_resolution_format, set_resolution_fps,"e","et"),   # invalid set_resolution_height (same datatype)
                    (cam_node, set_resolution_width, 720.0, set_resolution_format, set_resolution_fps,"e","et"),  # invalid set_resolution_height (diff datatype - "float")
                    (cam_node, set_resolution_width, "720", set_resolution_format, set_resolution_fps,"e","et"),   # invalid set_resolution_height (diff datatype - "str")
                    (cam_node, set_resolution_width, True, set_resolution_format, set_resolution_fps,"e","et"),    # invalid set_resolution_height (diff datatype - "bool")

                    (cam_node, set_resolution_width, set_resolution_height, "UY", set_resolution_fps,"e","et"),   # invalid set_resolution_format (same datatype)
                    (cam_node, set_resolution_width, set_resolution_height, 1.0, set_resolution_fps,"e","et"),  # invalid set_resolution_format (diff datatype - "float")
                    (cam_node, set_resolution_width, set_resolution_height, int, set_resolution_fps,"e","et"),   # invalid set_resolution_format (diff datatype - "int")
                    (cam_node, set_resolution_width, set_resolution_height, True, set_resolution_fps,"e","et"),    # invalid set_resolution_format (diff datatype - "bool")

                    (cam_node, set_resolution_width, set_resolution_height, set_resolution_format, -1,"e","et"),   # invalid set_resolution_fps (same datatype)
                    (cam_node, set_resolution_width, set_resolution_height, set_resolution_format, 60.0,"e","et"),  # invalid set_resolution_fps (diff datatype - "float")
                    (cam_node, set_resolution_width, set_resolution_height, set_resolution_format, "60","e","et"),   # invalid set_resolution_fps (diff datatype - "str")
                    (cam_node, set_resolution_width, set_resolution_height, set_resolution_format, True,"e","et"),    # invalid set_resolution_fps (diff datatype - "bool")
                ],
            "uvc_var":
                [# Format : (cam_node, parameter_name, min, max, step, hold, image_save, save_format, expected_error_code, expected_error_type),
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, 0, None),     #valid input

                    (-1, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid cam_node (same datatype)
                    (0.0, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),    # invalid cam_node (diff datatype - "bool")

                    (cam_node, "bright", uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_parameter_name (same datatype)
                    (cam_node, 0.0, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),  # invalid uvc_var_parameter_name (diff datatype - "float")
                    (cam_node, 0, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_parameter_name (diff datatype - "int")
                    (cam_node, False, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),    # invalid uvc_var_parameter_name (diff datatype - "bool")

                    # (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_min (same datatype)
                    (cam_node, uvc_var_parameter_name, float(uvc_var_min), uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),  # invalid uvc_var_min (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, str(uvc_var_min), uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_min (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, True, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),    # invalid uvc_var_min (diff datatype - "bool")

                    # (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_max (same datatype)
                    (cam_node, uvc_var_parameter_name, uvc_var_min, float(uvc_var_max), uvc_var_step, hold, image_save, save_format, "e","et"),  # invalid uvc_var_max (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, str(uvc_var_max), uvc_var_step, hold, image_save, save_format, "e","et"),   # invalid uvc_var_max (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, True, uvc_var_step, hold, image_save, save_format, "e","et"),    # invalid uvc_var_max (diff datatype - "bool")

                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, 0, hold, image_save, save_format, "e","et"),   # invalid uvc_var_step (same datatype)
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, float(uvc_var_step), hold, image_save, save_format, "e","et"),  # invalid uvc_var_step (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, str(uvc_var_step), hold, image_save, save_format, "e","et"),   # invalid uvc_var_step (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, True, hold, image_save, save_format, "e","et"),    # invalid uvc_var_step (diff datatype - "bool")

                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, 0, image_save, save_format, "e","et"),   # invalid hold (same datatype)
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, 1.0, image_save, save_format, "e","et"),  # invalid hold (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, "1", image_save, save_format, "e","et"),   # invalid hold (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, True, image_save, save_format, "e","et"),    # invalid hold (diff datatype - "bool")

                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, None, save_format, "e","et"),   # invalid image_save (same datatype)
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, 1.0, save_format, "e","et"),  # invalid image_save (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, "1", save_format, "e","et"),   # invalid image_save (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, 1, save_format, "e","et"),    # invalid image_save (diff datatype - "int")

                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, "bmpp", "e","et"),   # invalid save_format (same datatype)
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, 1.0, "e","et"),  # invalid save_format (diff datatype - "float")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, 1, "e","et"),   # invalid save_format (diff datatype - "str")
                    (cam_node, uvc_var_parameter_name, uvc_var_min, uvc_var_max, uvc_var_step, hold, image_save, True, "e","et"),    # invalid save_format (diff datatype - "bool")
                ],
            "uvc_multiple_var":
                [# Format : (cam_node, parameter_name1, min1, max1, step1, parameter_name2, min2, max2, step2, hold, image_save, save_format, expected_error_code, expected_error_type),
                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1,
                    uvc_multiple_var_parameter_name2, uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, 0, None),  # valid input


                    (-1, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid cam_node (same datatype)

                    (0.0, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid cam_node (diff datatype - "float")

                    ("0", uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid cam_node (diff datatype - "str")

                    (False, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid cam_node (diff datatype - "bool")

                    (cam_node, "bright", uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name1 (same datatype)

                    (cam_node, 0.0, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name1 (diff datatype - "float")

                    (cam_node, 0, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name1 (diff datatype - "int")

                    (cam_node, False, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name1 (diff datatype - "bool")

                    # (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                    #  uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid cam_node (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, 0.0, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min1 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, 0, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min1 (diff datatype - "int")

                    (cam_node, uvc_multiple_var_parameter_name1, False, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min1 (diff datatype - "bool")

                    # (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                    #  uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max1 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, 1.0, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max1 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, 1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max1 (diff datatype - "int")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, True, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max1 (diff datatype - "bool")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, 0, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step1 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, 1.0, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step1 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, "1", uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step1 (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, True, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step1 (diff datatype - "bool")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, "zooom",
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name2 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, 1.0,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name2 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, 1,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name2 (diff datatype - "int")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, True,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_parameter_name2 (diff datatype - "bool")

                    # (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     # uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min2 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     float(uvc_multiple_var_min2), uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min2 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     str(uvc_multiple_var_min2), uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min2 (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     False, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_min2 (diff datatype - "bool")

                    # (-1, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     # uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max2 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, float(uvc_multiple_var_max2), uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max2 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, str(uvc_multiple_var_max2), uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max2 (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, True, uvc_multiple_var_step2, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_max2 (diff datatype - "bool")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, 0, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step2 (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, 0.0, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step2 (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, "0", hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step2 (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, False, hold, image_save, save_format, "e","et"),   # invalid uvc_multiple_var_step2 (diff datatype - "bool")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, 0, image_save, save_format, "e","et"),   # invalid hold (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, 1.0, image_save, save_format, "e","et"),   # invalid hold (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, "1", image_save, save_format, "e","et"),   # invalid hold (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, True, image_save, save_format, "e","et"),   # invalid hold (diff datatype - "bool")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, None, save_format, "e","et"),   # invalid image_save (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, 1.0, save_format, "e","et"),   # invalid image_save (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, "1", save_format, "e","et"),   # invalid image_save (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, 1, save_format, "e","et"),   # invalid image_save (diff datatype - "int")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, "bmpp", "e","et"),   # invalid save_format (same datatype)

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, 1.0, "e","et"),   # invalid save_format (diff datatype - "float")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, 1, "e","et"),   # invalid save_format (diff datatype - "str")

                    (cam_node, uvc_multiple_var_parameter_name1, uvc_multiple_var_min1, uvc_multiple_var_max1, uvc_multiple_var_step1, uvc_multiple_var_parameter_name2,
                     uvc_multiple_var_min2, uvc_multiple_var_max2, uvc_multiple_var_step2, hold, image_save, True, "e","et"),   # invalid save_format (diff datatype - "bool")
                ],
            "get_hid":
                [# Format : (cam_node, cam_ID, get_parameter_ID, expected_error_code, expected_error_type),
                    (cam_node, cam_ID, get_parameter_ID, 0, None),     #valid input

                    (-1, cam_ID, get_parameter_ID, "e","et"),   # invalid cam_node (same datatype)
                    (0.0, cam_ID, get_parameter_ID, "e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", cam_ID, get_parameter_ID, "e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, cam_ID, get_parameter_ID, "e","et"),    # invalid cam_node (diff datatype - "bool")

                    # (cam_node, cam_ID, get_parameter_ID, "e","et"),   # invalid cam_ID (same datatype)
                    (cam_node, 1.0, get_parameter_ID, "e","et"),  # invalid cam_ID (diff datatype - "float")
                    (cam_node, "0xFF", get_parameter_ID, "e","et"),   # invalid cam_ID (diff datatype - "str")
                    (get_parameter_ID, True, get_parameter_ID, "e","et"),    # invalid cam_ID (diff datatype - "bool")

                    # (cam_node, cam_ID, get_parameter_ID, "e","et"),   # invalid get_parameter_ID (same datatype)
                    (cam_node, cam_ID, 1.0, "e","et"),  # invalid get_parameter_ID (diff datatype - "float")
                    (cam_node, cam_ID, "0xFF", "e","et"),   # invalid get_parameter_ID (diff datatype - "str")
                    (cam_node, cam_ID, True, "e","et"),    # invalid get_parameter_ID (diff datatype - "bool")
                ],
            "set_hid":
                [# Format : (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, expected_error_code, expected_error_type),
                    (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, 0, None),     #valid input

                    (-1, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid cam_node (same datatype)
                    (0.0, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),    # invalid cam_node (diff datatype - "bool")

                    # (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid cam_ID (same datatype)
                    (cam_node, 1.0, set_parameter_ID, set_parameter_value_ID, "e","et"),  # invalid cam_ID (diff datatype - "float")
                    (cam_node, "0xFF", set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid cam_ID (diff datatype - "str")
                    (get_parameter_ID, True, set_parameter_ID, set_parameter_value_ID, "e","et"),    # invalid cam_ID (diff datatype - "bool")

                    # (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid set_parameter_ID (same datatype)
                    (cam_node, cam_ID, 1.0, set_parameter_value_ID, "e","et"),  # invalid set_parameter_ID (diff datatype - "float")
                    (cam_node, cam_ID, "0xFF", set_parameter_value_ID, "e","et"),   # invalid set_parameter_ID (diff datatype - "str")
                    (cam_node, cam_ID, True, set_parameter_value_ID, "e","et"),    # invalid set_parameter_ID (diff datatype - "bool")

                    # (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid set_parameter_ID (same datatype)
                    (cam_node, cam_ID, set_parameter_ID, 1.0, "e","et"),  # invalid set_parameter_ID (diff datatype - "float")
                    (cam_node, cam_ID, set_parameter_ID, "0xFF", "e","et"),   # invalid set_parameter_ID (diff datatype - "str")
                    (cam_node, cam_ID, set_parameter_ID, True, "e","et"),    # invalid set_parameter_ID (diff datatype - "bool")
                ],
            "hid_var":
                [# Format : (cam_node, cam_ID, set_parameter_ID, min, max, step, byte_number, get_parameter_ID, hold, image_save, save_format, expected_error_code, expected_error_type),
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format, 0, None),     #valid input

                    (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid cam_node (same datatype)
                    (0.0, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid cam_node (diff datatype - "bool")

                    # (cam_node, 0xFF, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid cam_ID (same datatype)
                    (cam_node, 1.0, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid cam_ID (diff datatype - "float")
                    (cam_node, "0xFF", set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid cam_ID (diff datatype - "str")
                    (cam_node, True, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid cam_ID (diff datatype - "bool")

                    # (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid set_parameter_ID (same datatype)
                    (cam_node, cam_ID, 1.0, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid set_parameter_ID (diff datatype - "float")
                    (cam_node, cam_ID, "0xFF", hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid set_parameter_ID (diff datatype - "str")
                    (cam_node, cam_ID, True, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid set_parameter_ID (diff datatype - "bool")

                    # (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_min (same datatype)
                    (cam_node, cam_ID, set_parameter_ID, 1.0, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid hid_var_min (diff datatype - "float")
                    (cam_node, cam_ID, set_parameter_ID, "1", hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_min (diff datatype - "str")
                    (cam_node, cam_ID, set_parameter_ID, True, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid hid_var_min (diff datatype - "bool")

                    # (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_max (same datatype)
                    (0.0, cam_ID, set_parameter_ID, hid_var_min, 1.0, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid hid_var_max (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, hid_var_min, "1", hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_max (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, hid_var_min, True, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid hid_var_max (diff datatype - "bool")

                    (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, 0, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_step (same datatype)
                    (0.0, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, 1.0, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid hid_var_step (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, hid_var_min, hid_var_max, "1", byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid hid_var_step (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, True, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid hid_var_step (diff datatype - "bool")

                    (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, -2, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid byte_number (same datatype)
                    (0.0, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, 2.0, get_parameter_ID, hold, image_save, save_format,"e","et"),  # invalid byte_number (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, "2", get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid byte_number (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, True, get_parameter_ID, hold, image_save, save_format,"e","et"),    # invalid byte_number (diff datatype - "bool")

                    # (-1, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, save_format,"e","et"),   # invalid get_parameter_ID (same datatype)
                    (0.0, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, 1.0, hold, image_save, save_format,"e","et"),  # invalid get_parameter_ID (diff datatype - "float")
                    ("0", cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, "0xFF", hold, image_save, save_format,"e","et"),   # invalid get_parameter_ID (diff datatype - "str")
                    (False, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, True, hold, image_save, save_format,"e","et"),    # invalid get_parameter_ID (diff datatype - "bool")

                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, 0, image_save, save_format,"e","et"),   # invalid hold (same datatype)
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, 1.0, image_save, save_format,"e","et"),  # invalid hold (diff datatype - "float")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, "1", image_save, save_format,"e","et"),   # invalid hold (diff datatype - "str")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, True, image_save, save_format,"e","et"),    # invalid hold (diff datatype - "bool")

                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, None, save_format,"e","et"),   # invalid image_save (same datatype)
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, 1.0, save_format,"e","et"),  # invalid image_save (diff datatype - "float")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, "1", save_format,"e","et"),   # invalid image_save (diff datatype - "str")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, 1, save_format,"e","et"),    # invalid image_save (diff datatype - "int")

                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, "bmpp","e","et"),   # invalid save_format (same datatype)
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, 1.0,"e","et"),  # invalid save_format (diff datatype - "float")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, 1,"e","et"),   # invalid save_format (diff datatype - "str")
                    (cam_node, cam_ID, set_parameter_ID, hid_var_min, hid_var_max, hid_var_step, byte_number, get_parameter_ID, hold, image_save, True,"e","et"),    # invalid save_format (diff datatype - "bool")
                ],
            "set_hid_default":
                [# Format : (cam_node, cam_ID expected_error_code, exoected_error_type),
                    (cam_node, cam_ID, 0, None),     #valid input

                    (-1, cam_ID, "e","et"),   # invalid cam_node (same datatype)
                    (0.0, cam_ID, "e","et"),  # invalid cam_node (diff datatype - "float")
                    ("0", cam_ID, "e","et"),   # invalid cam_node (diff datatype - "str")
                    (False, cam_ID, "e","et"),    # invalid cam_node (diff datatype - "bool")

                    # (cam_node, cam_ID, set_parameter_ID, set_parameter_value_ID, "e","et"),   # invalid cam_ID (same datatype)
                    (cam_node, 1.0, "e","et"),  # invalid cam_ID (diff datatype - "float")
                    (cam_node, "0xFF", "e","et"),   # invalid cam_ID (diff datatype - "str")
                    (get_parameter_ID, True, "e","et"),    # invalid cam_ID (diff datatype - "bool")
                ]
}

class functions:

    def get_devices(self,para_ec,para_et):
        get_devices = Camera_API.get_devices()


    def open_camera(self,para_node,para_ec,para_et):
        open_camera = Camera_API.open_camera(para_node)


    def get_pid(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        pid = Camera_API.get_PID(para_node)


    def get_vid(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        vid = Camera_API.get_VID(para_node)


    def get_device_path(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        get_device_path = Camera_API.get_device_path(para_node)


    def get_firmware_version(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        get_firmware_version = Camera_API.get_firmware_version(para_node)


    def getting_unique_ID(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        getting_unique_ID = Camera_API.getting_unique_ID(para_node)


    def get_supported_resolutions(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        get_supported_resolutions = Camera_API.get_supported_resolutions(para_node)


    def getting_supported_uvc_parameter(self,para_node,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        getting_supported_uvc_parameter = Camera_API.getting_supported_uvc_parameter(para_node)


    def streaming(self,para_node,para_duration,para_show_FPS,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        streaming = Camera_API.streaming(para_node,para_duration,para_show_FPS)


    def set_resolution(self,para_node,para_width,para_height,para_format,para_fps,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        streaming = Camera_API.streaming(para_node,para_width,para_height,para_format,para_fps)


    def uvc_var(self,para_node,para_parameter_name,para_min,para_max,para_step,para_hold,para_image_save,
                para_save_format,para_ec,para_et):

        Camera_API.open_camera(cam_node)
        uvc_var = Camera_API.uvc_var(para_node,para_parameter_name,para_min,para_max,para_step,para_hold,
                                     para_image_save,para_save_format)


    def uvc_multiple_var(self,para_node,para_parameter_name1,para_min1,para_max1,para_step1,para_parameter_name2,
                         para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format,para_ec,para_et):

        Camera_API.open_camera(cam_node)
        uvc_multiple_var = Camera_API.uvc_multiple_var(para_node,para_parameter_name1,para_min1,para_max1,
                           para_step1,para_parameter_name2,para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format)


    def get_hid(self,para_node,para_cam_ID,para_get_parameter_ID,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        get_hid = Camera_API.get_hid(para_node,para_cam_ID,para_get_parameter_ID)


    def set_hid(self,para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        set_hid = Camera_API.set_hid(para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID)


    def hid_var(self,para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,
                para_get_parameter_ID,para_hold,para_image_save,para_save_format,para_ec,para_et):

        Camera_API.open_camera(cam_node)
        hid_var = Camera_API.hid_var(para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,
                para_get_parameter_ID,para_hold,para_image_save,para_save_format)


    def set_hid_default(self,para_node,para_cam_ID,para_ec,para_et):
        Camera_API.open_camera(cam_node)
        set_hid_default = Camera_API.set_hid_default(para_node,para_cam_ID)

class Test_valid_invalid_data:

    def test1_get_devices(self,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_devices(self,para_ec,para_et)
        else:
            functions.get_devices(self,para_ec,para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["open_camera"])
    def test2_open_camera(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.open_camera(self,para_node,para_ec,para_et)
        else:
            functions.open_camera(self,para_node,para_ec,para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["get_pid"])
    def test3_get_pid(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_pid(self,para_node,para_ec,para_et)
        else:
            functions.get_pid(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["get_vid"])
    def test4_get_vid(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_vid(self, para_node, para_ec, para_et)
        else:
            functions.get_vid(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["get_device_path"])
    def test5_get_device_path(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_device_path(self, para_node, para_ec, para_et)
        else:
            functions.get_device_path(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["get_firmware_version"])
    def test6_get_firmware_version(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_firmware_version(self, para_node, para_ec, para_et)
        else:
            functions.get_firmware_version(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["getting_unique_ID"])
    def test7_getting_unique_ID(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.getting_unique_ID(self, para_node, para_ec, para_et)
        else:
            functions.getting_unique_ID(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["get_supported_resolution"])
    def test8_get_supported_resolutions(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_supported_resolutions(self, para_node, para_ec, para_et)
        else:
            functions.get_supported_resolutions(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node, para_ec, para_et", data_set["getting_supported_uvc_parameter"])
    def test9_getting_supported_uvc_parameter(self,para_node,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.getting_supported_uvc_parameter(self, para_node, para_ec, para_et)
        else:
            functions.getting_supported_uvc_parameter(self, para_node, para_ec, para_et)

    @pytest.mark.parametrize("para_node,para_duration,para_show_FPS,para_ec,para_et", data_set["streaming"])
    def test10_streaming(self,para_node,para_duration,para_show_FPS,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.streaming(self,para_node,para_duration,para_show_FPS,para_ec,para_et)
        else:
            functions.streaming(self,para_node,para_duration,para_show_FPS,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_width,para_height,para_format,para_fps,para_ec,para_et", data_set["set_resolution"])
    def test11_set_resolution(self,para_node,para_width,para_height,para_format,para_fps,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.set_resolution(self,para_node,para_width,para_height,para_format,para_fps,para_ec,para_et)
        else:
            functions.set_resolution(self,para_node,para_width,para_height,para_format,para_fps,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_parameter_name,para_min,para_max,para_step,para_hold,para_image_save,para_save_format,para_ec,para_et", data_set["uvc_var"])
    def test12_uvc_var(self,para_node,para_parameter_name,para_min,para_max,para_step,para_hold,para_image_save,
                para_save_format,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.uvc_var(self,para_node,para_parameter_name,para_min,para_max,para_step,para_hold,para_image_save,
                para_save_format,para_ec,para_et)
        else:
            functions.uvc_var(self,para_node,para_parameter_name,para_min,para_max,para_step,para_hold,para_image_save,
                para_save_format,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_parameter_name1,para_min1,para_max1,para_step1,para_parameter_name2,para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format,para_ec,para_et", data_set["uvc_multiple_var"])
    def test13_uvc_multiple_var(self,para_node,para_parameter_name1,para_min1,para_max1,para_step1,para_parameter_name2,
                         para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.uvc_multiple_var(self,para_node,para_parameter_name1,para_min1,para_max1,para_step1,para_parameter_name2,
                         para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format,para_ec,para_et)
        else:
            functions.uvc_multiple_var(self,para_node,para_parameter_name1,para_min1,para_max1,para_step1,para_parameter_name2,
                         para_min2,para_max2,para_step2,para_hold,para_image_save,para_save_format,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_cam_ID,para_get_parameter_ID,para_ec,para_et", data_set["get_hid"])
    def test14_get_hid(self,para_node,para_cam_ID,para_get_parameter_ID,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.get_hid(self,para_node,para_cam_ID,para_get_parameter_ID,para_ec,para_et)
        else:
            functions.get_hid(self,para_node,para_cam_ID,para_get_parameter_ID,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID,para_ec,para_et", data_set["set_hid"])
    def test15_set_hid(self,para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.set_hid(self,para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID,para_ec,para_et)
        else:
            functions.set_hid(self,para_node,para_cam_ID,para_set_parameter_ID,para_set_parameter_value_ID,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,para_get_parameter_ID,para_hold,para_image_save,para_save_format,para_ec,para_et", data_set["hid_var"])
    def test16_hid_var(self,para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,
                para_get_parameter_ID,para_hold,para_image_save,para_save_format,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.hid_var(self,para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,
                para_get_parameter_ID,para_hold,para_image_save,para_save_format,para_ec,para_et)
        else:
            functions.hid_var(self,para_node,para_cam_ID,para_set_parameter_ID,para_min,para_max,para_step,para_byte_number,
                para_get_parameter_ID,para_hold,para_image_save,para_save_format,para_ec,para_et)

    @pytest.mark.parametrize("para_node,para_cam_ID,para_ec,para_et", data_set["set_hid_default"])
    def test17_set_hid_default(self,para_node,para_cam_ID,para_ec,para_et):
        if para_ec == None:
            with pytest.raises(para_et):
                functions.set_hid_default(self,para_node,para_cam_ID,para_ec,para_et)
        else:
            functions.set_hid_default(self,para_node,para_cam_ID,para_ec,para_et)
















