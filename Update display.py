import hid

dev = hid.device()
dev.open(0xFEED, 0x0001)

def update_screen(text):
    payload = [0x00] + list(text.encode("utf-8"))
    payload += [0x00] * (33 - len(payload))
    dev.write(payload)

update_screen("OBS: Recording")