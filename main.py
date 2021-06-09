from pathlib import Path
import yaml

import alacritty
import zathura
import nvim

from austral import palette

home = str(Path.home())
with open(home + '/.config/zathura/colors', 'w') as file:
    for line in zathura.generate(palette):
        file.write(line)

alacritty_path = home + '/.config/alacritty/alacritty.yml'
alacritty_config = alacritty.get_current_config(alacritty_path)
alacritty_config['colors'] = alacritty.make_colors_config(palette)
with open(alacritty_path, 'w') as file:
    yaml.dump(alacritty_config, file)

nvim_path = home + '/.config/nvim/colors'
Path(nvim_path).mkdir(parents=True, exist_ok=True)
with open(nvim_path + '/austral.vim', 'w') as file:
    for hi in nvim.generate(palette):
        file.write(hi)
