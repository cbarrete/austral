groups = {
    'Normal': {
        'fg': 'fg',
        'bg': 'bg',
    },
    'Comment': {
        'fg': 'green',
        'gui': 'italic',
    },
    'Constant': {
        'fg': 'yellow',
    },
    'String': {
        'fg': 'orange',
    },
    'Character': {
        'fg': 'orange',
    },
    'Number': {
        'fg': 'light_green',
    },
    'Boolean': {
        'fg': 'blue',
    },
    'Float': {
        'fg': 'light_green',
    },
    'Identifier': {
        'fg': 'blue',
    },
    'Function': {
        'fg': 'yellow',
    },
    'Statement': {
        'fg': 'purple',
    },
    'Conditional': {
        'fg': 'purple',
    },
    'Repeat': {
        'fg': 'purple',
    },
    'Label': {
        'fg': 'light_blue',
    },
    'Operator': {
        'fg': 'purple',
    },
    'Keyword': {
        'fg': 'blue',
    },
    'Exception': {
        'fg': 'purple',
    },
    'PreProc': {
        'fg': 'yellow',
    },
    'Include': {
        'fg': 'purple',
    },
    'Define': {
        'fg': 'purple',
    },
    'Title': {
        'fg': 'cyan',
    },
    'Macro': {
        'fg': 'purple',
    },
    'PreCondit': {
        'fg': 'light_blue',
    },
    'Type': {
        'fg': 'light_blue',
    },
    'StorageClass': {
        'fg': 'light_blue',
    },
    'Structure': {
        'fg': 'yellow',
    },
    'Typedef': {
        'fg': 'yellow',
    },
    'Special': {
        'fg': 'blue',
        'gui': 'italic',
    },
    'SpecialComment': {
        'fg': 'line_grey',
    },
    'Error': {
        'fg': 'error_red',
        'gui': 'bold,reverse',
    },
    'Todo': {
        'fg': 'purple',
        'gui': 'bold,italic',
    },
    'Underlined': {
        'fg': 'cyan',
        'gui': 'underline',
    },
    'Cursor': {
        'gui': 'reverse',
    },

    'ColorColumn': {
        'bg': 'cursor_grey',
    },
    'CursorLineNr': {
        'fg': 'white',
        'gui': 'bold',
    },
    'SignColumn': {
        'bg': 'bg',
    },
    'Conceal': {
        'fg': 'line_grey',
    },
    'CursorColumn': {
        'bg': 'cursor_grey',
    },
    'CursorLine': {
        'bg': 'cursor_grey',
    },
    'Directory': {
        'fg': 'blue',
    },
    'DiffAdd': {
        'fg': 'green',
        'bg': 'bg',
    },
    'DiffChange': {
        'fg': 'yellow',
        'bg': 'bg',
    },
    'DiffDelete': {
        'fg': 'red',
        'bg': 'bg',
    },
    'DiffText': {
        'fg': 'black',
        'bg': 'yellow',
    },
    'diffAdded': {
        'fg': 'green'
    },
    'diffRemoved': {
        'fg': 'red'
    },
    'ErrorMsg': {
        'fg': 'error_red',
    },
    'VertSplit': {
        'fg': 'vertsplit',
    },
    'FoldColumn': {
        'fg': 'yellow',
        'bg': 'bg',
    },
    'Folded': {
        'fg': 'line_grey',
        'bg': 'bg',
        'gui': 'NONE',
    },
    'IncSearch': {
        'fg': 'yellow',
        'bg': 'line_grey',
    },
    'LineNr': {
        'fg': 'gutter_fg_grey',
    },
    'MatchParen': {
        'fg': 'blue',
        'gui': 'underline',
    },
    'NonText': {
        'fg': 'special_grey',
    },
    'Pmenu': {
        'fg': 'white',
        'bg': 'menu_grey',
    },
    'PmenuSel': {
        'fg': 'black',
        'bg': 'blue',
    },
    'PmenuSbar': {
        'bg': 'special_grey',
    },
    'PmenuThumb': {
        'bg': 'white',
    },
    'Question': {
        'fg': 'purple',
    },
    'QuickFixLine': {
        'fg': 'black',
        'bg': 'yellow',
    },
    'Search': {
        'fg': 'black',
        'bg': 'yellow',
    },
    'SpecialKey': {
        'fg': 'special_grey',
    },
    'SpellBad': {
        'fg': 'error_red',
        'gui': 'underline',
    },
    'SpellCap': {
        'fg': 'dark_yellow',
    },
    'SpellLocal': {
        'fg': 'dark_yellow',
    },
    'SpellRare': {
        'fg': 'dark_yellow',
    },
    'StatusLine': {
        'fg': 'white',
        'bg': 'cursor_grey',
        'gui': 'NONE',
    },
    'StatusLineNC': {
        'fg': 'line_grey',
        'bg': 'cursor_grey',
        'gui': 'NONE',
    },
    'TabLine': {
        'fg': 'line_grey',
        'bg': 'bg',
        'gui': 'NONE',
    },
    'TabLineSel': {
        'bg': 'bg',
        'gui': 'NONE',
    },
    'TabLineFill': {
        'bg': 'bg',
        'gui': 'NONE',
    },
    'Terminal': {
        'fg': 'white',
        'bg': 'black',
    },
    'Visual': {
        'bg': 'visual_grey',
    },
    'VisualNOS': {
        'fg': 'visual_grey',
    },
    'WarningMsg': {
        'bg': 'yellow',
    },
    'WildMenu': {
        'fg': 'black',
        'bg': 'blue',
    },
    'EndOfBuffer': {
        'fg': 'black',
    },
}

def generate(palette):
    for group, values in groups.items():
        line = 'hi {}'.format(group)
        if 'fg' in values:
            line += ' guifg=' + palette[values['fg']]
        if 'bg' in values:
            line += ' guibg=' + palette[values['bg']]
        if 'gui' in values:
            line += ' gui=' + values['gui']
        line += '\n'
        yield line
