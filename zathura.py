mappings = {
    'completion-bg': 'bg',
    'completion-fg': 'fg',
    'completion-group-bg': 'grey',
    'completion-group-fg': 'fg',
    'completion-highlight-bg': 'blue',
    'completion-highlight-fg': 'bg',
    'default-bg': 'bg',
    'default-fg': 'fg',
    'highlight-active-color': 'red',
    'highlight-color': 'blue',
    'index-active-bg': 'blue',
    'index-active-fg': 'bg',
    'index-bg': 'bg',
    'index-fg': 'fg',
    'inputbar-bg': 'bg',
    'inputbar-fg': 'fg',
    'notification-bg': 'bg',
    'notification-error-bg': 'bg',
    'notification-error-fg': 'red',
    'notification-fg': 'blue',
    'notification-warning-bg': 'bg',
    'notification-warning-fg': 'red',
    'recolor-darkcolor': 'fg',
    'recolor-lightcolor': 'bg',
    'render-loading-bg': 'bg',
    'render-loading-fg': 'fg',
    'statusbar-bg': 'bg',
    'statusbar-fg': 'fg',
}

def generate(palette):
    for key, color in mappings.items():
        yield 'set {} {}\n'.format(key, palette[color])
