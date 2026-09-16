"""Shared PetMedic-style transparent gump treatment for release modes."""

import json

SETTING_KEY = "transparent_gumps_by_character"


def enabled(settings_path, player_serial):
    try:
        with open(settings_path, "r") as handle:
            data = json.load(handle)
        choices = data.get(SETTING_KEY, {})
        return bool(choices.get(str(int(player_serial)), False)) if isinstance(choices, dict) else False
    except:
        return False


def toggle(settings_path, player_serial):
    """Save only this character's UI choice; never overwrite another mode's settings."""
    try:
        with open(settings_path, "r") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            data = {}
    except:
        data = {}
    choices = data.get(SETTING_KEY, {})
    if not isinstance(choices, dict):
        choices = {}
    key = str(int(player_serial))
    new_value = not bool(choices.get(key, False))
    choices[key] = new_value
    data[SETTING_KEY] = choices
    with open(settings_path, "w") as handle:
        json.dump(data, handle, indent=2)
    return new_value


def add_background(gumps, gd, width, height, outer, panels, transparent):
    """PetMedic's title drag handle and continuous alpha surface."""
    if not transparent:
        gumps.AddBackground(gd, 0, 0, width, height, outer)
        for x, y, panel_width, panel_height, art in panels:
            gumps.AddBackground(gd, x, y, panel_width, panel_height, art)
        return
    gumps.AddBackground(gd, 0, 0, width, 40, outer)
    gumps.AddAlphaRegion(gd, 0, 0, width, height)
