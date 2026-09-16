# ============================================================
# ChestLoot Pro - Exodus Decorative Box Standalone v0.3.25
# Razor Enhanced Python / UOAlive
#
# Approved Detect Hidden Training build based on the fully tested v0.3.20.
# Persists durable options in ChestLootPro_Settings.json.
# Migrates existing standalone Shared Values without losing them.
# Applies the 16-pixel section and final-panel clearance standard.
# Final Exodus training build. It validates required loot bags before every
# Scan Area workflow, uses standard message colors, and preserves an unresolved
# pointer across travel.
# ============================================================

import os
import json
import time
import imp


# ============================================================
# UI AND CONFIGURATION
# ============================================================

MAIN_GUMP_ID = 0x45E0D106
OPTIONS_GUMP_ID = 0x45E0D107
GUMP_X = 80
GUMP_Y = 80

OUTER_ART = 9270
INNER_ART = 2620
ACTION_BUTTON_NORMAL = 4005
ACTION_BUTTON_PRESSED = 4007
ROW_ARROW_ART = 5837  # Confirmed PetMedic row button; label at x+34, y-1.
LEFT_ARROW_NORMAL = 4014
LEFT_ARROW_PRESSED = 4016
CONFIG_BUTTON_NORMAL = 2006
CONFIG_BUTTON_PRESSED = 2007
RUNEBOOK_BUTTON_NORMAL = 2103
RUNEBOOK_BUTTON_PRESSED = 2104
MODE_BUTTON_NORMAL = 2152
MODE_BUTTON_PRESSED = 2151
CHECK_OFF = 210
CHECK_ON = 211

HUE_TEXT = 1152
HUE_GOLD = 88
HUE_BLUE = 90
HUE_GREEN = 63
HUE_RED = 33
HUE_ORANGE = 44
HUE_JOURNAL_OPTION = 53
HUE_INFO = HUE_JOURNAL_OPTION
HUE_BOX_MARK = 0x0481

BTN_CLOSE = 0
BTN_OPTIONS = 1
BTN_SCAN_AREA = 2
BTN_TARGET_BOX = 3
BTN_LOOT_MODE = 4
BTN_MODE_SELECTION = 5
BTN_STOP_TRAINING = 6
BTN_BACK = 10
BTN_VALUABLES_BAG = 11
BTN_KEYS_BAG = 12
BTN_DETECT_HIDDEN_TRAINING = 13
BTN_TRANSPARENT_GUMPS = 14
BTN_LOOT_BASE = 100

SETTINGS_PREFIX = "ChestMaster_Exodus_Standalone_"
SETTINGS_FILE = "ChestLootPro_Settings.json"

KEEN_SENSES_MESSAGE = "Your keen senses detect something hidden in the area..."
DECORATIVE_BOX_NAME = "decorative box"
DETECT_HIDDEN_SKILL = "Detect Hidden"
REMOVE_TRAP_SKILL = "Remove Trap"
LOCKPICK_ID = 0x14FC

SCAN_INTERVAL_MS = 10500
SHARED_SKILL_COOLDOWN_MS = 10000
SHARED_SKILL_SAFETY_BUFFER_MS = 250
TARGET_CURSOR_TIMEOUT_MS = 2500
SCAN_RESULT_WINDOW_MS = 3000
SCAN_TIMEOUT_MS = 180000
BOX_SEARCH_RANGE = 12
BOX_MARK_RADIUS = 7
MAX_COMPLETED_BOXES = 10

MAX_LOCKPICK_ATTEMPTS = 10
MAX_TRAP_ATTEMPTS = 5
MAX_OPEN_ATTEMPTS = 4
LOCKPICK_RESULT_TIMEOUT_MS = 3500
TRAP_RESULT_TIMEOUT_MS = 4000
OPEN_DELAY_MS = 1200
CONTENTS_WAIT_MS = 3000
POST_OPEN_LOOT_DELAY_MS = 500
ACTION_DELAY_MS = 700
MOVE_DELAY_MS = 900
ACTION_WAIT_DELAY_MS = 1250
MOVE_TIMEOUT_MS = 3000
MOVE_RETRY_DELAY_MS = 600
MAIN_LOOP_DELAY_MS = 100
MAX_WEIGHT_BUFFER = 10
MAX_LOOT_PASSES = 3
SECTION_GAP = 15

DEBUG_MODE = False

PICK_SUCCESS_MESSAGES = [
    "The lock quickly yields to your skill",
    "You manage to pick the lock",
    "You successfully pick the lock",
    "This does not appear to be locked",
    "That is not locked",
]
PICK_FAIL_MESSAGES = ["You fail to pick the lock", "You are unable to pick the lock"]
LOCKED_MESSAGES = [
    "It appears to be locked",
    "That appears to be locked",
    "This appears to be locked",
]
TRAP_SUCCESS_MESSAGES = [
    "You successfully render the trap harmless",
    "That doesn't appear to be trapped",
]
TRAP_FAIL_MESSAGES = ["You fail to disarm the trap"]
ACTION_WAIT_MESSAGES = ["You must wait to perform another action", "You must wait"]
HARD_STOP_MESSAGES = [
    "That is too far away",
    "You can't reach that",
    "You do not see that",
    "Target cannot be seen",
    "Cannot see",
]

GEM_IDS = set([
    0x0F0F, 0x0F10, 0x0F11, 0x0F13, 0x0F15,
    0x0F16, 0x0F18, 0x0F25, 0x0F26,
])
GOLD_ID = 0x0EED
ESSENCE_ID = 0x571C
POTION_ID = 0x0F0A
SMOKE_BOMB_ID = 0x2808
INGREDIENT_IDS = set([0x3183, 0x3184, 0x3187, 0x3191])
KEY_IDS = {
    0x2D2D: "Sacrificial Dagger",
    0x14F0: "Summoning Altar",
    0x2258: "Summoning Rite",
    0x1F03: "Robe of Rite",
}

# Display order is alphabetical inside each logical group.
LOOT_OPTIONS = [
    ("Essences", "valuables"),
    ("Gems", "valuables"),
    ("Gold", "valuables"),
    ("Ingredients", "valuables"),
    ("Potions", "valuables"),
    ("Smoke Bombs", "valuables"),
    ("Robe of Rite", "keys"),
    ("Sacrificial Dagger", "keys"),
    ("Summoning Altar", "keys"),
    ("Summoning Rite", "keys"),
]

# Looting priority is intentionally separate from the alphabetical Options
# display. Stable sorting preserves the chest's original order within each
# category while moving the most useful Exodus materials first.
EXODUS_LOOT_PRIORITY = {
    "Ingredients": 0,
    "Essences": 1,
    "Gold": 2,
    "Potions": 3,
    "Robe of Rite": 4,
    "Sacrificial Dagger": 5,
    "Summoning Altar": 6,
    "Summoning Rite": 7,
    "Smoke Bombs": 8,
    "Gems": 9,
}


# ============================================================
# STATE AND SETTINGS
# ============================================================

class ExodusState:
    def __init__(self):
        self.mark_x = None
        self.mark_y = None
        self.mark_z = None
        self.mark_map = None
        self.location_arrow_active = False
        self.scan_x = None
        self.scan_y = None
        self.scan_z = None
        self.scan_map = None
        self.box_serial = 0
        self.discovered_boxes = set()
        self.scan_baseline = set()
        self.completed_boxes = set()
        self.completed_box_order = []
        self.scanning = False
        self.processing_box = False
        self.scan_started_ms = 0
        self.next_scan_ms = 0
        self.scan_attempts = 0
        self.last_detect_hidden_ms = 0
        # Training is deliberately session-only and always starts disabled.
        self.detect_hidden_training_enabled = False
        self.training_active = False
        self.training_cancel_requested = False
        self.training_stop_message_sent = False
        self.status_text = "Ready"
        self.status_hue = HUE_GREEN
        self.paused = False
        self.pause_message_sent = False
        self.last_journal_entry = None
        self.valuables_bag = 0
        self.keys_bag = 0
        self.loot_master_enabled = True
        self.loot_enabled = dict((name, True) for name, route in LOOT_OPTIONS)
        self.running = True


state = ExodusState()


def now_ms():
    return int(time.time() * 1000)


def shared_key(name):
    return SETTINGS_PREFIX + name


def load_shared_int(name, default_value=0):
    try:
        if Misc.CheckSharedValue(shared_key(name)):
            return int(Misc.ReadSharedValue(shared_key(name)))
    except:
        pass
    return default_value


def load_shared_bool(name, default_value=True):
    return load_shared_int(name, 1 if default_value else 0) != 0


def save_shared(name, value):
    try:
        Misc.SetSharedValue(shared_key(name), value)
    except:
        pass


def script_dir():
    try:
        return os.path.dirname(__file__)
    except:
        return os.getcwd()


def settings_path():
    return os.path.join(script_dir(), SETTINGS_FILE)


transparent_ui = imp.load_source("chestloot_transparent_ui", os.path.join(script_dir(), "transparent_ui.py"))


def add_release_background(gd, width, height, panels):
    transparent_ui.add_background(Gumps, gd, width, height, OUTER_ART, panels,
                                  transparent_ui.enabled(settings_path(), Player.Serial))


def read_settings_file():
    try:
        with open(settings_path(), "r") as settings_handle:
            data = json.load(settings_handle)
            return data if isinstance(data, dict) else {}
    except:
        return {}


def write_settings_file(data):
    try:
        with open(settings_path(), "w") as settings_handle:
            json.dump(data, settings_handle, indent=2)
        return True
    except Exception as ex:
        message("Your Exodus options could not be saved: " + str(ex), HUE_RED)
        return False


def load_settings():
    data = read_settings_file()
    saved_options = data.get("exodus_options", {}) or {}
    has_durable_settings = any(
        key in data for key in [
            "exodus_valuables_bag", "exodus_keys_bag",
            "exodus_options"
        ]
    )

    state.valuables_bag = int(data.get("exodus_valuables_bag", load_shared_int("ValuablesBag", 0)) or 0)
    state.keys_bag = int(data.get("exodus_keys_bag", load_shared_int("KeysBag", 0)) or 0)
    state.loot_master_enabled = bool(data.get("loot_enabled", load_shared_bool("LootEnabled", True)))
    for name, route in LOOT_OPTIONS:
        fallback = load_shared_bool("Loot_" + name.replace(" ", "_"), True)
        state.loot_enabled[name] = bool(saved_options.get(name, fallback))

    # First durable load migrates the prior standalone Shared Values.
    if not has_durable_settings:
        save_settings()
    refresh_setup_status(redraw=False)


def save_settings():
    # Continue mirroring Shared Values so an older standalone build can still
    # see the latest choices during the current Razor Enhanced session.
    save_shared("ValuablesBag", int(state.valuables_bag or 0))
    save_shared("KeysBag", int(state.keys_bag or 0))
    save_shared("LootEnabled", 1 if state.loot_master_enabled else 0)
    for name, route in LOOT_OPTIONS:
        save_shared("Loot_" + name.replace(" ", "_"), 1 if state.loot_enabled[name] else 0)

    data = read_settings_file()
    data["exodus_valuables_bag"] = int(state.valuables_bag or 0)
    data["exodus_keys_bag"] = int(state.keys_bag or 0)
    data["loot_enabled"] = bool(state.loot_master_enabled)
    data["exodus_options"] = dict((name, bool(state.loot_enabled[name])) for name, route in LOOT_OPTIONS)
    write_settings_file(data)


def save_loot_option(name):
    save_settings()


# ============================================================
# GENERAL HELPERS
# ============================================================

def message(text, hue=HUE_INFO):
    Misc.SendMessage("[ChestLoot Pro] " + str(text), hue)


def debug_log(text):
    if DEBUG_MODE:
        Misc.SendMessage("[Exodus Debug] " + str(text), HUE_BLUE)


def close_gump(gump_id):
    try:
        Gumps.CloseGump(gump_id)
    except:
        pass


def close_all_gumps():
    close_gump(MAIN_GUMP_ID)
    close_gump(OPTIONS_GUMP_ID)


def target_cursor_busy():
    try:
        return bool(Target.HasTarget())
    except:
        return False


def set_status(text, hue=HUE_TEXT, redraw=True):
    state.status_text = str(text)
    state.status_hue = hue
    if redraw:
        draw_main_gump()


def pause_for_other_action():
    state.paused = True
    set_status("Paused - Another Action", HUE_RED, redraw=False)
    if not state.pause_message_sent:
        state.pause_message_sent = True
        message("Your attention is drawn elsewhere. The decorative box will wait.", HUE_RED)
    draw_main_gump()


def resume_from_pause():
    state.paused = False
    state.pause_message_sent = False


def begin_detect_hidden_training():
    state.training_active = True
    state.training_cancel_requested = False
    state.training_stop_message_sent = False


def finish_detect_hidden_training():
    state.training_active = False
    state.training_cancel_requested = False
    state.training_stop_message_sent = False


def request_training_stop(announce=True):
    if not state.training_active:
        return
    state.training_cancel_requested = True
    if announce and not state.training_stop_message_sent:
        state.training_stop_message_sent = True
        message("You pause your Detect Hidden training.", HUE_JOURNAL_OPTION)


def stop_detect_hidden_training(announce=True):
    if not state.training_active:
        return
    request_training_stop(announce)
    stop_scanning()
    finish_detect_hidden_training()
    set_status("Ready", HUE_GREEN)


def poll_training_controls():
    """Keep Stop Training responsive during the scan result window."""
    if not state.training_active:
        return False
    try:
        if not Gumps.WaitForGump(MAIN_GUMP_ID, 1):
            return state.training_cancel_requested
        button_id = int(Gumps.GetGumpData(MAIN_GUMP_ID).buttonid)
    except:
        return state.training_cancel_requested
    if button_id == BTN_STOP_TRAINING:
        request_training_stop(True)
    elif button_id == BTN_CLOSE:
        state.running = False
        request_training_stop(False)
    else:
        # Operational buttons are unavailable until the active loop is stopped.
        draw_main_gump()
    return state.training_cancel_requested


def tracking_arrow_off():
    try:
        Player.TrackingArrow(0, 0, False)
    except:
        pass


def tracking_arrow_on(x, y):
    try:
        Player.TrackingArrow(int(x), int(y), True)
    except:
        pass


def current_map():
    try:
        return int(Player.Map)
    except:
        return -1


def valid_container(serial):
    if not serial:
        return False
    try:
        item = Items.FindBySerial(int(serial))
        return item is not None and bool(item.IsContainer)
    except:
        return False


def setup_problem():
    if not state.loot_master_enabled:
        return None
    valuables_ok = valid_container(state.valuables_bag)
    keys_ok = valid_container(state.keys_bag)
    if not valuables_ok and not keys_ok:
        return "Open Options to select loot bags"
    if not valuables_ok:
        return "Open Options: select Valuables Bag"
    if not keys_ok:
        return "Open Options: select Exodus Keys Bag"
    return None


def refresh_setup_status(redraw=True):
    problem = setup_problem()
    if problem:
        set_status(problem, HUE_RED, redraw=redraw)
        return False
    set_status("Ready", HUE_GREEN, redraw=redraw)
    return True


def require_setup():
    if refresh_setup_status(redraw=True):
        return True
    message("You must prepare your loot bags before searching the decorative boxes.", HUE_RED)
    return False


def select_bag(prompt, setting_name):
    if target_cursor_busy():
        set_status("Paused - Another Action", HUE_RED)
        return 0
    try:
        serial = int(Target.PromptTarget(""))
    except:
        serial = 0
    if serial <= 0:
        message("No container was selected.", HUE_RED)
        return 0
    if not valid_container(serial):
        message("That cannot be used as a loot container.", HUE_RED)
        return 0
    save_shared(setting_name, serial)
    bag_name = "Valuables Bag" if setting_name == "ValuablesBag" else "Exodus Keys Bag"
    message("Your {} has been recorded.".format(bag_name), HUE_JOURNAL_OPTION)
    return serial


def near_weight_limit():
    try:
        return int(Player.Weight) >= int(Player.MaxWeight) - MAX_WEIGHT_BUFFER
    except:
        return False


def item_container_serial(item):
    try:
        container = item.Container
        if hasattr(container, "Serial"):
            return int(container.Serial)
        return int(container)
    except:
        return 0


# ============================================================
# JOURNAL AND LOCATION TRACKING
# ============================================================

def initialize_journal_cursor():
    try:
        entries = list(Journal.GetJournalEntry(-1) or [])
        if entries:
            state.last_journal_entry = entries[-1]
    except:
        state.last_journal_entry = None


def new_journal_entries():
    try:
        if state.last_journal_entry is None:
            entries = list(Journal.GetJournalEntry(-1) or [])
        else:
            entries = list(Journal.GetJournalEntry(state.last_journal_entry) or [])
        if entries:
            state.last_journal_entry = entries[-1]
        return entries
    except:
        return []


def process_journal():
    for entry in new_journal_entries():
        try:
            text = str(entry.Text)
        except:
            continue
        if KEEN_SENSES_MESSAGE.lower() in text.lower():
            record_hidden_area()


def journal_has(messages):
    for journal_text in messages:
        try:
            if Journal.Search(journal_text):
                return True
        except:
            pass
    return False


def wait_for_journal(success_messages, fail_messages, timeout_ms):
    start = now_ms()
    while now_ms() - start < timeout_ms:
        if journal_has(success_messages):
            return "success"
        if journal_has(HARD_STOP_MESSAGES):
            return "hard"
        if journal_has(ACTION_WAIT_MESSAGES):
            return "wait"
        if journal_has(fail_messages):
            return "fail"
        Misc.Pause(100)
    return "timeout"


def record_hidden_area():
    try:
        state.mark_x = int(Player.Position.X)
        state.mark_y = int(Player.Position.Y)
        state.mark_z = int(Player.Position.Z)
        state.mark_map = current_map()
    except:
        message("The hidden location could not be marked.", HUE_RED)
        return
    # A Keen Eye clue updates the pointer, but it does not end an active
    # training loop. Detect Hidden Training follows the player's current
    # position and continues until stopped or a box is actually revealed.
    if not state.training_active:
        stop_scanning()
        state.scan_baseline = set()
    state.location_arrow_active = True
    tracking_arrow_on(state.mark_x, state.mark_y)
    draw_main_gump()


def clear_saved_location():
    state.mark_x = None
    state.mark_y = None
    state.mark_z = None
    state.mark_map = None
    state.location_arrow_active = False
    tracking_arrow_off()


def set_scan_center_from_saved_or_player():
    if state.mark_x is not None:
        state.scan_x = int(state.mark_x)
        state.scan_y = int(state.mark_y)
        state.scan_z = int(state.mark_z)
        state.scan_map = state.mark_map
    else:
        state.scan_x = int(Player.Position.X)
        state.scan_y = int(Player.Position.Y)
        state.scan_z = int(Player.Position.Z)
        state.scan_map = current_map()


def map_matches_scan_center():
    return state.scan_map is None or current_map() == state.scan_map


def distance_from_scan_center(item):
    try:
        return max(abs(int(item.Position.X) - state.scan_x), abs(int(item.Position.Y) - state.scan_y))
    except:
        return 999


def remember_completed_box(serial):
    serial = int(serial)
    if serial in state.completed_boxes:
        return
    state.completed_boxes.add(serial)
    state.completed_box_order.append(serial)
    while len(state.completed_box_order) > MAX_COMPLETED_BOXES:
        state.completed_boxes.discard(state.completed_box_order.pop(0))


# ============================================================
# BOX DISCOVERY
# ============================================================

def item_properties(item, wait_ms=500):
    try:
        Items.WaitForProps(item, wait_ms)
    except:
        pass
    try:
        return [str(x or "").strip().lower() for x in list(Items.GetPropStringList(item) or []) if str(x or "").strip()]
    except:
        return []


def item_name(item):
    try:
        name = str(item.Name or "").strip()
        if name:
            return name.lower()
    except:
        pass
    props = item_properties(item)
    return props[0] if props else ""


def box_shows_contents(item):
    return any("contents:" in line and "items" in line for line in item_properties(item))


def nearby_decorative_boxes(exclude_opened=False):
    found = []
    try:
        item_filter = Items.Filter()
        item_filter.Enabled = True
        item_filter.OnGround = 1
        item_filter.RangeMax = BOX_SEARCH_RANGE
        item_filter.CheckIgnoreObject = False
        candidates = list(Items.ApplyFilter(item_filter) or [])
    except:
        candidates = []
    for item in candidates:
        try:
            if DECORATIVE_BOX_NAME not in item_name(item):
                continue
            if int(item.Serial) in state.completed_boxes:
                continue
            if exclude_opened and box_shows_contents(item):
                continue
            if state.scan_x is not None and distance_from_scan_center(item) > BOX_MARK_RADIUS:
                continue
            found.append(item)
        except:
            pass
    return found


def choose_nearest_box(boxes):
    if not boxes:
        return None
    boxes = list(boxes)
    boxes.sort(key=distance_from_scan_center)
    return boxes[0]


def distance_from_player(item):
    try:
        return max(
            abs(int(item.Position.X) - int(Player.Position.X)),
            abs(int(item.Position.Y) - int(Player.Position.Y))
        )
    except:
        return 999


def choose_nearest_box_to_player(boxes):
    if not boxes:
        return None
    boxes = list(boxes)
    boxes.sort(key=distance_from_player)
    return boxes[0]


def apply_box_highlight(item, announce_new=False):
    revealed_during_training = bool(state.training_active)
    stop_scanning()
    if revealed_during_training:
        finish_detect_hidden_training()
    state.box_serial = int(item.Serial)
    # The hidden-location pointer represents an unresolved case location.
    # Clear it only after a visible decorative box has actually been found.
    clear_saved_location()
    try:
        Items.SetColor(item.Serial, HUE_BOX_MARK)
        Items.Message(item.Serial, HUE_GOLD, "Exodus Decorative Box")
    except:
        pass
    if announce_new and state.box_serial not in state.discovered_boxes:
        state.discovered_boxes.add(state.box_serial)
        if revealed_during_training:
            message(
                "An Exodus decorative box has been revealed. Detect Hidden training has stopped.",
                HUE_GREEN
            )
    set_status("Box Located", HUE_GREEN)


def refresh_existing_box():
    if not state.box_serial:
        return False
    box = Items.FindBySerial(state.box_serial)
    if box is None:
        state.box_serial = 0
        return False
    apply_box_highlight(box, announce_new=False)
    return True


def recover_single_visible_box():
    candidates = nearby_decorative_boxes(exclude_opened=True)
    if candidates:
        box = choose_nearest_box_to_player(candidates)
        apply_box_highlight(box, int(box.Serial) not in state.discovered_boxes)
        if len(candidates) > 1:
            message("More than one decorative box lies nearby. The closest has been marked.", HUE_BLUE)
        return "adopted"
    return "none"


def begin_scan():
    # When looting is enabled, every Scan Area workflow begins with the same
    # bag validation. Loot Disabled remains the intentional exception because
    # the script will leave the revealed contents for the player.
    if not require_setup():
        return
    if state.processing_box:
        message("The current box is already being examined.", HUE_RED)
        return
    resume_from_pause()
    if refresh_existing_box():
        return
    set_scan_center_from_saved_or_player()
    if not map_matches_scan_center():
        set_status("Wrong Facet", HUE_RED)
        return
    if recover_single_visible_box() != "none":
        return
    state.scan_baseline = set(int(x.Serial) for x in nearby_decorative_boxes())
    state.scanning = True
    state.scan_started_ms = now_ms()
    state.next_scan_ms = 0
    state.scan_attempts = 0
    if state.detect_hidden_training_enabled:
        begin_detect_hidden_training()
        message(
            "Detect Hidden training has begun. Your search will continue until a box is revealed or training is stopped.",
            HUE_BLUE
        )
    set_status("Scanning for decorative boxes...", HUE_BLUE)


def stop_scanning():
    state.scanning = False
    state.scan_started_ms = 0
    state.next_scan_ms = 0


def detect_new_box():
    new_boxes = [x for x in nearby_decorative_boxes() if int(x.Serial) not in state.scan_baseline]
    return choose_nearest_box(new_boxes)


def perform_detect_hidden():
    if not state.scanning:
        return
    if state.training_cancel_requested:
        stop_detect_hidden_training(announce=False)
        return
    if not map_matches_scan_center():
        stop_scanning()
        if state.training_active:
            finish_detect_hidden_training()
            message("Detect Hidden training has stopped as you leave the dungeon.", HUE_JOURNAL_OPTION)
            set_status("Ready", HUE_GREEN)
        else:
            set_status("No decorative boxes found", HUE_RED)
            message("Nothing was revealed. Reposition and scan again.", HUE_RED)
        return
    if not state.detect_hidden_training_enabled and now_ms() - state.scan_started_ms >= SCAN_TIMEOUT_MS:
        stop_scanning()
        set_status("No decorative boxes found", HUE_RED)
        message("Nothing was revealed. Reposition and scan again.", HUE_RED)
        return
    new_box = detect_new_box()
    if new_box is not None:
        apply_box_highlight(new_box, True)
        return
    if now_ms() < state.next_scan_ms:
        return
    if target_cursor_busy():
        if state.detect_hidden_training_enabled:
            # Respect an unrelated target cursor and retry shortly without
            # ending the training session or overwriting the player's action.
            state.next_scan_ms = now_ms() + 500
            return
        stop_scanning()
        pause_for_other_action()
        return
    state.scan_attempts += 1
    try:
        if state.detect_hidden_training_enabled:
            # Training follows the player. A Keen Eye pointer remains an
            # independent remembered destination and never limits skill use.
            state.scan_x = int(Player.Position.X)
            state.scan_y = int(Player.Position.Y)
            state.scan_z = int(Player.Position.Z)
        Player.UseSkill(DETECT_HIDDEN_SKILL)
        if not Target.WaitForTarget(TARGET_CURSOR_TIMEOUT_MS, False):
            state.next_scan_ms = now_ms() + SCAN_INTERVAL_MS
            return
        Target.TargetExecute(state.scan_x, state.scan_y, state.scan_z, 0)
        state.last_detect_hidden_ms = now_ms()
        if state.detect_hidden_training_enabled:
            state.next_scan_ms = (
                state.last_detect_hidden_ms
                + SHARED_SKILL_COOLDOWN_MS
                + SHARED_SKILL_SAFETY_BUFFER_MS
            )
    except:
        state.next_scan_ms = now_ms() + SCAN_INTERVAL_MS
        return
    started = now_ms()
    while now_ms() - started < SCAN_RESULT_WINDOW_MS:
        if state.detect_hidden_training_enabled and poll_training_controls():
            stop_detect_hidden_training(announce=False)
            return
        new_box = detect_new_box()
        if new_box is not None:
            apply_box_highlight(new_box, True)
            return
        process_journal()
        Misc.Pause(100)
    if not state.detect_hidden_training_enabled:
        stop_scanning()
        set_status("No decorative boxes found", HUE_RED)
        message("Nothing was revealed. Reposition and scan again.", HUE_RED)


# ============================================================
# TARGET, LOCKPICK, TRAP, AND OPEN
# ============================================================

def use_targeted(action, target):
    if target_cursor_busy():
        pause_for_other_action()
        return "yield"
    try:
        action()
        if not Target.WaitForTarget(TARGET_CURSOR_TIMEOUT_MS, False):
            return "failed"
        Target.TargetExecute(target)
        return "success"
    except:
        return "failed"


def prompt_for_visible_box():
    if target_cursor_busy():
        pause_for_other_action()
        return None
    try:
        serial = int(Target.PromptTarget(""))
        item = Items.FindBySerial(serial)
    except:
        item = None
    if item is None or DECORATIVE_BOX_NAME not in item_name(item):
        message("That is not a visible Decorative Box.", HUE_RED)
        return None
    try:
        if int(item.Container) != 0:
            message("Target a Decorative Box on the ground.", HUE_RED)
            return None
    except:
        pass
    return item


def resolve_target_box():
    if state.box_serial:
        box = Items.FindBySerial(state.box_serial)
        if box is not None:
            return box
        state.box_serial = 0
    return prompt_for_visible_box()


def get_lockpick():
    try:
        return Items.FindByID(LOCKPICK_ID, -1, Player.Backpack.Serial)
    except:
        return None


def box_out_of_range_message():
    message("The decorative box is beyond your reach. Move closer and try again.", HUE_RED)


def pick_lock(box):
    set_status("Picking the lock...", HUE_BLUE)
    for attempt in range(MAX_LOCKPICK_ATTEMPTS):
        lockpick = get_lockpick()
        if lockpick is None:
            set_status("No lockpicks remaining", HUE_RED)
            message("You have no lockpicks remaining.", HUE_RED)
            return False
        try:
            Journal.Clear()
        except:
            pass
        result = use_targeted(lambda: Items.UseItem(lockpick), box)
        if result == "yield":
            return "yield"
        if result != "success":
            Misc.Pause(ACTION_DELAY_MS)
            continue
        result = wait_for_journal(PICK_SUCCESS_MESSAGES, PICK_FAIL_MESSAGES, LOCKPICK_RESULT_TIMEOUT_MS)
        if result == "success":
            return "success"
        if result == "hard":
            set_status("Move closer to the box", HUE_RED)
            box_out_of_range_message()
            return False
        Misc.Pause(ACTION_WAIT_DELAY_MS if result == "wait" else ACTION_DELAY_MS)
    set_status("The lock refuses to yield", HUE_RED)
    message("The lock refuses to yield.", HUE_RED)
    return False


def wait_for_detect_hidden_cooldown():
    if not state.last_detect_hidden_ms:
        return
    ready_at = state.last_detect_hidden_ms + SHARED_SKILL_COOLDOWN_MS + SHARED_SKILL_SAFETY_BUFFER_MS
    remaining = ready_at - now_ms()
    if remaining <= 0:
        return
    set_status("Waiting - Remove Trap", HUE_BLUE)
    message(
        "You steady your hands, waiting {:.1f} seconds before examining the trap.".format(remaining / 1000.0),
        HUE_BLUE
    )
    if remaining > 0:
        Misc.Pause(remaining)


def remove_trap(box):
    wait_for_detect_hidden_cooldown()
    set_status("Disarming the trap...", HUE_BLUE)
    for attempt in range(MAX_TRAP_ATTEMPTS):
        try:
            Journal.Clear()
        except:
            pass
        result = use_targeted(lambda: Player.UseSkill(REMOVE_TRAP_SKILL), box)
        if result == "yield":
            return "yield"
        if result != "success":
            Misc.Pause(ACTION_WAIT_DELAY_MS)
            continue
        result = wait_for_journal(TRAP_SUCCESS_MESSAGES, TRAP_FAIL_MESSAGES, TRAP_RESULT_TIMEOUT_MS)
        if result == "success":
            return "success"
        if result == "hard":
            set_status("Move closer to the box", HUE_RED)
            box_out_of_range_message()
            return False
        if result == "wait":
            set_status("Waiting - Remove Trap", HUE_BLUE)
            Misc.Pause(SCAN_INTERVAL_MS)
            continue
        if result == "fail":
            if attempt + 1 >= MAX_TRAP_ATTEMPTS:
                break
            message("The trap resists your efforts. You prepare to examine it again.", HUE_BLUE)
            Misc.Pause(SCAN_INTERVAL_MS)
            continue
        Misc.Pause(ACTION_WAIT_DELAY_MS)
    set_status("The trap remains armed", HUE_RED)
    message("The decorative box remains trapped.", HUE_RED)
    return False


def open_box(box):
    set_status("Opening the box...", HUE_BLUE)
    for attempt in range(MAX_OPEN_ATTEMPTS):
        try:
            Journal.Clear()
            # WaitForContents is the single authoritative open request. Using
            # Items.UseItem plus a fixed pause before this call made Exodus
            # wait twice for the same operation.
            Items.WaitForContents(box.Serial, CONTENTS_WAIT_MS)
        except:
            pass
        if journal_has(LOCKED_MESSAGES):
            return "locked"
        if journal_has(HARD_STOP_MESSAGES):
            return "hard"
        if journal_has(ACTION_WAIT_MESSAGES):
            Misc.Pause(ACTION_WAIT_DELAY_MS)
            continue
        try:
            refreshed = Items.FindBySerial(box.Serial)
            if refreshed is not None and refreshed.Contains is not None:
                return "open"
        except:
            pass
    return "failed"


def open_with_repick(box):
    for attempt in range(3):
        result = open_box(box)
        if result == "open":
            return "success"
        if result == "hard":
            set_status("Move closer to the box", HUE_RED)
            box_out_of_range_message()
            return False
        if result == "locked":
            Misc.Pause(ACTION_WAIT_DELAY_MS)
            result = pick_lock(box)
            if result != "success":
                return result
            Misc.Pause(ACTION_WAIT_DELAY_MS)
            continue
        break
    set_status("The box could not be opened", HUE_RED)
    message("The decorative box could not be opened.", HUE_RED)
    return False


# ============================================================
# LOOT ENGINE
# ============================================================

def classify_loot(item):
    try:
        item_id = int(item.ItemID)
    except:
        return None
    if item_id == ESSENCE_ID:
        return "Essences"
    if item_id in GEM_IDS:
        return "Gems"
    if item_id == GOLD_ID:
        return "Gold"
    if item_id in INGREDIENT_IDS:
        return "Ingredients"
    if item_id == POTION_ID:
        return "Potions"
    if item_id == SMOKE_BOMB_ID:
        return "Smoke Bombs"
    if item_id in KEY_IDS:
        return KEY_IDS[item_id]
    return None


def destination_for(category):
    for name, route in LOOT_OPTIONS:
        if name == category:
            return state.keys_bag if route == "keys" else state.valuables_bag
    return 0


def wait_for_move(item_serial, destination_serial):
    started = now_ms()
    while now_ms() - started < MOVE_TIMEOUT_MS:
        moved = Items.FindBySerial(item_serial)
        if moved is None:
            return True
        if item_container_serial(moved) == int(destination_serial):
            return True
        Misc.Pause(100)
    return False


def move_item_confirmed(item, destination_serial):
    for attempt in range(2):
        try:
            Items.Move(item, int(destination_serial), 0)
        except:
            pass
        if wait_for_move(int(item.Serial), destination_serial):
            return True
        Misc.Pause(MOVE_RETRY_DELAY_MS)
    return False


def stable_box_snapshot(box):
    previous_signature = None
    latest = []
    started = now_ms()
    while now_ms() - started < CONTENTS_WAIT_MS:
        try:
            refreshed = Items.FindBySerial(box.Serial)
            latest = list(refreshed.Contains or [])
            signature = tuple(sorted(int(item.Serial) for item in latest))
        except:
            latest = []
            signature = tuple()
        if signature == previous_signature:
            return latest
        previous_signature = signature
        Misc.Pause(100)
    return latest


def selected_loot_in_box(box):
    contents = stable_box_snapshot(box)
    selected = []
    for item in contents:
        category = classify_loot(item)
        if category is not None and state.loot_enabled.get(category, False):
            selected.append((item, category))
    selected.sort(key=lambda entry: EXODUS_LOOT_PRIORITY.get(entry[1], 999))
    return selected


def loot_box(box):
    if not refresh_setup_status(redraw=False):
        draw_main_gump()
        return False
    set_status("Searching for valuables...", HUE_BLUE)
    message("You begin searching the decorative box for valuable treasures.", HUE_BLUE)
    # Opening a container and moving an item share the shard action queue.
    # This short proven buffer prevents the first move from producing the
    # game's "You must wait" response.
    Misc.Pause(POST_OPEN_LOOT_DELAY_MS)
    for loot_pass in range(MAX_LOOT_PASSES):
        selected = selected_loot_in_box(box)
        if not selected:
            message("You gather the spoils you came for.", HUE_GREEN)
            return True
        for item, category in selected:
            if near_weight_limit():
                set_status("Your pack is nearly full", HUE_RED)
                message("Your pack is nearly full.", HUE_RED)
                return False
            if not valid_container(state.valuables_bag) or not valid_container(state.keys_bag):
                refresh_setup_status(redraw=True)
                return False
            destination = destination_for(category)
            if not move_item_confirmed(item, destination):
                set_status("An item could not be moved", HUE_RED)
                message("You cannot seem to take the item.", HUE_RED)
                return False
            Misc.Pause(MOVE_DELAY_MS)
    if selected_loot_in_box(box):
        set_status("An item could not be moved", HUE_RED)
        message("You cannot seem to take the item.", HUE_RED)
        return False
    message("You gather the spoils you came for.", HUE_GREEN)
    return True


def process_target_box():
    if state.processing_box or not require_setup():
        return
    resume_from_pause()
    box = resolve_target_box()
    if state.paused:
        return
    if box is None:
        refresh_setup_status()
        return
    state.box_serial = int(box.Serial)
    state.processing_box = True
    stop_scanning()
    clear_saved_location()
    completed = False
    try:
        result = pick_lock(box)
        if result != "success":
            return
        Misc.Pause(ACTION_DELAY_MS)
        result = remove_trap(box)
        if result != "success":
            return
        Misc.Pause(ACTION_DELAY_MS)
        result = open_with_repick(box)
        if result != "success":
            return
        if state.loot_master_enabled:
            if not loot_box(box):
                return
        else:
            message("You leave the contents of the decorative box for your own inspection.", HUE_JOURNAL_OPTION)
        remember_completed_box(box.Serial)
        state.box_serial = 0
        completed = True
        set_status("Complete", HUE_GREEN)
    finally:
        state.processing_box = False
        if not state.paused and not completed and state.status_hue != HUE_RED:
            refresh_setup_status(redraw=False)
        draw_main_gump()


# ============================================================
# GUMPS
# ============================================================

def add_button_label(gd, x, y, button_id, label, hue,
                     normal_art=ACTION_BUTTON_NORMAL,
                     pressed_art=ACTION_BUTTON_PRESSED,
                     label_offset=34):
    Gumps.AddButton(gd, x, y, normal_art, pressed_art, button_id, 1, 0)
    Gumps.AddLabel(gd, x + label_offset, y + 2, hue, label)


def add_config_button(gd, x, y, button_id, label, hue):
    add_button_label(gd, x, y, button_id, label, hue,
                     CONFIG_BUTTON_NORMAL, CONFIG_BUTTON_PRESSED, 26)


def add_mode_button(gd, x, y, button_id, label):
    # The diamond's right point and the label's vertical center share one axis.
    Gumps.AddButton(gd, x, y, MODE_BUTTON_NORMAL, MODE_BUTTON_PRESSED, button_id, 1, 0)
    Gumps.AddLabel(gd, x + 34, y + 4, HUE_BLUE, label)


def add_centered_title(gd, width, y, text):
    Gumps.AddLabel(gd, max(18, int((width - len(text) * 7) / 2)), y, HUE_GOLD, text)


def add_divider(gd, x, y, width):
    # Verified Divider Gallery option B1. HTML text renders reliably in
    # ClassicUO, unlike the previously tested tiled-art divider candidates.
    # Supply more hyphens than the box can display so the HTML box clips the
    # visible rule at its calculated right edge instead of ending early.
    Gumps.AddHtml(
        gd, x, y, width, 22,
        "<basefont color=#0080FF>" + ("-" * max(50, width)) + "</basefont>",
        False, False
    )


def add_yellow_label(gd, x, y, width, text):
    # Use an explicit HTML color because gump hue 88 renders blue in the
    # current ClassicUO client rather than the intended ChestMaster yellow.
    Gumps.AddHtml(gd, x, y, width, 20,
                  "<basefont color=#FFFF00>" + text + "</basefont>",
                  False, False)


def add_chestloot_title(gd, x, y, width, height):
    """Draw the approved Chest [white ornament] Loot Pro suite title."""
    title_width = 126
    # Two-pixel optical correction for the ornament and letter shapes.
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


def draw_main_gump():
    close_gump(MAIN_GUMP_ID)
    # MAIN GUMP LAYOUT — every visible element has independent coordinates.
    # Adjust X to move left/right and Y to move up/down.
    # Size the compact main gump to the shortened "Exodus Deco Box" label
    # while preserving the standard 16-pixel outer frame margins.
    width = 197
    frame_side_margin = 16
    frame_bottom_margin = 16
    outer_x, outer_y = 0, 0
    title_x, title_y, title_width, title_height = 10, 12, width - 20, 26
    top_panel_x, top_panel_y = frame_side_margin, 32
    top_panel_width, top_panel_height = width - (frame_side_margin * 2), 111
    training_button_visible = bool(state.training_active)
    bottom_panel_x, bottom_panel_y = frame_side_margin, 151
    bottom_panel_width = width - (frame_side_margin * 2)
    bottom_panel_height = 120 if training_button_visible else 84
    height = bottom_panel_y + bottom_panel_height + frame_bottom_margin

    mode_button_x, mode_button_y = 25, 44
    mode_label_x, mode_label_y = 59, 48
    loot_button_x, loot_button_y = 25, 79
    loot_label_x, loot_label_y = 59, 78
    options_button_x, options_button_y = int(width / 2) - 30, 106
    scan_button_x, scan_button_y = 26, 164
    scan_label_x, scan_label_y = 60, 166
    target_button_x, target_button_y = 26, 200
    target_label_x, target_label_y = 60, 202
    stop_button_x, stop_button_y = 26, 236
    stop_label_x, stop_label_y = 60, 238

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    add_release_background(gd, width, height, [
        (top_panel_x, top_panel_y, top_panel_width, top_panel_height, INNER_ART),
        (bottom_panel_x, bottom_panel_y, bottom_panel_width, bottom_panel_height, INNER_ART)])
    # Keep only the space required by the centered title and two function groups.
    add_chestloot_title(gd, title_x, title_y, title_width, title_height)
    # Gold borders are functional separators. Keep every button clear of the
    # decorative edges rather than using the border itself as padding.
    # Reserved now as a real control so integrated ChestMaster can route it
    # back to Mode Selection without redesigning this gump.
    Gumps.AddButton(gd, mode_button_x, mode_button_y, MODE_BUTTON_NORMAL,
                    MODE_BUTTON_PRESSED, BTN_MODE_SELECTION, 1, 0)
    Gumps.AddLabel(gd, mode_label_x, mode_label_y, HUE_BLUE, "Exodus Deco Box")
    loot_label = "Loot Enabled" if state.loot_master_enabled else "Loot Disabled"
    loot_hue = HUE_GREEN if state.loot_master_enabled else HUE_RED
    Gumps.AddButton(gd, loot_button_x, loot_button_y, ROW_ARROW_ART,
                    ROW_ARROW_ART, BTN_LOOT_MODE, 1, 0)
    Gumps.AddLabel(gd, loot_label_x, loot_label_y, loot_hue, loot_label)
    # The Small Round B artwork is the complete Options control. Center it
    # without a duplicate text label beside it.
    Gumps.AddButton(gd, options_button_x, options_button_y,
                    CONFIG_BUTTON_NORMAL, CONFIG_BUTTON_PRESSED,
                    BTN_OPTIONS, 1, 0)
    Gumps.AddButton(gd, scan_button_x, scan_button_y, ACTION_BUTTON_NORMAL,
                    ACTION_BUTTON_PRESSED, BTN_SCAN_AREA, 1, 0)
    Gumps.AddLabel(gd, scan_label_x, scan_label_y, HUE_BLUE, "Scan Area")
    Gumps.AddButton(gd, target_button_x, target_button_y, ACTION_BUTTON_NORMAL,
                    ACTION_BUTTON_PRESSED, BTN_TARGET_BOX, 1, 0)
    Gumps.AddLabel(gd, target_label_x, target_label_y, HUE_GREEN, "Target Box")
    if training_button_visible:
        Gumps.AddButton(gd, stop_button_x, stop_button_y, ACTION_BUTTON_NORMAL,
                        ACTION_BUTTON_PRESSED, BTN_STOP_TRAINING, 1, 0)
        Gumps.AddLabel(gd, stop_label_x, stop_label_y, HUE_RED, "Stop Training")
    Gumps.SendGump(MAIN_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)


def bag_status(serial):
    return ("Set", HUE_GREEN) if valid_container(serial) else ("Not Set", HUE_RED)


def draw_options_gump():
    close_gump(OPTIONS_GUMP_ID)
    # Two columns share one content panel; width fits the longest complete
    # Exodus Keys row and its required right-side clearance.
    width = 388
    frame_margin = 16
    content_panel_x, content_panel_y = frame_margin, 32
    content_panel_width, content_panel_height = width - (frame_margin * 2), 547
    back_panel_x, back_panel_y = frame_margin, 587
    back_panel_width, back_panel_height = width - (frame_margin * 2), 45
    height = back_panel_y + back_panel_height + frame_margin
    divider_x, divider_width = 32, content_panel_width - 32
    # A 15-pixel section clearance follows the prior 20-pixel label box.
    types_header_y = 128 + 20 + SECTION_GAP
    loot_row_y = [203 + 23 * index for index in range(6)]
    keys_row_y = [203 + 23 * index for index in range(4)]
    trap_header_y = loot_row_y[-1] + 20 + SECTION_GAP
    trap_label_y = trap_header_y + 37
    training_header_y = trap_label_y + 20 + SECTION_GAP
    training_label_y = training_header_y + 42
    transparency_header_y = training_label_y + 20 + SECTION_GAP
    transparency_label_y = transparency_header_y + 42
    back_button_x, back_button_y = 34, back_panel_y + 11
    back_label_x, back_label_y = 68, back_button_y + 2

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    add_release_background(gd, width, height, [
        (content_panel_x, content_panel_y, content_panel_width, content_panel_height, INNER_ART),
        (back_panel_x, back_panel_y, back_panel_width, back_panel_height, INNER_ART)])
    add_chestloot_title(gd, 10, 10, width - 20, 26)
    add_yellow_label(gd, 30, 62, width - 60, "Loot Bags")
    add_divider(gd, divider_x, 82, divider_width)
    # Valuables is always the first destination bag in ChestMaster Options.
    text, hue = bag_status(state.valuables_bag)
    Gumps.AddButton(gd, 34, 100, ROW_ARROW_ART, ROW_ARROW_ART,
                    BTN_VALUABLES_BAG, 1, 0)
    Gumps.AddLabel(gd, 68, 99, HUE_TEXT, "Valuables Bag:")
    Gumps.AddLabel(gd, 195, 99, hue, text)
    text, hue = bag_status(state.keys_bag)
    Gumps.AddButton(gd, 34, 129, ROW_ARROW_ART, ROW_ARROW_ART,
                    BTN_KEYS_BAG, 1, 0)
    Gumps.AddLabel(gd, 68, 128, HUE_TEXT, "Exodus Keys Bag:")
    Gumps.AddLabel(gd, 195, 128, hue, text)
    add_yellow_label(gd, 30, types_header_y, 148, "Loot Types")
    add_divider(gd, 32, types_header_y + 20, 146)
    add_yellow_label(gd, 190, types_header_y, 166, "Exodus Keys")
    add_divider(gd, 192, types_header_y + 20, 164)
    for index in range(6):
        name = LOOT_OPTIONS[index][0]
        check_art = CHECK_ON if state.loot_enabled[name] else CHECK_OFF
        row_y = loot_row_y[index]
        Gumps.AddButton(gd, 34, row_y - 2, check_art, check_art,
                        BTN_LOOT_BASE + index, 1, 0)
        label_hue = HUE_GREEN if state.loot_enabled[name] else HUE_RED
        Gumps.AddLabel(gd, 68, row_y, label_hue, name)
    for index in range(6, 10):
        name = LOOT_OPTIONS[index][0]
        check_art = CHECK_ON if state.loot_enabled[name] else CHECK_OFF
        row_y = keys_row_y[index - 6]
        Gumps.AddButton(gd, 194, row_y - 2, check_art, check_art,
                        BTN_LOOT_BASE + index, 1, 0)
        label_hue = HUE_GREEN if state.loot_enabled[name] else HUE_RED
        Gumps.AddLabel(gd, 228, row_y, label_hue, name)
    add_yellow_label(gd, 30, trap_header_y, width - 60, "Trap Removal Method")
    add_divider(gd, divider_x, trap_header_y + 20, divider_width)
    Gumps.AddLabel(gd, 34, trap_label_y, HUE_TEXT, "Remove Trap Required")
    add_yellow_label(gd, 30, training_header_y, width - 60, "Skill Training")
    add_divider(gd, divider_x, training_header_y + 20, divider_width)
    training_art = CHECK_ON if state.detect_hidden_training_enabled else CHECK_OFF
    Gumps.AddButton(gd, 34, training_label_y - 2,
                    training_art, training_art,
                    BTN_DETECT_HIDDEN_TRAINING, 1, 0)
    Gumps.AddLabel(
        gd, 68, training_label_y,
        HUE_GREEN if state.detect_hidden_training_enabled else HUE_RED,
        "Detect Hidden Training"
    )
    add_yellow_label(gd, 30, transparency_header_y, width - 60, "Transparency")
    add_divider(gd, divider_x, transparency_header_y + 20, divider_width)
    on = transparent_ui.enabled(settings_path(), Player.Serial)
    transparency_art = CHECK_ON if on else CHECK_OFF
    Gumps.AddButton(gd, 34, transparency_label_y - 2, transparency_art,
                    transparency_art, BTN_TRANSPARENT_GUMPS, 1, 0)
    Gumps.AddLabel(gd, 68, transparency_label_y,
                   HUE_GREEN if on else HUE_TEXT, "Transparent Gumps")
    Gumps.AddButton(gd, back_button_x, back_button_y, LEFT_ARROW_NORMAL,
                    LEFT_ARROW_PRESSED, BTN_BACK, 1, 0)
    Gumps.AddLabel(gd, back_label_x, back_label_y, HUE_GOLD, "Back")
    Gumps.SendGump(OPTIONS_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)


def run_options_gump():
    """Pause operational work and wait for genuine Options responses."""
    stop_scanning()
    while state.running:
        draw_options_gump()
        while state.running:
            try:
                if Gumps.WaitForGump(OPTIONS_GUMP_ID, 60000):
                    break
            except:
                pass
        if not state.running:
            return
        try:
            button_id = int(Gumps.GetGumpData(OPTIONS_GUMP_ID).buttonid)
        except:
            button_id = BTN_CLOSE
        if button_id in [BTN_CLOSE, BTN_BACK]:
            close_gump(OPTIONS_GUMP_ID)
            refresh_setup_status(redraw=False)
            draw_main_gump()
            return
        if button_id == BTN_VALUABLES_BAG:
            serial = select_bag("Select the Valuables Bag.", "ValuablesBag")
            if serial:
                state.valuables_bag = serial
                save_settings()
            continue
        if button_id == BTN_KEYS_BAG:
            serial = select_bag("Select the Exodus Keys Bag.", "KeysBag")
            if serial:
                state.keys_bag = serial
                save_settings()
            continue
        if button_id == BTN_DETECT_HIDDEN_TRAINING:
            state.detect_hidden_training_enabled = not state.detect_hidden_training_enabled
            status = "enabled" if state.detect_hidden_training_enabled else "disabled"
            message("Detect Hidden training is now {}.".format(status), HUE_JOURNAL_OPTION)
            continue
        if button_id == BTN_TRANSPARENT_GUMPS:
            try:
                on = transparent_ui.toggle(settings_path(), Player.Serial)
                message("Transparency is {}.".format("enabled" if on else "disabled"), HUE_JOURNAL_OPTION)
            except Exception as ex:
                message("Transparency could not be saved: " + str(ex), HUE_RED)
            continue
        if BTN_LOOT_BASE <= button_id < BTN_LOOT_BASE + len(LOOT_OPTIONS):
            index = button_id - BTN_LOOT_BASE
            name = LOOT_OPTIONS[index][0]
            state.loot_enabled[name] = not state.loot_enabled[name]
            save_loot_option(name)
            status = "enabled" if state.loot_enabled[name] else "disabled"
            message("{} looting is now {}.".format(name, status), HUE_JOURNAL_OPTION)


def handle_main_gump():
    try:
        if not Gumps.WaitForGump(MAIN_GUMP_ID, 50):
            return
        button_id = int(Gumps.GetGumpData(MAIN_GUMP_ID).buttonid)
    except:
        return
    if state.training_active and button_id not in [BTN_CLOSE, BTN_STOP_TRAINING]:
        # Keep the active loop deterministic. Stop Training remains available
        # before any other operational action is accepted.
        draw_main_gump()
        return
    if button_id == BTN_CLOSE:
        state.running = False
    elif button_id == BTN_OPTIONS:
        close_gump(MAIN_GUMP_ID)
        run_options_gump()
    elif button_id == BTN_LOOT_MODE:
        state.loot_master_enabled = not state.loot_master_enabled
        save_settings()
        status = "enabled" if state.loot_master_enabled else "disabled"
        message("Exodus looting is now {}.".format(status), HUE_JOURNAL_OPTION)
        refresh_setup_status(redraw=False)
        draw_main_gump()
    elif button_id == BTN_MODE_SELECTION:
        Misc.SetSharedValue("ChestLootPro_ReturnToModeSelection", 1)
        state.running = False
    elif button_id == BTN_SCAN_AREA:
        begin_scan()
    elif button_id == BTN_TARGET_BOX:
        process_target_box()
    elif button_id == BTN_STOP_TRAINING:
        stop_detect_hidden_training(True)


# ============================================================
# MAIN
# ============================================================

def main():
    load_settings()
    initialize_journal_cursor()
    draw_main_gump()
    last_arrow_refresh = 0
    while state.running:
        process_journal()
        if state.scanning:
            perform_detect_hidden()
        # Keep an unresolved Keen Eye pointer visible even while Detect Hidden
        # Training is active. Ordinary movement never clears the pointer.
        if state.location_arrow_active and state.mark_x is not None and now_ms() - last_arrow_refresh >= 4000:
            tracking_arrow_on(state.mark_x, state.mark_y)
            last_arrow_refresh = now_ms()
        handle_main_gump()
        Misc.Pause(MAIN_LOOP_DELAY_MS)
    stop_scanning()
    finish_detect_hidden_training()
    tracking_arrow_off()
    save_settings()
    close_all_gumps()



def run_mode():
    try:
        main()
    except Exception as error:
        stop_scanning()
        finish_detect_hidden_training()
        tracking_arrow_off()
        close_all_gumps()
        message("Stopped: " + str(error), HUE_RED)
