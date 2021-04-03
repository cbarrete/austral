from pathlib import Path
import yaml

import alacritty
import zathura

from aurora import palette

home = str(Path.home())
with open(home + '/.config/zathura/colors', 'w') as file:
    for line in zathura.generate(palette):
        file.write(line)

alacritty_path = home + '/.config/alacritty/alacritty.yml'
alacritty_config = alacritty.get_current_config(alacritty_path)
alacritty_config['colors'] = alacritty.make_colors_config(palette)
with open(alacritty_path, 'w') as file:
    yaml.dump(alacritty_config, file)
