import hid

vid = 0xFEED
pid = 0x001
rgb = 0x10
RAW_HID_USAGE_PAGE = 0xFF60

devices = hid.enumerate(vid,pid)
target = next(
    (d for d in devices
        if d.get("usage_page") == RAW_HID_USAGE_PAGE),
    None
)

def set_led(r=255,g=255,b=255,brightness=100):
    try:
        device = hid.device()
        device.open_path(target["path"])
        report = bytes([rgb,r,g,b,brightness])
        report += bytes(32 - len(report))
        device.write(b"\x00" + report)
    finally:
        device.close()
    return [r,g,b,brightness]
if __name__ == "__main__":
    set_led(255,255,255,255)