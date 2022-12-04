

# Example of using the markers_core module and the UsbParMar gadget.

# Add note about OpenSesame prepare vs run.


import marker_management as mark
import time
import utils.GS_timing as timing


# Find the address and make the marker object:
marker_device_type = 'EVA'
device_info = mark.find_device(device_type=marker_device_type, fallback_to_fake=True)
marker_address = device_info['com_port']
marker_manager = mark.MarkerManager(marker_device_type, marker_address, crash_on_marker_errors=False)
marker_manager.set_bits('00000001')
marker_manager.set_bit(0, 'on')

print(marker_manager.device_address)
print(marker_manager.device_properties)


# The marker instance will fallback to using a fake marker device if a suitable one could not be found,
# warn user of this:
# if marker_manager.is_fake():
#     pass
marker_manager.set_value(0)
timing.delay(100)
marker_manager.set_value(3)
timing.delay(100)
marker_manager.set_value(3)
timing.delay(100)
marker_manager.set_value(0)
timing.delay(100)
marker_manager.set_value(0)
timing.delay(100)
marker_manager.set_value(2)
timing.delay(100)
marker_manager.set_value(0)
timing.delay(100)
marker_manager.set_value(3)
marker_manager.set_value(0)
timing.delay(100)

marker_manager.close()

marker_table, marker_summary, errors = marker_manager.gen_marker_table()
marker_manager.save_marker_table()
marker_manager.print_marker_table()