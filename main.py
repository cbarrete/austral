from pathlib import Path
import zathura

from aurora import palette

with open(str(Path.home()) + '/.config/zathura/colors', 'w') as file:
    for line in zathura.generate(palette):
        file.write(line)
