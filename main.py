def pulsador_a():
    basic.show_string("Bienvenido")


def pulsador_b():
    basic.show_icon(IconNames.SILLY)

input.on_button_pressed(Button.A, pulsador_a)
input.on_button_pressed(Button.B, pulsador_b)