#include QMK_KEYBOARD_H
#include "raw_hid.h"
#include <string.h>

// Base Keymap (Top Center is Mute/Play, Bottom row are F13-F17)
const uint16_t PROGMEM keymaps[][1][6] = {
    [0] = LAYOUT(
                 KC_MPLY,
        KC_F13, KC_F14, KC_F15, KC_F16, KC_F17
    )
};

// Rotary Encoder: Volume Up / Down
#if defined(ENCODER_ENABLE)
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    }
    return false;
}
#endif

// Buffer for host PC text
static char oled_buffer[32] = "TapPad Ready";

// Use raw_hid_receive_user instead of raw_hid_receive to avoid VIA conflicts
void raw_hid_receive_user(uint8_t *data, uint8_t length) {
    memset(oled_buffer, 0, sizeof(oled_buffer));
    strncpy(oled_buffer, (char *)data, sizeof(oled_buffer) - 1);
}

// 0.91" OLED Display Task
#if defined(OLED_ENABLE)
oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_180;
}

bool oled_task_user(void) {
    oled_write_P(PSTR("== TAPPAD DECK ==\n"), false);
    oled_write(oled_buffer, false);
    return false;
}
#endif

// Start RGB LED automatically on boot
void keyboard_post_init_user(void) {
    #if defined(RGBLIGHT_ENABLE)
    rgblight_enable_noeeprom();
    rgblight_sethsv_noeeprom(HSV_CYAN);
    #endif
}