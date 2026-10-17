#include QMK_KEYBOARD_H
#include "raw_hid.h"
#include <string.h>
#include "rgblight.h"

static char oled_buffer[32] = "       TapPad!";

const uint16_t PROGMEM keymaps[][1][6] = {
    [0] = LAYOUT(
                 KC_F20,
        KC_F13, KC_F14, KC_F15, KC_F16, KC_F17
    )
};

#if defined(ENCODER_ENABLE)
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_F18);
        } else {
            tap_code(KC_F19);
        }
    }
    return false;
}
#endif


void raw_hid_receive(uint8_t *data, uint8_t length) {
    if (length >= 5 && data[0] == 0x10){
        uint8_t brightness = data[4];
        uint8_t r = ((uint16_t)data[1] * brightness)/255;
        uint8_t g = ((uint16_t)data[2] * brightness)/255;
        uint8_t b = ((uint16_t)data[3] * brightness)/255;

        rgblight_enable_noeeprom();
        rgblight_setrgb(r, g, b);
        return;
    }
}

#if defined(OLED_ENABLE)
oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_0;
}

bool oled_task_user(void) {
    oled_on();
    oled_set_cursor(0,1);
    oled_write(oled_buffer, false);
    return false;
}
#endif