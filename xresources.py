def make_colors_config(palette):
    colors = {
        'background': palette['bg'],
        'foreground': palette['fg'],
        'cursorColor': palette['dark_yellow'],
        'color0': palette['black'],
        'color8': palette['line_grey'],
        'color1': palette['red'],
        'color9': palette['error_red'],
        'color2': palette['green'],
        'color10': palette['light_green'],
        'color3': palette['dark_yellow'],
        'color11': palette['yellow'],
        'color4': palette['blue'],
        'color12': palette['light_blue'],
        'color5': palette['purple'],
        'color13': palette['purple'],
        'color6': palette['cyan'],
        'color14': palette['vivid_blue'],
        'color7': palette['white'],
        'color15': palette['fg'],
    }
    for key, value in colors.items():
        yield '*{}: {}'.format(key, value)
