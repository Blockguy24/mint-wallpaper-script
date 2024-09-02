#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path
from random import choice

SYS_BACKGROUNDS = Path("/usr/share/backgrounds")

WALLPAPERS_DAY: list[Path] = [
    SYS_BACKGROUNDS / "linuxmint-ulyana/jankaluza_dew_drop.jpg",
    SYS_BACKGROUNDS / "linuxmint-ulyana/cwale_sheffield.jpg",
    SYS_BACKGROUNDS / "linuxmint-uma/mpiwnicki_bladerunner.jpg",
    SYS_BACKGROUNDS / "linuxmint-una/aburden_frozen_winter_ball.jpg",
    SYS_BACKGROUNDS / "linuxmint-una/mpiwnicki_volcanic_valley.jpg",
    SYS_BACKGROUNDS / "linuxmint-vera/aburden_grass.jpg",
    SYS_BACKGROUNDS / "linuxmint-vera/pczerwinski_3d_render.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/jcorl_white_sands.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/meiying_body_of_water.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/mfakurian_abstract.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/mnohassi_morocco.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/mpiwnick_atacama.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/mpiwnick_atacama.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/mpiwnicki_torres_del_paine.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/slee_blocks.jpg",
]

WALLPAPERS_NIGHT: list[Path] = [
    SYS_BACKGROUNDS / "linuxmint-ulyssa/sshah_star_trails.jpg",
    SYS_BACKGROUNDS / "linuxmint-uma/oram_blue_moon.jpg",
    SYS_BACKGROUNDS / "linuxmint-una/jwarvel_frozen_soap.jpg",
    SYS_BACKGROUNDS / "linuxmint-una/nwatson_eclipse.jpg",
    SYS_BACKGROUNDS / "linuxmint-vanessa/eskof_bubble.jpg",
    SYS_BACKGROUNDS / "linuxmint-vanessa/fakurian_purple.jpg",
    SYS_BACKGROUNDS / "linuxmint-vera/mpiwnicki_red_dusk.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/aksenapati_blanket.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/aksenapati_snow_mountain.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/jcorl_monument_valley.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/jpanchal_cpu.jpg",
    SYS_BACKGROUNDS / "linuxmint-wilma/slee_earth.jpg",
]


def set_wallpaper(path: os.PathLike):
    subprocess.run(
        [
            "gsettings",
            "set",
            "org.cinnamon.desktop.background",
            "picture-uri",
            f"file://{path}",
        ]
    )


def main(argv) -> int | str | None:
    if len(argv) != 4:
        return "Invalid arg count"

    _, event, prev, curr = argv
    if event != "period-changed":
        return f"Unexpected event: {event!r}"

    if curr == "daytime":
        set_wallpaper(choice(WALLPAPERS_DAY))
    elif curr == "night":
        set_wallpaper(choice(WALLPAPERS_NIGHT))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
