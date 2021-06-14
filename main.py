import os
from pathlib import Path
import yaml

import alacritty
import nvim
import xresources
import zathura

from austral import palette

home = str(Path.home())
with open(home + '/.config/zathura/colors', 'w') as file:
    for line in zathura.make_colors_config(palette):
        file.write(line + '\n')

alacritty_path = home + '/.config/alacritty/alacritty.yml'
alacritty_config = alacritty.get_current_config(alacritty_path)
alacritty_config['colors'] = alacritty.make_colors_config(palette)
with open(alacritty_path, 'w') as file:
    yaml.dump(alacritty_config, file)

nvim_path = home + '/.config/nvim/colors'
Path(nvim_path).mkdir(parents=True, exist_ok=True)
with open(nvim_path + '/austral.vim', 'w') as file:
    for hi in nvim.generate(palette):
        file.write(hi + '\n')
# TODO go over nvim instances and source config again

xresources_path = home + '/.config/Xresources.colors'
with open(xresources_path, 'w') as file:
    for line in xresources.make_colors_config(palette):
        file.write(line + '\n')
os.system('xrdb -merge ' + xresources_path)

os.system('pkill -USR1 polybar')
