# ============================================================
# ChestLoot Pro - Readable Integration Build
# Version: 1.0
# - Preserves settings and recorded-item changes saved by a mode when control
#   returns to Mode Selection or the controller closes.
# Tagline: From lock to loot.
#
# READABLE MULTI-FILE PUBLIC RELEASE
#
# Approved behavioral sources:
#   Dungeon Chest v0.4.17
#   Shop Chest v0.2.4
#   Exodus Decorative Box v0.3.25
#
# This file intentionally contains ordinary, readable Razor Enhanced Python.
# No encoded source, runtime unpacking, or hidden copies of other scripts.
# ============================================================

import os
import json
import time
import imp


# ============================================================
# PRODUCT AND FILES
# ============================================================

PRODUCT_NAME = "ChestLoot Pro"
VERSION = "1.0"
TAGLINE = "From lock to loot."

SETTINGS_FILE = "ChestLootPro_Settings.json"
KNOWLEDGE_FILE = "ChestLootPro_Knowledge.json"
LEGACY_SETTINGS_FILE = "ChestMasterPro_Settings.json"
LEGACY_KNOWLEDGE_FILE = "ChestMasterPro_Knowledge.json"
RETURN_TO_SELECTOR_KEY = "ChestLootPro_ReturnToModeSelection"


# ============================================================
# MODE REGISTRY
# ============================================================

MODE_DUNGEON = 0
MODE_KOTL = 1
MODE_SHOP = 2
MODE_EXODUS = 3

MODE_NAMES = {
    MODE_DUNGEON: "Dungeon Chest",
    MODE_SHOP: "Shop Chest",
    MODE_EXODUS: "Exodus Decorative Box",
}

MODE_ORDER = [MODE_DUNGEON, MODE_SHOP, MODE_EXODUS]

MODE_MODULE_FILES = {
    MODE_DUNGEON: "dungeon_mode.py",
    MODE_SHOP: "shop_mode.py",
    MODE_EXODUS: "exodus_mode.py",
}


# ============================================================
# SHARED UI CONSTANTS
# ============================================================

MODE_GUMP_ID = 0x45E0D130
GUMP_X = 50
GUMP_Y = 50

OUTER_ART = 9270
INNER_ART = 2620
ACTION_BUTTON_NORMAL = 4005
ACTION_BUTTON_PRESSED = 4007
MODE_BUTTON_NORMAL=2152
MODE_BUTTON_PRESSED=2151
RUNEBOOK_BUTTON_NORMAL=2103
RUNEBOOK_BUTTON_PRESSED=2104
CONFIG_BUTTON_NORMAL=2006
CONFIG_BUTTON_PRESSED=2007
MAIN_GUMP_ID=0x45E0D131
BTN_MODE_SELECTION=100
BTN_LOOT_MODE=101
BTN_OPTIONS=102
BTN_ACTION_BASE=110

HUE_TEXT = 1152
HUE_GOLD = 88
HUE_OPTION = 53
HUE_BLUE = 90
HUE_GREEN = 63
HUE_RED = 33
HUE_ORANGE = 44

FRAME_MARGIN = 16
INTER_PANEL_GAP = 8
SECTION_GAP = 16


# ============================================================
# SESSION STATE
# ============================================================

class ChestLootState:
    def __init__(self):
        self.running = True
        self.active_mode = MODE_DUNGEON
        self.screen = "mode_selection"
        self.busy = False
        self.loot_enabled = True

        # Detect Hidden Training remains temporary by design.
        self.detect_hidden_training_enabled = False
        self.detect_hidden_training_active = False

        self.settings = {}
        self.knowledge = {}


state = ChestLootState()


# ============================================================
# FILE AND MIGRATION HELPERS
# ============================================================

def script_dir():
    try:
        return os.path.dirname(__file__)
    except:
        return os.getcwd()


def local_path(filename):
    return os.path.join(script_dir(), filename)


def read_json(path, default_value):
    try:
        with open(path, "r") as source:
            value = json.load(source)
            return value if isinstance(value, dict) else default_value
    except:
        return default_value


def write_json(path, value):
    try:
        with open(path, "w") as destination:
            json.dump(value, destination, indent=2)
        return True
    except Exception as error:
        message("Your records could not be saved: " + str(error), HUE_RED)
        return False


def migrate_legacy_file(old_filename, new_filename):
    old_path = local_path(old_filename)
    new_path = local_path(new_filename)

    # Copy-only migration preserves the approved ChestMaster rollback files.
    if os.path.exists(new_path) or not os.path.exists(old_path):
        return

    legacy_value = read_json(old_path, None)
    if legacy_value is None:
        message("Your prior records could not be read.", HUE_RED)
        return

    write_json(new_path, legacy_value)


def migrate_chestmaster_records():
    migrate_legacy_file(LEGACY_SETTINGS_FILE, SETTINGS_FILE)
    migrate_legacy_file(LEGACY_KNOWLEDGE_FILE, KNOWLEDGE_FILE)


def load_records():
    state.settings = read_json(local_path(SETTINGS_FILE), {})
    state.knowledge = read_json(local_path(KNOWLEDGE_FILE), {})

    saved_mode = state.settings.get("active_profile", MODE_DUNGEON)
    try:
        saved_mode = int(saved_mode)
    except:
        saved_mode = MODE_DUNGEON

    if saved_mode in MODE_ORDER:
        state.active_mode = saved_mode
    state.loot_enabled = bool(state.settings.get("loot_enabled", True))


def save_records():
    # A launched mode owns the shared settings and knowledge files while it is
    # running. Reload its newest settings before saving the controller-owned
    # active mode so a stale controller snapshot cannot undo option changes.
    settings_path = local_path(SETTINGS_FILE)
    latest_settings = read_json(settings_path, {})
    if not isinstance(latest_settings, dict):
        latest_settings = {}
    latest_settings["active_profile"] = int(state.active_mode)
    state.settings = latest_settings
    write_json(settings_path, state.settings)

    # The controller does not edit learned-item knowledge. Refresh its memory
    # without rewriting the file saved by the active mode.
    latest_knowledge = read_json(local_path(KNOWLEDGE_FILE), {})
    if isinstance(latest_knowledge, dict):
        state.knowledge = latest_knowledge


# ============================================================
# SHARED PLAYER FEEDBACK
# ============================================================

def message(text, hue=HUE_BLUE):
    try:
        Misc.SendMessage("[{}] {}".format(PRODUCT_NAME, str(text)), hue)
    except:
        pass


def close_gump(gump_id):
    try:
        Gumps.CloseGump(gump_id)
    except:
        pass


def add_chestloot_title(gd, x, y, width, height):
    """Draw the approved Chest [white ornament] Loot Pro suite title."""
    title_width = 126
    # Two-pixel optical correction applied wherever the tool title appears.
    start_x = x + int((width - title_width) / 2) + 2

    Gumps.AddHtml(
        gd, start_x, y, 52, height,
        "<basefont color=#FFFF00><big>Chest</big></basefont>",
        False, False
    )
    Gumps.AddImage(gd, start_x + 40, y + 3, 2103, 2498)
    Gumps.AddHtml(
        gd, start_x + 55, y, 42, height,
        "<basefont color=#FFFF00><big>Loot</big></basefont>",
        False, False
    )
    Gumps.AddHtml(
        gd, start_x + 90, y, 36, height,
        "<basefont color=#FFFFFF><big>Pro</big></basefont>",
        False, False
    )


# ============================================================
# MODE SELECTION
# ============================================================

def draw_mode_selection():
    close_gump(MODE_GUMP_ID)

    # Validated Mode Selection v0.1.2 geometry.
    # Fit the full Exodus label with clear space inside the right panel edge.
    width = 244
    height = 227

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    transparent_ui = imp.load_source("chestloot_transparent_ui", os.path.join(script_dir(), "chestloot_modes", "transparent_ui.py"))
    transparent_ui.add_background(Gumps, gd, width, height, OUTER_ART,
                                  [(16, 32, width - 32, 179, INNER_ART)],
                                  transparent_ui.enabled(local_path(SETTINGS_FILE), Player.Serial))

    add_chestloot_title(gd, 10, 10, width - 20, 26)

    Gumps.AddHtml(
        gd, 30, 51, width - 60, 20,
        "<basefont color=#FFFF00>Select Mode</basefont>",
        False, False
    )
    Gumps.AddHtml(
        gd, 32, 71, width - 64, 22,
        "<basefont color=#0080FF>" + ("-" * max(50, width - 64)) + "</basefont>",
        False, False
    )

    # Preserve the visually approved v0.1.2 order and 36-pixel row rhythm.
    rows = [
        (MODE_DUNGEON + 1, 91, MODE_NAMES[MODE_DUNGEON]),
        (MODE_SHOP + 1, 127, MODE_NAMES[MODE_SHOP]),
        (MODE_EXODUS + 1, 163, MODE_NAMES[MODE_EXODUS]),
    ]

    for button_id, y, label in rows:
        Gumps.AddButton(
            gd, 26, y,
            MODE_BUTTON_NORMAL, MODE_BUTTON_PRESSED,
            button_id, 1, 0
        )
        Gumps.AddLabel(gd, 60, y + 4, HUE_BLUE, label)

    Gumps.SendGump(
        MODE_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y,
        gd.gumpDefinition, gd.gumpStrings
    )

def handle_mode_selection():
    if not Gumps.WaitForGump(MODE_GUMP_ID, 100):
        return

    try:
        button_id = int(Gumps.GetGumpData(MODE_GUMP_ID).buttonid)
    except:
        button_id = 0

    if button_id == 0:
        state.running = False
        return

    selected_mode = button_id - 1
    if selected_mode not in MODE_ORDER:
        draw_mode_selection()
        return

    state.active_mode = selected_mode
    save_records()

    if launch_approved_mode(selected_mode):
        state.screen = "mode_selection"
        draw_mode_selection()
    else:
        state.running = False


def launch_approved_mode(mode_id):
    """Run one approved standalone mode and report whether it requested Back."""
    if mode_id not in MODE_ORDER:
        return False
    filename = MODE_MODULE_FILES.get(mode_id)
    if not filename:
        return False

    root = script_dir()
    module_path = os.path.join(root, "chestloot_modes", filename)
    if not os.path.exists(module_path):
        message("ChestLoot Pro could not find {}.".format(filename), HUE_RED)
        return True

    try:
        Misc.SetSharedValue(RETURN_TO_SELECTOR_KEY, 0)
    except:
        pass

    module_name = "chestloot_mode_{}_{}".format(mode_id, int(time.time() * 1000))
    module = imp.load_source(module_name, module_path)

    # Razor Enhanced provides these names to the controller. Standalone mode
    # modules receive the same API objects explicitly before their run begins.
    for api_name in [
        "Misc", "Gumps", "Player", "Items", "Target", "Journal",
        "Spells", "Mobiles", "Statics", "PathFinding"
    ]:
        if api_name in globals():
            setattr(module, api_name, globals()[api_name])

    # All three release modes share the controller folder for settings and migration.
    module.script_dir = script_dir
    module.run_mode()

    try:
        return int(Misc.ReadSharedValue(RETURN_TO_SELECTOR_KEY)) == 1
    except:
        return False


# ============================================================
# MAIN LOOP
# ============================================================

def run():
    migrate_chestmaster_records()
    load_records()
    message("{} v{} loaded.".format(PRODUCT_NAME, VERSION), HUE_GREEN)
    draw_mode_selection()

    while state.running:
        if state.screen == "mode_selection":
            handle_mode_selection()
        Misc.Pause(50)

    save_records()
    close_gump(MODE_GUMP_ID)
    message("{} closed.".format(PRODUCT_NAME), HUE_OPTION)


run()
