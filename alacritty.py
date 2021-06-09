from pathlib import Path
import yaml

from austral import palette

def get_current_config(path):
    path = Path(path)
    if not path.is_file():
        return {}
    with open(path, 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def make_colors_config(palette):
    return {
        'primary': {
            'foreground': palette['fg'],
            'background': palette['bg'],
        },
        'normal': {
            'black':   palette['bg'],
            'red':     palette['red'],
            'green':   palette['green'],
            'yellow':  palette['dark_yellow'],
            'blue':    palette['blue'],
            'magenta': palette['purple'],
            'cyan':    palette['cyan'],
            'white':   palette['white'],
        },
        'bright': {
            'black':   palette['line_grey'],
            'red':     palette['error_red'],
            'green':   palette['light_green'],
            'yellow':  palette['yellow'],
            'blue':    palette['light_blue'],
            'magenta': palette['purple'],
            'cyan':    palette['vivid_blue'],
            'white':   palette['fg'],
        },
        'cursor': {
            'text': 'CellBackground',
            'cursor': palette['green'],
        },
        'vi_mode_cursor': {
            'text': 'CellBackground',
            'cursor': palette['green'],
        },
        'search': {
            'matches': {
                'foreground': palette['dark_yellow'],
                'background': palette['bg'],
            },
            'focused_match': {
                'foreground': 'CellBackground',
                'background': 'CellForeground',
            },
            'bar': {
                'foreground': palette['bg'],
                'background': palette['dark_yellow'],
            },
        },
        'line_indicator': {
            'foreground': palette['bg'],
            'background': palette['dark_yellow'],
        },
    }
