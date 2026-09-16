# ============================================================
# ChestLoot Pro - Dungeon Chest
# v0.4.17-dungeon-test
# - Separates Wands from the Minimum Magic Tier as an independent, default-enabled Loot Type.
# - Opens the chest target cursor without a redundant instructional journal message.
# - Applies the 16-pixel Options section and final-panel clearance standard.
# - Preserves the validated Dungeon main-gump action-panel geometry.
# - Applies yellow 53 to recorded-list and general-information journal messages.
# - Narrows the Dungeon Options gump while preserving standard inner margins.
# - Removes the redundant timer value from genuine Remove Trap failure feedback.
# - Separates gump gold 88 from journal option yellow 53.
# - Uses yellow 53 for every active Dungeon Options confirmation.
# - Gives the Trap Removal control a full 24-pixel clearance above the main-panel border.
# - Moves the complete footer panel downward while preserving the eight-pixel channel.
# - Enables every Dungeon loot category by default for new settings.
# - Reports successful collection only when at least one item was moved.
# - Uses the approved completion narration: You gather the spoils you came for.
# - Removes obsolete test-destination feedback from bag selection.
# - Produces one gold confirmation after a valid Options bag selection.
# - Adds Lockpicks as a configurable Dungeon loot type, enabled by default.
# - Uses a two-column alphabetical Loot Types layout.
# - Shortens the Dungeon Options gump for smaller displays.
# - Tracks the Remove Trap cooldown with a 500 ms safety buffer.
# - Distinguishes cooldown responses from genuine Remove Trap failures.
# - Retries up to five genuine Remove Trap failures before stopping safely.
# - Reports the Rare Dungeon Items count at mode entry and list opening.
# - Uses the Close Style 4017/4019 removal control beside the Remove label.
# - Places recorded item names before their removal action without categories.
# - Narrows the Dungeon main gump while preserving validated control positions.
# - Promoted the gameplay-validated Dungeon workflow to stable status.
# - Uses orange for a successfully retrieved recorded Rare.
# - Treats Magic Untrap as successful after a clean failure-monitoring window.
# - Never opens after an explicit spell failure; failed casts are retried.
# - Retries safely when the journal reports that another spell is already casting.
# - Exposes Magic Untrap confirmation and cast-conflict timing constants.
# - Applies the approved action/result/options/discovery journal color roles.
# - Separates Arrows and Bolts into independent alphabetical loot options.
# - Replaces the Dungeon completion narration with the approved wording.
# - Normalizes journal hues to the shared ChestMaster palette.
# - Identifies the exact loot bag after each recorded destination change.
# - Removes the Dungeon Ignore Item feature and all unknown-item classification.
# - Adds an experimental post-loot Daily Rare property scan.
# - Stabilizes fresh chest snapshots and verifies selected loot before completion.
# - Aligns every round Options control to the approved bag-row relationship.
# - Compacts the Recorded Items gump and standardizes its footer navigation.
# - Corrects false weight-limit warnings caused by double-counting stack weight.
# - Applies the approved compact Dungeon main and Options gump geometry.
# - Uses round runebook controls for bags, magic tier, recorded lists, and trap method.
# - Uses the left-arrow navigation art for Back and Previous.
# - Restores parent-gump navigation when a submenu is right-clicked.
# - Restores the standard ChestMaster frame treatment for Recorded Item lists.
# - Implements the approved Dungeon Chest Steps 1-9 test workflow.
# - Replaces the legacy integrated gumps with the approved compact suite layout.
# - Uses one authoritative implementation for every Dungeon gump.
# - Exposes every visible coordinate and art choice in DUNGEON_LAYOUT.
# - Uses WaitForContents as the authoritative open request and fresh snapshot.
# - Classifies each item once and moves recorded rares first.
# - Recognizes mundane equipment without an exhaustive property scan.
# - Confirms every item move and retries one shard-throttled move once.
# - Uses positive blue plus sound 580 after a recorded rare is secured.
# - Centralizes Dungeon gump layout values in the DL settings table.
# - Finalized six Shop Item categories.
# - Updated the Shop category selector to the approved compact single-column layout.
# - Standardized and visually centered main gump titles.
# - Applied final Dungeon and Shop main-button spacing.
# - Renamed legacy target/steal button constants.
# - Added fixed eight-entry pagination to recorded-item lists.
# - Preserved compatibility with legacy learned Shop Item categories.
# - Corrected Shop Options framing so Recorded Items remains inside the main gold box.
# - Restored the standard 18-pixel gap before the separate 50-pixel Back footer.
# Working Beta
# UOAlive / Razor Enhanced / ClassicUO
# ============================================================
# Purpose:
#   First integrated working version of ChestLoot Pro.
#   Combines the finalized profile gumps with Dungeon, Kotl, and Shop workflows.
#
# Release Notes - Working Beta 0.3.0
#   - UI-only refresh built from the stable v0.2.10 engine.
#   - Reduced persistent main-gump width while preserving vertical spacing.
#   - Reduced profile, options, list, and category-selection gump widths.
#   - Corrected all divider lengths for the narrower inner frames.
#   - Repositioned bag-status and list Remove labels to remain inside their frames.
#   - Finalized Shop Category Selection with two framed sections, extra Tools clearance,
#     gold Back wording, and the original cancel button ID.
#   - Preserved lockpicking, trap removal, loot timing, journal parsing, persistence,
#     button IDs, and Shop cooldown behavior from v0.2.10.
#
# Release Notes - Working Beta 0.2.8
#   - Shortened main action labels to Target Chest and Steal Item.
#   - Added Shop Chest cooldown and immersive journal flow.
#   - Shop mode now rescans after every successful theft.
#   - The next-opportunity message appears only when another eligible item remains.
#   - Standardized the exact shard cooldown journal message.
#   - Retained proven 900 ms Dungeon item-movement timing.
#   - Retained hue-only Kotl Artifact detection (0x0A1F).
#
# Release Notes - Working Beta 0.2.6
#   - Added Shop Item category-selection gump before targeting an item.
#   - Learned Shop Items now always store an explicit category.
#   - Relearning an item updates its category.
#
# Release Notes - Prototype 0.1.15
#   - Left-aligned every interactive button across all gumps.
#   - Replaced text dividers with full-width solid blue divider bars.
#   - Restored Dungeon Rare Items and Ignored Items list access.
#   - Restored the Dungeon minimum magic-tier setting.
#   - Added cycling buttons for magic tier and trap method.
#   - Added Shop Rare Items and Shop Items list access.
#   - Added UI-only remove-list gumps for testing list navigation.
#   - Shop Chest remains fixed to Remove Trap and shows no trap control.
#   - Script now always opens on the chest-type selection screen.
#   - Removed the unnecessary Back button from the startup selector.
#   - Added Gold to the Kotl Regal Case loot types.
#   - Retained mandatory Kotl Artifacts as informational text only.
#   - Renamed Trap Method sections to Trap Removal Method.
#   - Trap buttons now display only Magic Untrap or Remove Trap.
#   - Removed Open text from recorded-item buttons.
#   - Corrected full magic-tier names and label/value spacing.
#   - Simplified Loot Enabled/Disabled into one colored button label.
#   - Fixed divider width so bars respect each gump's inner margins.
#   - Balanced the selector spacing beneath Shop Chest.
#   - Removed the Shop Chest Special Rules section.
#   - Compacted all profile main gumps to minimize persistent screen space.
#   - Extended the startup selector divider by one dash on the right.
#   - Changed active chest-type labels on main gumps to blue.
#   - Removed excess space below Dungeon trap selection.
#   - Enlarged every Back-button footer frame to prevent overlap.
#   - Added safe vertical clearance above all Options Back-button footers.
#   - Normalized Options gump bottom margins to match the top border.
#   - Added the Shop Chest Steal Next Item action button.
#   - Historical integrated-build note: Shop used its then-current action order.
#   - Applied approved action hues: learning yellow, stealing red, targeting green.
#   - Replaced the Shop Other category with Potions.
#   - Expanded Shop categories to Food, Gems, Potions, Reagents, Refinements, Resources, and Tools.
#   - Replaced the Shop Rare Loot Bag selector with a Valuables Bag selector.
#   - Kept Shop categories in alphabetical order.
#   - Renamed Learn Rare to Learn Rare Item in Dungeon and Shop modes.
#   - Renamed the Dungeon Daily Rare Bag to Rare Item Bag.
#   - Removed Daily Rares from Dungeon Loot Types; learned rares are always looted.
#   - Added Rare Item Bag to Shop Chest Options.
#   - Dungeon and Shop Rare Item Bag selectors now edit one shared setting.
#   - Renamed Magic Bag to Magic Item Bag.
#   - Renamed Kotl Loot Bag to Kotl Item Bag.
#   - Renamed Shop Loot Bag to Shop Item Bag.
#   - Alphabetized all Dungeon, Kotl, and Shop Loot Types.
#   - Split Dungeon Blank Scrolls and Spell Scrolls into separate categories.
#   - Added configurable Dungeon Lockpicks and Shop Spell Scrolls.
#   - Standardized Kotl item names for Inoperative Automaton Head and Stasis Chamber Power Core.
#   - Removed Rare Items automatic-loot sections from Dungeon and Shop Options to restore compact layouts.
#   - Retained the Kotl Artifacts automatic-loot section because Kotl artifacts have no bag selector.
#   - Rebalanced Dungeon and Shop Options spacing after removing those informational sections.
#   - Removed Lockpicks from configurable Dungeon Loot Types; lockpicks are intended to be always looted.
#   - Reclaimed the removed Lockpicks row to move Dungeon Magic Items, Recorded Items, and Trap Removal sections upward.
#   - Slightly enlarged the Dungeon Options frame so Magic Untrap remains comfortably inside the gold border.
#   - Enlarged the Shop Options frame so the Shop Items row sits fully inside the gold border.
# ============================================================

MAIN_GUMP_ID = 885100
PROFILE_GUMP_ID = 885101
OPTIONS_GUMP_ID = 885102
LIST_GUMP_ID = 885103
SHOP_CATEGORY_GUMP_ID = 885104

GUMP_X = 50
GUMP_Y = 50

# ============================================================
# GUMP LAYOUT SETTINGS - DUNGEON TEST BUILD
# Every visible Dungeon button, label, frame, divider, and title can be
# repositioned here without changing workflow code. Button and label
# coordinates are deliberately independent.
# ============================================================
DL = {
    # MAIN GUMP - compact two-panel ChestMaster layout.
    "main_width": 204, "main_height": 251,
    "main_outer_x": 0, "main_outer_y": 0,
    "main_title_x": 10, "main_title_y": 10, "main_title_w": 184, "main_title_h": 26,
    "main_upper_x": 16, "main_upper_y": 32, "main_upper_w": 172, "main_upper_h": 111,
    "main_lower_x": 16, "main_lower_y": 151, "main_lower_w": 172, "main_lower_h": 84,
    "mode_button_x": 26, "mode_button_y": 45, "mode_label_x": 60, "mode_label_y": 49,
    "loot_button_x": 26, "loot_button_y": 80, "loot_label_x": 60, "loot_label_y": 79,
    "options_button_x": 70, "options_button_y": 107,
    "learn_button_x": 26, "learn_button_y": 164, "learn_label_x": 60, "learn_label_y": 166,
    "target_button_x": 26, "target_button_y": 200, "target_label_x": 60, "target_label_y": 202,

    # OPTIONS GUMP - yellow headers, full-width blue dividers, separate Back footer.
    "options_width": 356, "options_height": 753,
    "options_outer_x": 0, "options_outer_y": 0,
    "options_main_x": 16, "options_main_y": 32, "options_main_w": 324, "options_main_h": 652,
    "options_footer_x": 16, "options_footer_y": 692, "options_footer_w": 324, "options_footer_h": 45,
    "options_title_x": 21, "options_title_y": 27, "options_title_w": 314, "options_title_h": 22,
    "section_x": 30, "section_divider_x": 32, "section_divider_w": 292,
    "bags_header_y": 62, "types_header_y": 192, "magic_header_y": 382,
    "trap_header_y": 457, "recorded_header_y": 533,
    "bag_button_x": 34, "bag_label_x": 68, "bag_state_x": 185,
    "valuable_bag_y": 99, "magic_bag_y": 128, "rare_bag_y": 157,
    "toggle_button_x": 34, "toggle_label_x": 68,
    "toggle_right_button_x": 186, "toggle_right_label_x": 220,
    "loot_row_1_y": 232, "loot_row_2_y": 255, "loot_row_3_y": 278,
    "loot_row_4_y": 301, "loot_row_5_y": 324, "loot_row_6_y": 347,
    "tier_button_x": 34, "tier_button_y": 423, "tier_label_x": 68, "tier_label_y": 422,
    "trap_button_x": 34, "trap_button_y": 499, "trap_label_x": 68, "trap_label_y": 498,
    "rares_button_x": 34, "rares_button_y": 575, "rares_label_x": 68, "rares_label_y": 574,
    "back_button_x": 34, "back_button_y": 703, "back_label_x": 68, "back_label_y": 705,
    # RECORDED LIST GUMPS - standard ChestMaster panel with navigation footer.
    "list_width": 380, "list_height": 447,
    "list_main_x": 16, "list_main_y": 32, "list_main_w": 348, "list_main_h": 328,
    "list_footer_x": 16, "list_footer_y": 368, "list_footer_w": 348, "list_footer_h": 63,
    "list_title_y": 48,
    "list_empty_x": 34, "list_empty_y": 78,
    "list_row_label_x": 34, "list_row_label_y": 78,
    "list_row_button_x": 270, "list_row_button_y": 76,
    "list_remove_label_x": 304, "list_remove_label_y": 78, "list_row_spacing": 35,
    "list_page_x": 150, "list_page_y": 374,
    "list_back_button_x": 28, "list_back_button_y": 397, "list_back_label_x": 62, "list_back_label_y": 399,
    "list_prev_button_x": 160, "list_prev_button_y": 397, "list_prev_label_x": 194, "list_prev_label_y": 399,
    "list_next_button_x": 292, "list_next_button_y": 397, "list_next_label_x": 326, "list_next_label_y": 399,
}

PROFILE_DUNGEON = 0
PROFILE_KOTL = 1
PROFILE_SHOP = 2

PROFILE_NAMES = {
    PROFILE_DUNGEON: "Dungeon Chest",
    PROFILE_KOTL: "Kotl Regal Case",
    PROFILE_SHOP: "Shop Chest"
}

BTN_PROFILE_SELECT = 1
BTN_TOGGLE_LOOT = 2
BTN_OPEN_OPTIONS = 3
BTN_TARGET = 4
BTN_LEARN_RARE = 5
BTN_IGNORE_ITEM = 6
BTN_LEARN_SHOP_ITEM = 7
BTN_STEAL_ITEM = 8

BTN_PROFILE_DUNGEON = 20
BTN_PROFILE_KOTL = 21
BTN_PROFILE_SHOP = 22
BTN_PROFILE_BACK = 29

BTN_OPTIONS_BACK = 99
BTN_TRANSPARENT_GUMPS = 151
BTN_LIST_BACK = 98
BTN_LIST_REMOVE_BASE = 900
BTN_LIST_PREV = 890
BTN_LIST_NEXT = 891
LIST_ITEMS_PER_PAGE = 8

BTN_SHOP_CATEGORY_CANCEL = 400
BTN_SHOP_CATEGORY_CONSUMABLES = 401
BTN_SHOP_CATEGORY_DECORATIONS = 402
BTN_SHOP_CATEGORY_EQUIPMENT = 403
BTN_SHOP_CATEGORY_REFINEMENTS = 404
BTN_SHOP_CATEGORY_RESOURCES = 405
BTN_SHOP_CATEGORY_TOOLS = 406

BTN_DUNGEON_VAL_BAG = 100
BTN_DUNGEON_MAGIC_BAG = 101
BTN_DUNGEON_RARE_BAG = 102
BTN_DUNGEON_AMMO = 110
BTN_DUNGEON_BOLTS = 124
BTN_DUNGEON_WANDS = 125
BTN_DUNGEON_BLANK_SCROLLS = 111
BTN_DUNGEON_GEMS = 112
BTN_DUNGEON_GOLD = 113
BTN_DUNGEON_LOCKPICKS = 114
BTN_DUNGEON_MAGIC = 115
BTN_DUNGEON_POTIONS = 116
BTN_DUNGEON_REAGS = 117
BTN_DUNGEON_REFINEMENTS = 118
BTN_DUNGEON_SPELL_SCROLLS = 123
BTN_DUNGEON_MAGIC_TIER = 119
BTN_DUNGEON_TRAP_CYCLE = 120
BTN_DUNGEON_OPEN_RARES = 121
BTN_DUNGEON_OPEN_IGNORED = 122

BTN_KOTL_VAL_BAG = 200
BTN_KOTL_ITEM_BAG = 201
BTN_KOTL_GOLD = 209
BTN_KOTL_GEMS = 210
BTN_KOTL_BOOKS = 211
BTN_KOTL_CARDS = 212
BTN_KOTL_POWER_CORES = 213
BTN_KOTL_HEADS = 214
BTN_KOTL_TRAP_CYCLE = 220

BTN_SHOP_VAL_BAG = 300
BTN_SHOP_ITEM_BAG = 301
BTN_SHOP_RARE_BAG = 302
BTN_SHOP_FOOD = 310
BTN_SHOP_GEMS = 311
BTN_SHOP_POTIONS = 312
BTN_SHOP_REAGENTS = 313
BTN_SHOP_REFINEMENTS = 314
BTN_SHOP_RESOURCES = 315
BTN_SHOP_TOOLS = 316
BTN_SHOP_SPELL_SCROLLS = 317
BTN_SHOP_OPEN_RARES = 320
BTN_SHOP_OPEN_ITEMS = 321

OUTER_ART = 9270
INNER_ART = 2620
ACTION_BUTTON_NORMAL = 4005
ACTION_BUTTON_PRESSED = 4007
ROW_ARROW_ART = 5837  # Confirmed PetMedic row button; label at x+34, y-1.
LEFT_ARROW_NORMAL = 4014
LEFT_ARROW_PRESSED = 4016
CLOSE_BUTTON_NORMAL = 4017
CLOSE_BUTTON_PRESSED = 4019
MODE_BUTTON_NORMAL = 2152
MODE_BUTTON_PRESSED = 2151
RUNEBOOK_BUTTON_NORMAL = 2103
RUNEBOOK_BUTTON_PRESSED = 2104
SMALL_ROUND_NORMAL = 2116
SMALL_ROUND_PRESSED = 2115
CONFIG_BUTTON_NORMAL = 2006
CONFIG_BUTTON_PRESSED = 2007
CHECK_OFF = 210
CHECK_ON = 211
BLUE_LINE_ART = 2624

HUE_TEXT = 1152
HUE_ENABLED = 63
HUE_DISABLED = 33
HUE_GOLD = 88
HUE_JOURNAL_OPTION = 53
HUE_INFO = HUE_JOURNAL_OPTION
HUE_BLUE = 90
HUE_ORANGE = 44

TRAP_MAGIC = 0
TRAP_SKILL = 1
TRAP_NAMES = ["Magic Untrap", "Remove Trap"]

MAGIC_TIERS = [
    "Minor Magic",
    "Lesser Magic",
    "Greater Magic",
    "Major Magic",
    "Lesser Artifact",
    "Greater Artifact",
    "Major Artifact",
    "Legendary Artifact"
]

active_profile = PROFILE_DUNGEON
loot_enabled = True
current_screen = "profile"
gump_closed = False
active_list_name = None

# UI-only example records make the remove-list layout testable.
rare_items = ["Example Rare Treasure", "Example Decorative Relic"]
ignored_items = ["Example Discarded Item"]
shop_items = ["Example Shop Resource", "Example Shop Tool"]

dungeon_valuables_bag = None
dungeon_magic_bag = None
shared_rare_item_bag = None
kotl_valuables_bag = None
kotl_item_bag = None
shop_valuables_bag = None
shop_item_bag = None

dungeon_options = {
    "Arrows": True,
    "Blank Scrolls": True,
    "Bolts": True,
    "Gems": True,
    "Gold": True,
    "Lockpicks": True,
    "Magic Items": True,
    "Potions": True,
    "Reagents": True,
    "Refinements": True,
    "Spell Scrolls": True,
    "Wands": True
}
# Fresh installs begin at Lesser Magic so Dungeon Magic Items follow the
# release-wide default of looting every supported category.
dungeon_magic_tier_index = 1
dungeon_trap_method = TRAP_MAGIC

kotl_options = {
    "Cards of Semidar": True,
    "Gems": True,
    "Gold": True,
    "Inoperative Automaton Head": True,
    "Rare Books": True,
    "Stasis Chamber Power Core": True
}
kotl_trap_method = TRAP_MAGIC

shop_options = {
    "Consumables": True,
    "Decorations": True,
    "Equipment": True,
    "Refinements": True,
    "Resources": True,
    "Tools": True
}

active_list_page = 0


def close_gump(gump_id):
    try:
        Gumps.CloseGump(gump_id)
    except:
        pass


def close_all_test_gumps():
    close_gump(MAIN_GUMP_ID)
    close_gump(PROFILE_GUMP_ID)
    close_gump(OPTIONS_GUMP_ID)
    close_gump(LIST_GUMP_ID)
    close_gump(SHOP_CATEGORY_GUMP_ID)


def say(message, hue=HUE_TEXT):
    try:
        Misc.SendMessage(message, hue)
    except:
        pass


def profile_name():
    return PROFILE_NAMES.get(active_profile, "Dungeon Chest")


def bag_state(serial):
    return "Set" if serial else "Not Set"


def bag_hue(serial):
    return HUE_ENABLED if serial else HUE_DISABLED


def enabled_text(value):
    return "Enabled" if value else "Disabled"


def check_text(value):
    return "[X]" if value else "[ ]"


def add_button(gd, x, y, button_id):
    Gumps.AddButton(gd, x, y, ACTION_BUTTON_NORMAL, ACTION_BUTTON_PRESSED, button_id, 1, 0)


def add_art_button(gd, x, y, normal_art, pressed_art, button_id):
    Gumps.AddButton(gd, x, y, normal_art, pressed_art, button_id, 1, 0)


def add_button_label(gd, x, y, button_id, text, hue=HUE_TEXT):
    add_button(gd, x, y, button_id)
    Gumps.AddLabel(gd, x + 34, y + 2, hue, text)


def add_solid_divider(gd, x, y, width):
    # Verified ChestMaster divider. ClassicUO does not reliably render the
    # older tiled-art candidate, so clip an overlong blue HTML rule instead.
    Gumps.AddHtml(
        gd, x, y, width, 22,
        "<basefont color=#0080FF>" + ("-" * max(50, width)) + "</basefont>",
        False, False
    )



def add_centered_title(gd, gump_width, y, text, hue=HUE_TEXT):
    # Razor Enhanced labels do not expose measured text width, so use the
    # established seven-pixel approximation and visually center the title.
    estimated_width = max(1, len(str(text))) * 7
    x = max(18, int((gump_width - estimated_width) / 2))
    Gumps.AddLabel(gd, x, y, hue, text)

def add_section_title(gd, y, text, width=262):
    x = DL.get("section_x", 32)
    Gumps.AddHtml(gd, x, y, width, 20,
                  "<basefont color=#FFFF00>" + text + "</basefont>",
                  False, False)
    add_solid_divider(gd, DL.get("section_divider_x", 32), y + 20,
                      DL.get("section_divider_w", width))


def add_bag_row(gd, y, label, serial, button_id):
    add_art_button(gd, DL.get("bag_button_x", 34), y + 1, ROW_ARROW_ART, ROW_ARROW_ART, button_id)
    Gumps.AddLabel(gd, DL.get("bag_label_x", 68), y, HUE_TEXT, label)
    Gumps.AddLabel(gd, DL.get("bag_state_x", 205), y, bag_hue(serial), bag_state(serial))


def add_toggle_row(gd, y, label, enabled, button_id, button_x=None, label_x=None):
    art = CHECK_ON if enabled else CHECK_OFF
    x_button = DL.get("toggle_button_x", 34) if button_x is None else button_x
    x_label = DL.get("toggle_label_x", 68) if label_x is None else label_x
    Gumps.AddButton(gd, x_button, y - 2, art, art, button_id, 1, 0)
    Gumps.AddLabel(gd, x_label, y, HUE_ENABLED if enabled else HUE_DISABLED, label)


def add_cycle_row(gd, y, label, value, button_id, enabled=True):
    hue = HUE_TEXT if enabled else HUE_DISABLED
    add_art_button(gd, DL.get("tier_button_x", 34), DL.get("tier_button_y", y + 1), ROW_ARROW_ART, ROW_ARROW_ART, button_id)
    Gumps.AddLabel(gd, DL.get("tier_label_x", 58), y, hue, label + ":  " + value)


def add_value_button(gd, y, value, button_id, enabled=True):
    hue = HUE_TEXT if enabled else HUE_DISABLED
    add_art_button(gd, DL.get("trap_button_x", 34), DL.get("trap_button_y", y + 1), ROW_ARROW_ART, ROW_ARROW_ART, button_id)
    Gumps.AddLabel(gd, DL.get("trap_label_x", 58), y, hue, value)


def add_open_row(gd, y, label, button_id):
    if button_id == BTN_DUNGEON_OPEN_RARES:
        add_art_button(gd, DL["rares_button_x"], DL["rares_button_y"], ROW_ARROW_ART, ROW_ARROW_ART, button_id)
        Gumps.AddLabel(gd, DL["rares_label_x"], y, HUE_TEXT, label)
    else:
        add_art_button(gd, 34, y + 1, ROW_ARROW_ART, ROW_ARROW_ART, button_id)
        Gumps.AddLabel(gd, 68, y, HUE_TEXT, label)


def request_container(prompt_text):
    try:
        serial = Target.PromptTarget(prompt_text)
    except:
        serial = 0
    if not serial or serial == -1:
        cm_msg("No container was selected.", HUE_DISABLED)
        return None
    try:
        item = Items.FindBySerial(serial)
    except:
        item = None
    if item is None:
        cm_msg("That target could not be found.", HUE_DISABLED)
        return None
    try:
        if not item.IsContainer:
            cm_msg("That cannot be used as a loot container.", HUE_DISABLED)
            return None
    except:
        pass
    return serial


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
    close_all_test_gumps()
    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)

    main_width = DL["main_width"]
    main_height = DL["main_height"]

    add_release_background(gd, main_width, main_height, [
        (DL["main_upper_x"], DL["main_upper_y"], DL["main_upper_w"], DL["main_upper_h"], INNER_ART),
        (DL["main_lower_x"], DL["main_lower_y"], DL["main_lower_w"], DL["main_lower_h"], INNER_ART)])

    add_chestloot_title(gd, DL["main_title_x"], DL["main_title_y"], DL["main_title_w"], DL["main_title_h"])
    add_art_button(gd, DL["mode_button_x"], DL["mode_button_y"], MODE_BUTTON_NORMAL, MODE_BUTTON_PRESSED, BTN_PROFILE_SELECT)
    Gumps.AddLabel(gd, DL["mode_label_x"], DL["mode_label_y"], HUE_BLUE, "Dungeon Chest")

    add_art_button(gd, DL["loot_button_x"], DL["loot_button_y"], ROW_ARROW_ART, ROW_ARROW_ART, BTN_TOGGLE_LOOT)
    Gumps.AddLabel(
        gd, DL["loot_label_x"], DL["loot_label_y"],
        HUE_ENABLED if loot_enabled else HUE_DISABLED,
        "Loot " + enabled_text(loot_enabled)
    )
    add_art_button(gd, DL["options_button_x"], DL["options_button_y"], CONFIG_BUTTON_NORMAL, CONFIG_BUTTON_PRESSED, BTN_OPEN_OPTIONS)

    add_button(gd, DL["learn_button_x"], DL["learn_button_y"], BTN_LEARN_RARE)
    Gumps.AddLabel(gd, DL["learn_label_x"], DL["learn_label_y"], HUE_GOLD, "Learn Rare Item")
    add_button(gd, DL["target_button_x"], DL["target_button_y"], BTN_TARGET)
    Gumps.AddLabel(gd, DL["target_label_x"], DL["target_label_y"], HUE_ENABLED, "Target Chest")

    Gumps.SendGump(MAIN_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)


def draw_profile_gump():
    close_all_test_gumps()
    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 260, 221, OUTER_ART)
    Gumps.AddBackground(gd, 18, 18, 224, 182, INNER_ART)
    add_centered_title(gd, 260, 28, "ChestLoot Pro")
    add_section_title(gd, 56, "Select Chest Type", 198)
    add_button_label(gd, 34, 91, BTN_PROFILE_DUNGEON, "Dungeon Chest")
    add_button_label(gd, 34, 126, BTN_PROFILE_KOTL, "Kotl Regal Case")
    add_button_label(gd, 34, 161, BTN_PROFILE_SHOP, "Shop Chest")
    Gumps.SendGump(PROFILE_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)


def draw_options_gump():
    if active_profile == PROFILE_DUNGEON:
        draw_dungeon_options()
    elif active_profile == PROFILE_KOTL:
        draw_kotl_options()
    else:
        draw_shop_options()


def draw_dungeon_options():
    close_all_test_gumps()
    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    add_release_background(gd, DL["options_width"], DL["options_height"], [
        (DL["options_main_x"], DL["options_main_y"], DL["options_main_w"], DL["options_main_h"], INNER_ART),
        (DL["options_footer_x"], DL["options_footer_y"], DL["options_footer_w"], DL["options_footer_h"], INNER_ART)])
    add_chestloot_title(gd, 10, 10, DL["options_width"] - 20, 26)

    add_section_title(gd, DL["bags_header_y"], "Loot Bags")
    add_bag_row(gd, DL["valuable_bag_y"], "Valuables Bag", dungeon_valuables_bag, BTN_DUNGEON_VAL_BAG)
    add_bag_row(gd, DL["magic_bag_y"], "Magic Item Bag", dungeon_magic_bag, BTN_DUNGEON_MAGIC_BAG)
    add_bag_row(gd, DL["rare_bag_y"], "Rare Item Bag", shared_rare_item_bag, BTN_DUNGEON_RARE_BAG)

    add_section_title(gd, DL["types_header_y"], "Loot Types")
    rows = [
        (DL["loot_row_1_y"], "Arrows", "Arrows", BTN_DUNGEON_AMMO, False),
        (DL["loot_row_1_y"], "Blank Scrolls", "Blank Scrolls", BTN_DUNGEON_BLANK_SCROLLS, True),
        (DL["loot_row_2_y"], "Bolts", "Bolts", BTN_DUNGEON_BOLTS, False),
        (DL["loot_row_2_y"], "Gems", "Gems", BTN_DUNGEON_GEMS, True),
        (DL["loot_row_3_y"], "Gold", "Gold", BTN_DUNGEON_GOLD, False),
        (DL["loot_row_3_y"], "Lockpicks", "Lockpicks", BTN_DUNGEON_LOCKPICKS, True),
        (DL["loot_row_4_y"], "Magic Items", "Magic Items", BTN_DUNGEON_MAGIC, False),
        (DL["loot_row_4_y"], "Potions", "Potions", BTN_DUNGEON_POTIONS, True),
        (DL["loot_row_5_y"], "Reagents", "Reagents", BTN_DUNGEON_REAGS, False),
        (DL["loot_row_5_y"], "Refinements", "Refinements", BTN_DUNGEON_REFINEMENTS, True),
        (DL["loot_row_6_y"], "Spell Scrolls", "Spell Scrolls", BTN_DUNGEON_SPELL_SCROLLS, False),
        (DL["loot_row_6_y"], "Wands", "Wands", BTN_DUNGEON_WANDS, True)
    ]
    for y, label, key, button_id, right_column in rows:
        if right_column:
            add_toggle_row(gd, y, label, dungeon_options[key], button_id, DL["toggle_right_button_x"], DL["toggle_right_label_x"])
        else:
            add_toggle_row(gd, y, label, dungeon_options[key], button_id)

    add_section_title(gd, DL["magic_header_y"], "Magic Items")
    add_cycle_row(gd, DL["tier_label_y"], "Minimum Tier", MAGIC_TIERS[dungeon_magic_tier_index], BTN_DUNGEON_MAGIC_TIER, dungeon_options["Magic Items"])

    add_section_title(gd, DL["trap_header_y"], "Trap Removal Method")
    add_value_button(gd, DL["trap_label_y"], TRAP_NAMES[dungeon_trap_method], BTN_DUNGEON_TRAP_CYCLE)

    # Recorded Items is the final content section so destination/list
    # information follows every operational setting.
    add_section_title(gd, DL["recorded_header_y"], "Recorded Items")
    add_open_row(gd, DL["rares_label_y"], "Rare Dungeon Items", BTN_DUNGEON_OPEN_RARES)

    draw_transparency_option(gd, 609, 649)

    add_art_button(gd, DL["back_button_x"], DL["back_button_y"], LEFT_ARROW_NORMAL, LEFT_ARROW_PRESSED, BTN_OPTIONS_BACK)
    Gumps.AddLabel(gd, DL["back_label_x"], DL["back_label_y"], HUE_GOLD, "Back")
    Gumps.SendGump(OPTIONS_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)

def draw_kotl_options():
    close_all_test_gumps()
    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 330, 605, OUTER_ART)
    Gumps.AddBackground(gd, 18, 18, 294, 499, INNER_ART)
    Gumps.AddBackground(gd, 18, 535, 294, 50, INNER_ART)
    add_centered_title(gd, 330, 27, "Kotl Regal Case Options")

    add_section_title(gd, 56, "Loot Bags")
    add_bag_row(gd, 91, "Valuables Bag", kotl_valuables_bag, BTN_KOTL_VAL_BAG)
    add_bag_row(gd, 116, "Kotl Item Bag", kotl_item_bag, BTN_KOTL_ITEM_BAG)

    add_section_title(gd, 153, "Loot Types")
    add_toggle_row(gd, 188, "Cards of Semidar", kotl_options["Cards of Semidar"], BTN_KOTL_CARDS)
    add_toggle_row(gd, 211, "Gems", kotl_options["Gems"], BTN_KOTL_GEMS)
    add_toggle_row(gd, 234, "Gold", kotl_options["Gold"], BTN_KOTL_GOLD)
    add_toggle_row(gd, 257, "Inoperative Automaton Head", kotl_options["Inoperative Automaton Head"], BTN_KOTL_HEADS)
    add_toggle_row(gd, 280, "Rare Books", kotl_options["Rare Books"], BTN_KOTL_BOOKS)
    add_toggle_row(gd, 303, "Stasis Chamber Power Core", kotl_options["Stasis Chamber Power Core"], BTN_KOTL_POWER_CORES)

    add_section_title(gd, 340, "Kotl Artifacts")
    Gumps.AddLabel(gd, 34, 375, HUE_ENABLED, "Automatically Looted")
    Gumps.AddLabel(gd, 34, 398, HUE_TEXT, "Destination:  Main Backpack")

    add_section_title(gd, 435, "Trap Removal Method")
    add_value_button(gd, 470, TRAP_NAMES[kotl_trap_method], BTN_KOTL_TRAP_CYCLE)

    add_button_label(gd, 34, 548, BTN_OPTIONS_BACK, "Back", HUE_GOLD)
    Gumps.SendGump(OPTIONS_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)

def draw_shop_options():
    close_all_test_gumps()
    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)

    width = 330
    height = 554
    inner_width = 294

    Gumps.AddBackground(gd, 0, 0, width, height, OUTER_ART)
    # Main options frame includes Loot Bags, Loot Types, and Recorded Items.
    Gumps.AddBackground(gd, 18, 18, inner_width, 450, INNER_ART)
    # Standard Options footer: 18-pixel gap and 50-pixel gold frame.
    Gumps.AddBackground(gd, 18, 486, inner_width, 50, INNER_ART)

    add_centered_title(gd, width, 27, "Shop Chest Options")

    add_section_title(gd, 56, "Loot Bags")
    add_bag_row(gd, 91, "Valuables Bag", shop_valuables_bag, BTN_SHOP_VAL_BAG)
    add_bag_row(gd, 116, "Shop Item Bag", shop_item_bag, BTN_SHOP_ITEM_BAG)
    add_bag_row(gd, 141, "Rare Item Bag", shared_rare_item_bag, BTN_SHOP_RARE_BAG)

    add_section_title(gd, 178, "Loot Types")
    add_toggle_row(gd, 213, "Consumables", shop_options["Consumables"], BTN_SHOP_FOOD)
    add_toggle_row(gd, 236, "Decorations", shop_options["Decorations"], BTN_SHOP_GEMS)
    add_toggle_row(gd, 259, "Equipment", shop_options["Equipment"], BTN_SHOP_POTIONS)
    add_toggle_row(gd, 282, "Refinements", shop_options["Refinements"], BTN_SHOP_REFINEMENTS)
    add_toggle_row(gd, 305, "Resources", shop_options["Resources"], BTN_SHOP_RESOURCES)
    add_toggle_row(gd, 328, "Tools", shop_options["Tools"], BTN_SHOP_TOOLS)

    add_section_title(gd, 365, "Recorded Items")
    add_open_row(gd, 400, "Rare Items", BTN_SHOP_OPEN_RARES)
    add_open_row(gd, 425, "Shop Items", BTN_SHOP_OPEN_ITEMS)

    add_button_label(gd, 34, 499, BTN_OPTIONS_BACK, "Back", HUE_GOLD)
    Gumps.SendGump(
        OPTIONS_GUMP_ID,
        Player.Serial,
        GUMP_X,
        GUMP_Y,
        gd.gumpDefinition,
        gd.gumpStrings
    )

def _legacy_get_active_list():
    if active_list_name == "rare":
        return rare_items, "Rare Items"
    return shop_items, "Shop Items"


def _legacy_draw_list_gump():
    close_all_test_gumps()
    items, title = get_active_list()
    visible_count = max(1, len(items))
    height = 170 + (visible_count * 35)
    footer_y = height - 71

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)
    Gumps.AddBackground(gd, 0, 0, 320, height, OUTER_ART)
    Gumps.AddBackground(gd, 18, 18, 284, footer_y - 36, INNER_ART)
    Gumps.AddBackground(gd, 18, footer_y, 284, 50, INNER_ART)
    Gumps.AddLabel(gd, 34, 28, HUE_TEXT, title)
    add_solid_divider(gd, 34, 51, 252)

    if not items:
        Gumps.AddLabel(gd, 34, 78, HUE_DISABLED, "No entries recorded.")
    else:
        y = 78
        for index, item_name in enumerate(items):
            add_button(gd, 34, y - 2, BTN_LIST_REMOVE_BASE + index)
            Gumps.AddLabel(gd, 68, y, HUE_TEXT, item_name)
            Gumps.AddLabel(gd, 235, y, HUE_DISABLED, "Remove")
            y += 35

    add_button_label(gd, 34, footer_y + 13, BTN_LIST_BACK, "Back", HUE_GOLD)
    Gumps.SendGump(LIST_GUMP_ID, Player.Serial, GUMP_X, GUMP_Y, gd.gumpDefinition, gd.gumpStrings)


def _legacy_handle_bag_target(button_id):
    global dungeon_valuables_bag, dungeon_magic_bag, shared_rare_item_bag
    global kotl_valuables_bag, kotl_item_bag, shop_valuables_bag, shop_item_bag
    serial = request_container("Target the loot destination container.")
    if not serial:
        return
    if button_id == BTN_DUNGEON_VAL_BAG:
        dungeon_valuables_bag = serial
    elif button_id == BTN_DUNGEON_MAGIC_BAG:
        dungeon_magic_bag = serial
    elif button_id == BTN_DUNGEON_RARE_BAG:
        shared_rare_item_bag = serial
    elif button_id == BTN_KOTL_VAL_BAG:
        kotl_valuables_bag = serial
    elif button_id == BTN_KOTL_ITEM_BAG:
        kotl_item_bag = serial
    elif button_id == BTN_SHOP_VAL_BAG:
        shop_valuables_bag = serial
    elif button_id == BTN_SHOP_ITEM_BAG:
        shop_item_bag = serial
    elif button_id == BTN_SHOP_RARE_BAG:
        shared_rare_item_bag = serial


def open_list(list_name):
    global active_list_name, current_screen
    active_list_name = list_name
    current_screen = "list"
    if list_name == "rare" and active_profile == PROFILE_DUNGEON:
        dungeon_rare_count_message()
    draw_list_gump()


def _legacy_handle_dungeon_option(button_id):
    global dungeon_trap_method, dungeon_magic_tier_index
    if button_id in [BTN_DUNGEON_VAL_BAG, BTN_DUNGEON_MAGIC_BAG, BTN_DUNGEON_RARE_BAG]:
        handle_bag_target(button_id)
        return
    toggle_map = {
        BTN_DUNGEON_AMMO: "Arrows",
        BTN_DUNGEON_BOLTS: "Bolts",
        BTN_DUNGEON_BLANK_SCROLLS: "Blank Scrolls",
        BTN_DUNGEON_GEMS: "Gems",
        BTN_DUNGEON_GOLD: "Gold",
        BTN_DUNGEON_LOCKPICKS: "Lockpicks",
        BTN_DUNGEON_MAGIC: "Magic Items",
        BTN_DUNGEON_POTIONS: "Potions",
        BTN_DUNGEON_REAGS: "Reagents",
        BTN_DUNGEON_REFINEMENTS: "Refinements",
        BTN_DUNGEON_SPELL_SCROLLS: "Spell Scrolls",
        BTN_DUNGEON_WANDS: "Wands"
    }
    if button_id in toggle_map:
        key = toggle_map[button_id]
        dungeon_options[key] = not dungeon_options[key]
        state_text = "enabled" if dungeon_options[key] else "disabled"
        cm_msg("{} looting is now {}.".format(key, state_text), HUE_JOURNAL_OPTION)
    elif button_id == BTN_DUNGEON_MAGIC_TIER:
        if dungeon_options["Magic Items"]:
            dungeon_magic_tier_index = (dungeon_magic_tier_index + 1) % len(MAGIC_TIERS)
            cm_msg("Minimum Magic Tier is now {}.".format(MAGIC_TIERS[dungeon_magic_tier_index]), HUE_JOURNAL_OPTION)
    elif button_id == BTN_DUNGEON_TRAP_CYCLE:
        dungeon_trap_method = TRAP_SKILL if dungeon_trap_method == TRAP_MAGIC else TRAP_MAGIC
        cm_msg("{} has been selected.".format(TRAP_NAMES[dungeon_trap_method]), HUE_JOURNAL_OPTION)
    elif button_id == BTN_DUNGEON_OPEN_RARES:
        open_list("rare")

def _legacy_handle_kotl_option(button_id):
    global kotl_trap_method
    if button_id in [BTN_KOTL_VAL_BAG, BTN_KOTL_ITEM_BAG]:
        handle_bag_target(button_id)
        return
    toggle_map = {
        BTN_KOTL_CARDS: "Cards of Semidar",
        BTN_KOTL_GEMS: "Gems",
        BTN_KOTL_GOLD: "Gold",
        BTN_KOTL_HEADS: "Inoperative Automaton Head",
        BTN_KOTL_BOOKS: "Rare Books",
        BTN_KOTL_POWER_CORES: "Stasis Chamber Power Core"
    }
    if button_id in toggle_map:
        key = toggle_map[button_id]
        kotl_options[key] = not kotl_options[key]
    elif button_id == BTN_KOTL_TRAP_CYCLE:
        kotl_trap_method = TRAP_SKILL if kotl_trap_method == TRAP_MAGIC else TRAP_MAGIC

def _legacy_handle_shop_option(button_id):
    if button_id in [BTN_SHOP_VAL_BAG, BTN_SHOP_ITEM_BAG, BTN_SHOP_RARE_BAG]:
        handle_bag_target(button_id)
        return

    toggle_map = {
        BTN_SHOP_FOOD: "Consumables",
        BTN_SHOP_GEMS: "Decorations",
        BTN_SHOP_POTIONS: "Equipment",
        BTN_SHOP_REFINEMENTS: "Refinements",
        BTN_SHOP_RESOURCES: "Resources",
        BTN_SHOP_TOOLS: "Tools"
    }

    if button_id in toggle_map:
        key = toggle_map[button_id]
        shop_options[key] = not shop_options[key]
    elif button_id == BTN_SHOP_OPEN_RARES:
        open_list("rare")
    elif button_id == BTN_SHOP_OPEN_ITEMS:
        open_list("shop")


def get_button_id(gump_id):
    try:
        if not Gumps.WaitForGump(gump_id, 1):
            return None
    except:
        return None
    try:
        response = Gumps.GetGumpData(gump_id)
        return int(response.buttonid)
    except:
        return None


def _legacy_handle_main_screen():
    global current_screen, loot_enabled, gump_closed
    button_id = get_button_id(MAIN_GUMP_ID)
    if button_id is None:
        return
    if button_id == 0:
        gump_closed = True
    elif button_id == BTN_PROFILE_SELECT:
        current_screen = "profile"
        draw_profile_gump()
    elif button_id == BTN_TOGGLE_LOOT:
        loot_enabled = not loot_enabled
        draw_main_gump()
    elif button_id == BTN_OPEN_OPTIONS:
        current_screen = "options"
        draw_options_gump()
    elif button_id == BTN_LEARN_RARE and active_profile in (PROFILE_DUNGEON, PROFILE_SHOP):
        say("UI test only: Learn Rare Item is not connected.", HUE_GOLD)
        draw_main_gump()
    elif button_id == BTN_LEARN_SHOP_ITEM and active_profile == PROFILE_SHOP:
        say("UI test only: Learn Shop Item is not connected.", HUE_GOLD)
        draw_main_gump()
    elif button_id == BTN_STEAL_ITEM and active_profile == PROFILE_SHOP:
        say("UI test only: Steal Next Item is not connected.", HUE_DISABLED)
        draw_main_gump()
    elif button_id == BTN_TARGET:
        say("UI test only: {} processing is not connected.".format(profile_name()), HUE_INFO)
        draw_main_gump()


def _legacy_handle_profile_screen():
    global active_profile, current_screen, gump_closed
    button_id = get_button_id(PROFILE_GUMP_ID)
    if button_id is None:
        return
    if button_id == 0:
        gump_closed = True
    elif button_id == BTN_PROFILE_DUNGEON:
        active_profile = PROFILE_DUNGEON
        current_screen = "main"
        draw_main_gump()
    elif button_id == BTN_PROFILE_KOTL:
        active_profile = PROFILE_KOTL
        current_screen = "main"
        draw_main_gump()
    elif button_id == BTN_PROFILE_SHOP:
        active_profile = PROFILE_SHOP
        current_screen = "main"
        draw_main_gump()


def handle_options_screen():
    global current_screen, gump_closed
    button_id = get_button_id(OPTIONS_GUMP_ID)
    if button_id is None:
        return
    if button_id == 0:
        current_screen = "main"
        draw_main_gump()
        return
    if button_id == BTN_OPTIONS_BACK:
        current_screen = "main"
        draw_main_gump()
        return
    if button_id == BTN_TRANSPARENT_GUMPS and active_profile == PROFILE_DUNGEON:
        try:
            on = transparent_ui.toggle(settings_path(), Player.Serial)
            cm_msg("Transparency is {}.".format("enabled" if on else "disabled"), HUE_JOURNAL_OPTION)
        except Exception as ex:
            cm_msg("Transparency could not be saved: " + str(ex), HUE_DISABLED)
        draw_options_gump()
        return
    close_gump(OPTIONS_GUMP_ID)
    if active_profile == PROFILE_DUNGEON:
        handle_dungeon_option(button_id)
    elif active_profile == PROFILE_KOTL:
        handle_kotl_option(button_id)
    else:
        handle_shop_option(button_id)
    if current_screen == "options":
        draw_options_gump()


def _legacy_handle_list_screen():
    global current_screen, gump_closed, active_list_page

    button_id = get_button_id(LIST_GUMP_ID)
    if button_id is None:
        return

    if button_id == 0:
        gump_closed = True
        return

    if button_id == BTN_LIST_BACK:
        current_screen = "options"
        active_list_page = 0
        draw_options_gump()
        return

    if button_id == BTN_LIST_PREV:
        active_list_page = max(0, active_list_page - 1)
        draw_list_gump()
        return

    if button_id == BTN_LIST_NEXT:
        active_list_page += 1
        draw_list_gump()
        return

    if button_id >= BTN_LIST_REMOVE_BASE:
        entries, title = get_active_list()
        index = button_id - BTN_LIST_REMOVE_BASE

        if 0 <= index < len(entries):
            removed = entries.pop(index)
            cm_msg(
                "Removed from {}: {}".format(
                    title,
                    removed.get("name", "Unknown Item")
                ),
                HUE_DISABLED
            )
            save_all()

        draw_list_gump()


def _legacy_ui_test_run():
    global gump_closed
    close_all_test_gumps()
    gump_closed = False
    say("ChestLoot Pro gump test v0.1.13 started.", HUE_GOLD)
    draw_profile_gump()
    while not gump_closed:
        if current_screen == "main":
            handle_main_screen()
        elif current_screen == "profile":
            handle_profile_screen()
        elif current_screen == "options":
            handle_options_screen()
        elif current_screen == "list":
            handle_list_screen()
        Misc.Pause(50)
    close_all_test_gumps()
    say("ChestLoot Pro gump test closed.", HUE_DISABLED)



# Release Notes - Beta 0.2.3
#   - Restored the exact proven Dungeon Chest Pro item-move cadence.
#   - Removed the duplicate five-attempt post-move verification loop.
#   - Historical engine note: restored rare-found sound 580.
#   - Rare feedback now fires only after a successful move request.
#   - Kotl artifact detection now uses only the confirmed hue 0x0A1F.
#   - Removed artifact name/property fallback to avoid unnecessary property requests.
#
# ============================================================
# WORKING ENGINE - Beta 0.2.3
# ============================================================
# Release Notes
#   - Integrated the finalized v0.1.15 gumps with persistent settings.
#   - Preserved the proven Dungeon Chest lockpick, trap, open, and loot flow.
#   - Lockpicks are always looted to the Dungeon Valuables Bag.
#   - Added shared Rare Item knowledge and one shared Rare Item Bag.
#   - Added Kotl Regal Case trap/open/loot processing.
#   - Added Shop Chest targeting, learned item database, and Steal Next Item.
#   - Added persistent Rare, Ignore, and Shop Item lists.
#   - Added weight protection and immersive journal messages.
#
# Beta note:
#   Kotl named categories are identified by item name/properties. This avoids
#   hardcoding unverified shard-specific graphics while retaining the confirmed
#   Stasis Chamber Power Core graphic. Kotl artifacts are detected only by
#   hue 0x0A1F and always go to the main backpack.
# ============================================================

import os
import json
import time
import imp

VERSION = "1.0"
SETTINGS_FILE = "ChestLootPro_Settings.json"
KNOWLEDGE_FILE = "ChestLootPro_Knowledge.json"

LOCKPICK_ID = 0x14FC
REMOVE_TRAP_SKILL = "Remove Trap"
MAGIC_UNTRAP_SPELL = "Magic Untrap"
STEALING_SKILL = "Stealing"

MAX_LOCKPICK_ATTEMPTS = 10
MAX_TRAP_ATTEMPTS = 10
MAX_REMOVE_TRAP_FAILURES = 5
REMOVE_TRAP_COOLDOWN_MS = 10000
REMOVE_TRAP_COOLDOWN_BUFFER_MS = 500
WEIGHT_BUFFER = 10
TARGET_WAIT = 1800
OPEN_DELAY = 1200
LOOT_START_DELAY = 600
LOOT_MOVE_DELAY = 900
ACTION_DELAY = 700
ACTION_WAIT_DELAY = 1250
MAX_OPEN_ATTEMPTS = 2
MAX_MOVE_ATTEMPTS = 2
OPEN_RETRY_DELAY = 350
MOVE_INTERVAL = 900
MAGIC_UNTRAP_CONFIRM_TIMEOUT = 700
MAGIC_UNTRAP_CAST_CONFLICT_DELAY = 500
MAGIC_UNTRAP_ACTION_LANE_TIMEOUT = 5000
MAGIC_UNTRAP_ACTION_LANE_STABLE = 500
SNAPSHOT_POLL_INTERVAL = 100
SNAPSHOT_STABILITY_TIMEOUT = 900
SNAPSHOT_MIN_OBSERVE = 250
FINAL_LOOT_PASSES = 2

last_remove_trap_ms = 0

GOLD_IDS = [0x0EED]
LOCKPICK_IDS = [0x14FC]
GEM_IDS = [0x0F0F,0x0F10,0x0F11,0x0F13,0x0F15,0x0F16,0x0F18,0x0F21,0x0F25,0x0F26,0x0F2D]
REAGENT_IDS = [0x0F7A,0x0F7B,0x0F84,0x0F85,0x0F86,0x0F88,0x0F8C,0x0F8D]
BLANK_SCROLL_IDS = [0x0EF3]
ARROW_IDS = [0x0F3F]
BOLT_IDS = [0x1BFB]
POTION_IDS = [0x0F06,0x0F07,0x0F08,0x0F09,0x0F0A,0x0F0B,0x0F0C,0x0F0D]
REFINEMENT_IDS = [0x4CD8,0x4CD9,0x4CDA,0x142B,0x2D61,0x142A]
SPELL_SCROLL_MIN = 0x1F2D
SPELL_SCROLL_MAX = 0x1F6C
STASIS_POWER_CORE_ID = 0x9CDB
KOTL_ARTIFACT_HUE = 0x0A1F
RARE_FOUND_SOUND = 580       # 0x0244
RARE_FOUND_HUE = HUE_ORANGE   # recorded Rare treasure event

# Fast equipment recognition. ItemID remains the primary path for normal loot;
# these characteristics prevent mundane gear and jewelry from becoming false
# rare alerts without performing an exhaustive property scan.
EQUIPMENT_LAYERS = set([
    "right hand", "lefthand", "left hand", "shoes", "pants", "shirt", "helm",
    "gloves", "ring", "neck", "waist", "inner torso", "bracelet", "middle torso",
    "earrings", "arms", "cloak", "outer torso", "outer legs", "inner legs"
])
EQUIPMENT_NAME_WORDS = (
    "sword", "katana", "wakizashi", "kryss", "dagger", "axe", "mace", "maul",
    "hammer", "spear", "pitchfork", "halberd", "bardiche", "bow", "crossbow",
    "staff", "wand", "shield", "buckler", "helmet", "helm", "gorget", "tunic",
    "leggings", "gloves", "gauntlets", "sleeves", "arms", "chest", "breastplate",
    "ring", "bracelet", "earrings"
)

# Common food/resources/tools are intentionally conservative. The Learn Shop
# Item feature supplements these lists without requiring code edits.
FOOD_IDS = [0x097B,0x09B7,0x09C0,0x09C9,0x09D0,0x09D1,0x09D2,0x09D3,0x09E9,0x09EA,0x09EB,0x09EC,0x09ED,0x09F2,0x09F4,0x09F5,0x09F6,0x09F7,0x09F8,0x09F9,0x09FA,0x09FB,0x09FC,0x09FD,0x09FE,0x09FF,0x0A00,0x0C5C,0x0C64,0x0C6A]
RESOURCE_IDS = [0x0EED,0x0F7A,0x0F7B,0x0F84,0x0F85,0x0F86,0x0F88,0x0F8C,0x0F8D,0x1766,0x19B7,0x1BDD,0x1BF2,0x1BD1]
TOOL_IDS = [0x0E85,0x0E86,0x0F39,0x0F43,0x1022,0x1028,0x1034,0x1035,0x13E3,0x13E4,0x14FB,0x14FC]

PICK_SUCCESS = ["The lock quickly yields to your skill","You manage to pick the lock","You successfully pick the lock","This does not appear to be locked","That is not locked"]
PICK_FAIL = ["You fail to pick the lock","You are unable to pick the lock"]
LOCKED_MESSAGES = ["It appears to be locked","That appears to be locked","This appears to be locked"]
ACTION_WAIT_MESSAGES = ["You must wait to perform another action"]
SPELL_CAST_CONFLICT_MESSAGES = ["You are already casting a spell"]
MAGIC_UNTRAP_WRONG_TARGET = ["That isn't trapped"]
BANDAGE_TARGET_COLLISION = ["Bandages cannot be used on that"]
TRAP_SUCCESS = ["You successfully render the trap harmless"]
TRAP_NOT_PRESENT = ["That doesn't appear to be trapped"]
TRAP_FAIL = ["You fail to disarm the trap","You must wait to perform another action"]
HARD_STOP = ["That is too far away","You can't reach that","You do not see that","Target cannot be seen","Cannot see"]
SPELL_FAIL = ["The spell fizzles","You have not yet recovered from casting a spell","You must wait to perform another action","You lack the mana","Insufficient mana","Your concentration is disturbed"] + SPELL_CAST_CONFLICT_MESSAGES + HARD_STOP + MAGIC_UNTRAP_WRONG_TARGET + BANDAGE_TARGET_COLLISION
STEAL_SUCCESS = ["You successfully steal","You successfully pilfer","You steal the item"]
STEAL_FAIL = ["You fail to steal","You cannot steal","That is too heavy","You must wait to perform another action","You can't steal"]

# Replace UI-only example data.
rare_items = []
ignored_items = []
shop_items = []
current_shop_chest = None
shop_steal_ready_at = 0.0
SHOP_STEAL_COOLDOWN_SECONDS = 10.0


def script_dir():
    try: return os.path.dirname(__file__)
    except: return os.getcwd()


def settings_path(): return os.path.join(script_dir(), SETTINGS_FILE)
def knowledge_path(): return os.path.join(script_dir(), KNOWLEDGE_FILE)


transparent_ui = imp.load_source("chestloot_transparent_ui", os.path.join(script_dir(), "transparent_ui.py"))


def add_release_background(gd, width, height, panels):
    transparent_ui.add_background(Gumps, gd, width, height, OUTER_ART, panels,
                                  transparent_ui.enabled(settings_path(), Player.Serial))


def draw_transparency_option(gd, header_y, row_y):
    add_section_title(gd, header_y, "Transparency")
    on = transparent_ui.enabled(settings_path(), Player.Serial)
    art = CHECK_ON if on else CHECK_OFF
    Gumps.AddButton(gd, 34, row_y - 2, art, art, BTN_TRANSPARENT_GUMPS, 1, 0)
    Gumps.AddLabel(gd, 68, row_y, HUE_ENABLED if on else HUE_TEXT, "Transparent Gumps")


def cm_msg(text, hue=HUE_ENABLED):
    say("[ChestLoot Pro] " + text, hue)


def item_name(item):
    try:
        name = str(item.Name or "").strip()
        if name: return name
    except: pass
    return "Unknown Item"


def get_props(item, prop_cache=None):
    serial = int(item.Serial)
    if prop_cache is not None and serial in prop_cache:
        return prop_cache[serial]
    try: Items.WaitForProps(item, 750)
    except: pass
    try: values = Items.GetPropStringList(item.Serial) or []
    except: values = []
    result = [str(v).lower() for v in values]
    if prop_cache is not None:
        prop_cache[serial] = result
    return result


def item_text(item, prop_cache=None):
    return " ".join([item_name(item).lower()] + get_props(item, prop_cache))


def entry_for(item, category=None):
    return {"id": int(item.ItemID), "name": item_name(item), "category": category or ""}


def entry_matches(entry, item):
    try: return int(entry.get("id", -1)) == int(item.ItemID)
    except: return False


def has_entry(entries, item):
    return any(entry_matches(e, item) for e in entries)


def add_entry(entries, item, category=None):
    if has_entry(entries, item): return False
    entries.append(entry_for(item, category))
    # Rare journals are discovery histories. Keep new treasures in the order
    # the player records them so the newest entry remains easy to locate.
    return True


def journal_has(lines):
    for line in lines:
        try:
            if Journal.Search(line): return True
        except: pass
    return False


def wait_journal(success, fail, timeout=3500):
    loops=max(1,int(timeout/100))
    for _ in range(loops):
        if journal_has(success): return "success"
        if journal_has(HARD_STOP): return "hard"
        if journal_has(fail): return "fail"
        Misc.Pause(100)
    return "timeout"


def save_all():
    # Preserve settings owned by Shop, Kotl, and Exodus. Every mode shares the
    # same durable JSON files, so save only our fields into the existing data.
    try:
        with open(settings_path(),"r") as f: settings=json.load(f)
        if not isinstance(settings,dict): settings={}
    except: settings={}
    settings.update({
        "active_profile":active_profile,"loot_enabled":loot_enabled,
        "dungeon_valuables_bag":dungeon_valuables_bag,"dungeon_magic_bag":dungeon_magic_bag,
        "shared_rare_item_bag":shared_rare_item_bag,"kotl_valuables_bag":kotl_valuables_bag,
        "kotl_item_bag":kotl_item_bag,"shop_valuables_bag":shop_valuables_bag,"shop_item_bag":shop_item_bag,
        "dungeon_options":dungeon_options,"dungeon_magic_tier_index":dungeon_magic_tier_index,
        "dungeon_trap_method":dungeon_trap_method,"kotl_options":kotl_options,
        "kotl_trap_method":kotl_trap_method,"shop_options":shop_options
    })
    try:
        with open(knowledge_path(),"r") as f: knowledge=json.load(f)
        if not isinstance(knowledge,dict): knowledge={}
    except: knowledge={}
    knowledge.update({"rare_items":rare_items,"ignored_items":ignored_items,"shop_items":shop_items})
    try:
        with open(settings_path(),"w") as f: json.dump(settings,f,indent=2)
        with open(knowledge_path(),"w") as f: json.dump(knowledge,f,indent=2)
    except Exception as ex:
        cm_msg("Your records could not be saved: " + str(ex), HUE_DISABLED)


def load_all():
    global active_profile,loot_enabled,dungeon_valuables_bag,dungeon_magic_bag,shared_rare_item_bag
    global kotl_valuables_bag,kotl_item_bag,shop_valuables_bag,shop_item_bag
    global dungeon_magic_tier_index,dungeon_trap_method,kotl_trap_method
    global rare_items,ignored_items,shop_items
    try:
        with open(settings_path(),"r") as f: data=json.load(f)
        active_profile=int(data.get("active_profile",active_profile)); loot_enabled=bool(data.get("loot_enabled",loot_enabled))
        dungeon_valuables_bag=data.get("dungeon_valuables_bag"); dungeon_magic_bag=data.get("dungeon_magic_bag")
        shared_rare_item_bag=data.get("shared_rare_item_bag"); kotl_valuables_bag=data.get("kotl_valuables_bag")
        kotl_item_bag=data.get("kotl_item_bag"); shop_valuables_bag=data.get("shop_valuables_bag"); shop_item_bag=data.get("shop_item_bag")
        saved_dungeon_options = data.get("dungeon_options", {}) or {}
        dungeon_options.update(saved_dungeon_options)
        if "Ammunition" in saved_dungeon_options:
            old_ammunition = bool(saved_dungeon_options.get("Ammunition"))
            if "Arrows" not in saved_dungeon_options: dungeon_options["Arrows"] = old_ammunition
            if "Bolts" not in saved_dungeon_options: dungeon_options["Bolts"] = old_ammunition
        dungeon_options.pop("Ammunition", None)
        kotl_options.update(data.get("kotl_options",{})); shop_options.update(data.get("shop_options",{}))
        dungeon_magic_tier_index=int(data.get("dungeon_magic_tier_index",dungeon_magic_tier_index))
        dungeon_trap_method=int(data.get("dungeon_trap_method",dungeon_trap_method)); kotl_trap_method=int(data.get("kotl_trap_method",kotl_trap_method))
    except: pass
    try:
        with open(knowledge_path(),"r") as f: data=json.load(f)
        rare_items=data.get("rare_items",[]) or []; ignored_items=data.get("ignored_items",[]) or []; shop_items=data.get("shop_items",[]) or []
        for entry in shop_items:
            entry["category"] = normalize_shop_category(entry.get("category"))
    except: pass


def request_item(prompt):
    try: serial=Target.PromptTarget(prompt)
    except: serial=0
    if not serial or serial==-1: return None
    try: return Items.FindBySerial(serial)
    except: return None


def set_bag(button_id):
    global dungeon_valuables_bag,dungeon_magic_bag,shared_rare_item_bag,kotl_valuables_bag,kotl_item_bag,shop_valuables_bag,shop_item_bag
    # An empty Razor prompt avoids an extra client-colored journal line.
    # The completed selection receives one authoritative gold confirmation.
    serial=request_container("")
    if not serial: return
    bag_name = "Loot Bag"
    if button_id==BTN_DUNGEON_VAL_BAG: dungeon_valuables_bag=serial; bag_name="Valuables Bag"
    elif button_id==BTN_DUNGEON_MAGIC_BAG: dungeon_magic_bag=serial; bag_name="Magic Item Bag"
    elif button_id in (BTN_DUNGEON_RARE_BAG,BTN_SHOP_RARE_BAG): shared_rare_item_bag=serial; bag_name="Rare Item Bag"
    elif button_id==BTN_KOTL_VAL_BAG: kotl_valuables_bag=serial; bag_name="Valuables Bag"
    elif button_id==BTN_KOTL_ITEM_BAG: kotl_item_bag=serial; bag_name="Kotl Item Bag"
    elif button_id==BTN_SHOP_VAL_BAG: shop_valuables_bag=serial; bag_name="Valuables Bag"
    elif button_id==BTN_SHOP_ITEM_BAG: shop_item_bag=serial; bag_name="Shop Item Bag"
    save_all(); cm_msg("Your {} has been recorded.".format(bag_name), HUE_JOURNAL_OPTION)


def learn_rare():
    item=request_item("Target the rare item to record.")
    if not item: cm_msg("No treasure was recorded.",HUE_DISABLED); return
    if add_entry(rare_items,item): cm_msg("This treasure has been added to your journal.",HUE_JOURNAL_OPTION)
    else: cm_msg("This treasure is already recorded.",HUE_JOURNAL_OPTION)
    save_all()


def normalize_shop_category(category):
    legacy_map = {
        "Food": "Consumables",
        "Potions": "Consumables",
        "Spell Scrolls": "Consumables",
        "Gems": "Resources",
        "Reagents": "Resources",
        "Magic": "Equipment",
        "Jewelry": "Equipment",
        "Weapons": "Equipment",
        "Refinements": "Refinements",
        "Resources": "Resources",
        "Tools": "Tools",
        "Consumables": "Consumables",
        "Decorations": "Decorations",
        "Equipment": "Equipment"
    }
    return legacy_map.get(category, category if category in shop_options else "Resources")


def infer_shop_category(item):
    iid = int(item.ItemID)
    text_value = item_text(item)

    if iid in REFINEMENT_IDS or any(
        word in text_value
        for word in ["refinement", "polish", "varnish", "scour", "gloss", "wash"]
    ):
        return "Refinements"

    if iid in TOOL_IDS or any(
        word in text_value
        for word in ["tool", "shovel", "pickaxe", "tongs", "sewing kit", "scissors"]
    ):
        return "Tools"

    if (
        iid in POTION_IDS
        or SPELL_SCROLL_MIN <= iid <= SPELL_SCROLL_MAX
        or iid in FOOD_IDS
        or any(
            word in text_value
            for word in [
                "potion", "scroll", "food", "bread", "fish", "meat",
                "fruit", "vegetable", "apple", "pear", "grape",
                "wine", "liquor", "ale", "bandage"
            ]
        )
    ):
        return "Consumables"

    if iid in GEM_IDS or iid in REAGENT_IDS:
        return "Resources"

    if any(
        word in text_value
        for word in [
            "book", "ledger", "journal", "flower", "herb", "horseshoe",
            "forged metal", "statue", "painting", "decorative"
        ]
    ):
        return "Decorations"

    if any(
        word in text_value
        for word in [
            "spellbook", "runebook", "wand", "sword", "axe", "mace",
            "dagger", "bow", "crossbow", "shield", "helmet", "robe",
            "shirt", "pants", "boots", "shoes", "sandals", "ring",
            "bracelet", "necklace", "earrings"
        ]
    ):
        return "Equipment"

    return "Resources"


SHOP_CATEGORY_BUTTONS = [
    (BTN_SHOP_CATEGORY_CONSUMABLES, "Consumables"),
    (BTN_SHOP_CATEGORY_DECORATIONS, "Decorations"),
    (BTN_SHOP_CATEGORY_EQUIPMENT, "Equipment"),
    (BTN_SHOP_CATEGORY_REFINEMENTS, "Refinements"),
    (BTN_SHOP_CATEGORY_RESOURCES, "Resources"),
    (BTN_SHOP_CATEGORY_TOOLS, "Tools")
]


def choose_shop_category():
    close_gump(SHOP_CATEGORY_GUMP_ID)

    width = 290
    height = 366
    inner_width = width - 36

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)

    Gumps.AddBackground(gd, 0, 0, width, height, OUTER_ART)
    Gumps.AddBackground(gd, 18, 18, inner_width, 262, INNER_ART)
    Gumps.AddBackground(gd, 18, 298, inner_width, 50, INNER_ART)

    add_centered_title(gd, width, 28, "Choose Shop Item Category")
    add_solid_divider(gd, 34, 51, width - 68)

    y = 70
    for button_id, category in SHOP_CATEGORY_BUTTONS:
        add_button_label(gd, 34, y, button_id, category, HUE_TEXT)
        y += 34

    add_button_label(
        gd,
        34,
        311,
        BTN_SHOP_CATEGORY_CANCEL,
        "Back",
        HUE_GOLD
    )

    Gumps.SendGump(
        SHOP_CATEGORY_GUMP_ID,
        Player.Serial,
        GUMP_X,
        GUMP_Y,
        gd.gumpDefinition,
        gd.gumpStrings
    )

    while True:
        try:
            if Gumps.WaitForGump(SHOP_CATEGORY_GUMP_ID, 100):
                response = Gumps.GetGumpData(SHOP_CATEGORY_GUMP_ID)
                button_id = int(response.buttonid)
                close_gump(SHOP_CATEGORY_GUMP_ID)

                if button_id in (0, BTN_SHOP_CATEGORY_CANCEL):
                    return None

                for category_button, category in SHOP_CATEGORY_BUTTONS:
                    if button_id == category_button:
                        return category

                return None
        except:
            return None

        Misc.Pause(50)


def learn_shop():
    category=choose_shop_category()
    if not category:
        cm_msg("No shop category was selected.",HUE_DISABLED)
        return

    item=request_item("Target the {} item to record.".format(category.lower()))
    if not item:
        cm_msg("No shop item was recorded.",HUE_DISABLED)
        return

    for entry in shop_items:
        if entry_matches(entry,item):
            old_category=entry.get("category","")
            entry["name"]=item_name(item)
            entry["category"]=category
            shop_items.sort(key=lambda e:e.get("name","").lower())
            save_all()
            if old_category==category:
                cm_msg("This shop item is already recorded under {}.".format(category.lower()),HUE_INFO)
            else:
                cm_msg("This shop item is now recorded under {}.".format(category.lower()),HUE_GOLD)
            return

    shop_items.append(entry_for(item,category))
    shop_items.sort(key=lambda e:e.get("name","").lower())
    save_all()
    cm_msg("This item has been added to the {} section of your shop journal.".format(category.lower()),HUE_GOLD)


def get_lockpick():
    try: return Items.FindByID(LOCKPICK_ID,-1,Player.Backpack.Serial)
    except: return None


def use_targeted(action,target,wait=TARGET_WAIT):
    try:
        action(); Target.WaitForTarget(wait,False); Target.TargetExecute(target); return True
    except: return False


def target_cursor_busy():
    try: return bool(Target.HasTarget())
    except: return False


def player_casting_or_frozen():
    try: return bool(Player.Paralized)
    except: return False


def wait_for_magic_untrap_lane():
    started = now_ms()
    clear_since = 0
    while now_ms() - started < MAGIC_UNTRAP_ACTION_LANE_TIMEOUT:
        if not target_cursor_busy() and not player_casting_or_frozen():
            if not clear_since: clear_since = now_ms()
            if now_ms() - clear_since >= MAGIC_UNTRAP_ACTION_LANE_STABLE:
                return True
        else:
            clear_since = 0
        Misc.Pause(50)
    return False


def cast_magic_untrap_targeted(chest):
    if not wait_for_magic_untrap_lane():
        cm_msg("Another spell or targeting action is in progress. The chest remains closed.", HUE_DISABLED)
        return False
    try:
        Spells.CastMagery(MAGIC_UNTRAP_SPELL)
        if not Target.WaitForTarget(TARGET_WAIT, False):
            return False
        Target.TargetExecute(chest)
    except:
        return False
    return True


def now_ms():
    return int(time.time() * 1000)


def chest_out_of_range_message():
    cm_msg("The chest is beyond your reach. Move closer and try again.", HUE_DISABLED)


def wait_for_remove_trap_cooldown():
    if not last_remove_trap_ms:
        return
    ready_at = last_remove_trap_ms + REMOVE_TRAP_COOLDOWN_MS + REMOVE_TRAP_COOLDOWN_BUFFER_MS
    remaining = ready_at - now_ms()
    if remaining <= 0:
        return
    seconds = max(0.1, remaining / 1000.0)
    cm_msg(
        "You steady your hands, waiting {:.1f} seconds before examining the trap.".format(seconds),
        HUE_BLUE
    )
    Misc.Pause(remaining)


def wait_after_remove_trap_failure():
    ready_at = last_remove_trap_ms + REMOVE_TRAP_COOLDOWN_MS + REMOVE_TRAP_COOLDOWN_BUFFER_MS
    remaining = max(0, ready_at - now_ms())
    cm_msg(
        "The trap resists your efforts. You prepare to examine it again.",
        HUE_BLUE
    )
    if remaining > 0:
        Misc.Pause(remaining)


def pick_lock(chest):
    for _ in range(MAX_LOCKPICK_ATTEMPTS):
        pick=get_lockpick()
        if not pick: cm_msg("You have no lockpicks remaining.",HUE_DISABLED); return False
        try: Journal.Clear()
        except: pass
        if not use_targeted(lambda:Items.UseItem(pick),chest): return False
        result=wait_journal(PICK_SUCCESS,PICK_FAIL,3000)
        if result=="success": return True
        if result=="hard":
            chest_out_of_range_message()
            return False
        Misc.Pause(ACTION_DELAY)
    cm_msg("The lock refuses to yield.",HUE_DISABLED); return False


def remove_trap(chest,method):
    global last_remove_trap_ms

    if method == TRAP_SKILL:
        failures = 0
        while failures < MAX_REMOVE_TRAP_FAILURES:
            wait_for_remove_trap_cooldown()
            try: Journal.Clear()
            except: pass
            last_remove_trap_ms = now_ms()
            if not use_targeted(lambda:Player.UseSkill(REMOVE_TRAP_SKILL),chest):
                return False
            result = wait_journal(TRAP_SUCCESS + TRAP_NOT_PRESENT, TRAP_FAIL, 3500)
            if result == "success":
                return True
            if result == "hard":
                chest_out_of_range_message()
                return False
            if journal_has(ACTION_WAIT_MESSAGES):
                # A cooldown response is timing, not a genuine skill failure.
                # The timestamp above creates one full bounded fallback wait.
                continue
            failures += 1
            if failures >= MAX_REMOVE_TRAP_FAILURES:
                cm_msg("The chest remains trapped.", HUE_DISABLED)
                return False
            wait_after_remove_trap_failure()
        cm_msg("The chest remains trapped.", HUE_DISABLED)
        return False

    for _ in range(MAX_TRAP_ATTEMPTS):
        try: Journal.Clear()
        except: pass
        ok=cast_magic_untrap_targeted(chest)
        fail=SPELL_FAIL
        if not ok: return False
        result=wait_journal(TRAP_SUCCESS,fail,MAGIC_UNTRAP_CONFIRM_TIMEOUT)
        if result=="success": return True
        if result=="hard":
            chest_out_of_range_message()
            return False
        if journal_has(SPELL_CAST_CONFLICT_MESSAGES):
            cm_msg("Another action interrupted Magic Untrap. The chest remains closed. Try again when you are ready.", HUE_DISABLED)
            return False
        if journal_has(MAGIC_UNTRAP_WRONG_TARGET):
            cm_msg("Another action interrupted Magic Untrap. The chest remains closed. Try again when you are ready.", HUE_DISABLED)
            return False
        if journal_has(BANDAGE_TARGET_COLLISION):
            cm_msg("Another action interrupted Magic Untrap. The chest remains closed. Try again when you are ready.", HUE_DISABLED)
            return False
        if journal_has(ACTION_WAIT_MESSAGES):
            _wait_after_action()
            continue
        # UOAlive does not consistently provide an affirmative journal line for
        # Magic Untrap.  A clean confirmation window (no explicit spell failure)
        # is therefore the shard's successful result and may proceed to opening.
        if result=="timeout":
            return True
        Misc.Pause(1000)
    cm_msg("The trap remains armed.",HUE_DISABLED); return False


def _container_serial(value):
    try:
        if value is None: return 0
        if hasattr(value, "Serial"): return int(value.Serial)
        return int(value)
    except: return 0


def _item_container_serial(item):
    try: return _container_serial(item.Container)
    except: return 0


def _wait_after_action():
    # Razor Enhanced has no universal action-ready flag. A bounded pause is
    # safer than immediately repeating an action after the shard says to wait.
    Misc.Pause(ACTION_WAIT_DELAY)


def stable_chest_snapshot(chest):
    """Return a bounded, serial-stable view of the current chest contents."""
    started = time.time()
    previous_serials = None
    latest = []
    while (time.time() - started) * 1000 < SNAPSHOT_STABILITY_TIMEOUT:
        try:
            refreshed = Items.FindBySerial(chest.Serial)
            latest = list(refreshed.Contains or []) if refreshed is not None else []
        except:
            latest = []
        serials = tuple(sorted(int(item.Serial) for item in latest))
        elapsed = (time.time() - started) * 1000
        if elapsed >= SNAPSHOT_MIN_OBSERVE and serials == previous_serials:
            return latest
        previous_serials = serials
        Misc.Pause(SNAPSHOT_POLL_INTERVAL)
    return latest


def open_container(chest):
    """Use WaitForContents as the single authoritative opening request."""
    for attempt in range(MAX_OPEN_ATTEMPTS):
        if not chest_is_reachable(chest): return "hard", []
        try: Journal.Clear()
        except: pass
        try: Items.WaitForContents(chest.Serial, 3000)
        except: pass
        if journal_has(LOCKED_MESSAGES): return "locked", []
        if journal_has(HARD_STOP): return "hard", []
        if journal_has(ACTION_WAIT_MESSAGES):
            if attempt == 0: Misc.Pause(OPEN_RETRY_DELAY)
            continue
        try:
            refreshed = Items.FindBySerial(chest.Serial)
            if refreshed is not None and refreshed.Contains is not None:
                return "open", stable_chest_snapshot(chest)
        except: pass
        if attempt == 0: Misc.Pause(OPEN_RETRY_DELAY)
    return "failed", []

def open_with_repick(chest, description):
    """Open a picked chest, re-picking if the shard says it is locked."""
    for _ in range(3):
        state, contents=open_container(chest)
        if state=="open": return contents
        if state=="hard":
            chest_out_of_range_message()
            return None
        if state=="locked":
            if not pick_lock(chest): return None
            if not remove_trap(chest,dungeon_trap_method): return None
            continue
        break
    cm_msg("You cannot seem to open the chest.",HUE_DISABLED)
    return None


def over_weight():
    try: return Player.Weight>=Player.MaxWeight-WEIGHT_BUFFER
    except: return False


def move_item(item, destination):
    """Use the proven Dungeon Chest Pro item-movement timing."""
    for _ in range(2):
        try:
            amount = 1
            try:
                if item.Amount > 0:
                    amount = item.Amount
            except:
                amount = 1

            Items.Move(item, destination, amount)
            Misc.Pause(LOOT_MOVE_DELAY)
            return True
        except:
            Misc.Pause(650)

    return False


def play_rare_found():
    """Play the established rare alert and use the approved positive blue."""
    try:
        position = Player.Position
        Misc.PlaySound(
            RARE_FOUND_SOUND,
            position.X,
            position.Y,
            position.Z
        )
    except:
        pass

    cm_msg(
        "You uncover a treasure recorded in your journal.",
        RARE_FOUND_HUE
    )


def is_spell_scroll(item):
    try: return SPELL_SCROLL_MIN<=int(item.ItemID)<=SPELL_SCROLL_MAX
    except: return False


def magic_tier(item, prop_cache=None):
    text=item_text(item, prop_cache)
    names=["minor magic item","lesser magic item","greater magic item","major magic item","lesser artifact","greater artifact","major artifact","legendary artifact"]
    for i,name in enumerate(names):
        if name in text: return i
    return None


def chest_is_reachable(chest):
    try:
        refreshed = Items.FindBySerial(chest.Serial)
        if refreshed is None or refreshed.Deleted:
            return False
        return refreshed.DistanceTo(Mobiles.FindBySerial(Player.Serial)) <= 2
    except:
        try: return chest.DistanceTo(Mobiles.FindBySerial(Player.Serial)) <= 2
        except: return False


def is_recognized_equipment(item):
    """Fast mundane-equipment gate; does not request item properties."""
    try:
        layer = str(item.Layer or "").strip().lower()
        if layer and layer not in ("invalid", "none"):
            if layer in EQUIPMENT_LAYERS or any(token in layer for token in ("hand", "torso", "leg", "arm", "ring", "bracelet", "ear")):
                return True
    except: pass
    try:
        if bool(item.IsTwoHanded) or int(item.MaxDurability) > 0:
            return True
    except: pass
    name = item_name(item).lower()
    return any(word in name for word in EQUIPMENT_NAME_WORDS)


def standard_dungeon_category(item):
    try: iid = int(item.ItemID)
    except: return None
    if iid in LOCKPICK_IDS: return "Lockpicks"
    if iid in ARROW_IDS: return "Arrows"
    if iid in BOLT_IDS: return "Bolts"
    if iid in BLANK_SCROLL_IDS: return "Blank Scrolls"
    if iid in GEM_IDS: return "Gems"
    if iid in GOLD_IDS: return "Gold"
    if iid in POTION_IDS: return "Potions"
    if iid in REAGENT_IDS: return "Reagents"
    if iid in REFINEMENT_IDS: return "Refinements"
    if is_spell_scroll(item): return "Spell Scrolls"
    return None


def standard_category_enabled(category):
    return bool(dungeon_options.get(category, False))


def classify_dungeon_snapshot(contents, prop_cache=None):
    """Classify only configured loot; unmatched items are intentionally ignored."""
    rare, standard, magic = [], [], []
    for item in contents:
        if has_entry(rare_items, item):
            rare.append(item)
            continue
        category = standard_dungeon_category(item)
        if category:
            if standard_category_enabled(category): standard.append(item)
            continue
        if item_name(item).lower() == "wand":
            if dungeon_options["Wands"]:
                magic.append(item)
            continue
        if is_recognized_equipment(item):
            tier = magic_tier(item, prop_cache)
            if dungeon_options["Magic Items"] and tier is not None and tier >= dungeon_magic_tier_index:
                magic.append(item)
            continue
    return rare, standard, magic


def required_destination(label):
    if label == "rare": return shared_rare_item_bag
    if label == "standard": return dungeon_valuables_bag
    if label == "magic": return dungeon_magic_bag
    return None


def validate_loot_bag(serial, label):
    if not serial:
        cm_msg("Your {} can no longer be found.".format(label), HUE_DISABLED)
        return False
    try:
        bag = Items.FindBySerial(serial)
        if bag is None or not bag.IsContainer:
            raise Exception()
        if int(serial) != int(Player.Backpack.Serial) and int(bag.RootContainer) != int(Player.Backpack.Serial):
            raise Exception()
        return True
    except:
        cm_msg("Your {} can no longer be found.".format(label), HUE_DISABLED)
        return False


def next_item_fits(item):
    # Razor may report an entire stack's weight in item.Weight. Multiplying it
    # by item.Amount can double-count the stack and create false warnings.
    # Use the proven player-weight safety buffer before each move instead.
    return not over_weight()


def move_item_confirmed(item, chest, destination):
    for attempt in range(MAX_MOVE_ATTEMPTS):
        if not chest_is_reachable(chest): return False
        current = Items.FindBySerial(item.Serial)
        if current is None or _item_container_serial(current) != int(chest.Serial): return False
        try: Journal.Clear()
        except: pass
        try: Items.Move(current.Serial, int(destination), 0)
        except: return False
        Misc.Pause(MOVE_INTERVAL)
        current = Items.FindBySerial(item.Serial)
        if current is None or _item_container_serial(current) != int(chest.Serial):
            return True
        if journal_has(ACTION_WAIT_MESSAGES) and attempt == 0:
            continue
    return False


def move_classified_dungeon_loot(chest, contents, prop_cache):
    rare, standard, magic = classify_dungeon_snapshot(contents, prop_cache)
    groups = [
        ("rare", "Rare Item Bag", rare),
        ("standard", "Valuables Bag", standard),
        ("magic", "Magic Item Bag", magic)
    ]
    for key, label, items in groups:
        if items and not validate_loot_bag(required_destination(key), label):
            return False
    for key, label, items in groups:
        destination = required_destination(key)
        for item in items:
            if not next_item_fits(item):
                cm_msg("Your pack is nearly full.", HUE_DISABLED)
                return False
            if not move_item_confirmed(item, chest, destination):
                cm_msg("You cannot seem to take the item.", HUE_DISABLED)
                return False
            if key == "rare": play_rare_found()
    return True


def has_daily_rare(chest, contents, prop_cache):
    """Experimental post-loot scan; stop after the first Daily Rare match."""
    for item in contents:
        current = Items.FindBySerial(item.Serial)
        if current is None or _item_container_serial(current) != int(chest.Serial):
            continue
        if any("daily rare" in prop for prop in get_props(current, prop_cache)):
            return True
    return False


def loot_dungeon_snapshot(chest, contents):
    prop_cache = {}
    cm_msg("You begin searching the chest for valuable treasures.", HUE_BLUE)

    rare, standard, magic = classify_dungeon_snapshot(contents, prop_cache)
    moved_any = bool(rare or standard or magic)

    if not move_classified_dungeon_loot(chest, contents, prop_cache):
        return False

    # A bounded live verification prevents a partial first snapshot from
    # allowing selected Gold, recorded rares, or Magic Items to be skipped.
    for _ in range(FINAL_LOOT_PASSES):
        remaining = stable_chest_snapshot(chest)
        rare, standard, magic = classify_dungeon_snapshot(remaining, prop_cache)
        if not (rare or standard or magic):
            break
        moved_any = True
        if not move_classified_dungeon_loot(chest, remaining, prop_cache):
            return False

    remaining = stable_chest_snapshot(chest)
    rare, standard, magic = classify_dungeon_snapshot(remaining, prop_cache)
    if rare or standard or magic:
        cm_msg("You cannot seem to take the item.", HUE_DISABLED)
        return False
    if has_daily_rare(chest, remaining, prop_cache):
        cm_msg("Something unfamiliar catches your eye.", HUE_ORANGE)
    elif moved_any:
        cm_msg("You gather the spoils you came for.", HUE_ENABLED)
    return True


def dungeon_item_is_known(item):
    """Return True for every recognized Dungeon loot class, enabled or not.

    This intentionally ignores the player's Loot Type selections. A known item
    left behind by choice must never be reported as unfamiliar.
    """
    try:
        iid=int(item.ItemID)
    except:
        return False

    if has_entry(rare_items,item):
        return True
    if iid in LOCKPICK_IDS:
        return True
    if iid in GOLD_IDS or iid in GEM_IDS or iid in REAGENT_IDS:
        return True
    if iid in POTION_IDS or iid in BLANK_SCROLL_IDS or iid in ARROW_IDS or iid in BOLT_IDS:
        return True
    if iid in REFINEMENT_IDS or is_spell_scroll(item):
        return True
    if magic_tier(item) is not None:
        return True
    if item_name(item).lower()=="wand":
        return True
    return False


def dungeon_destination(item):
    iid=int(item.ItemID)
    if has_entry(rare_items,item): return shared_rare_item_bag or Player.Backpack.Serial
    selected=(
        (dungeon_options["Lockpicks"] and iid in LOCKPICK_IDS) or
        (dungeon_options["Gold"] and iid in GOLD_IDS) or
        (dungeon_options["Gems"] and iid in GEM_IDS) or
        (dungeon_options["Reagents"] and iid in REAGENT_IDS) or
        (dungeon_options["Potions"] and iid in POTION_IDS) or
        (dungeon_options["Blank Scrolls"] and iid in BLANK_SCROLL_IDS) or
        (dungeon_options["Arrows"] and iid in ARROW_IDS) or
        (dungeon_options["Bolts"] and iid in BOLT_IDS) or
        (dungeon_options["Refinements"] and iid in REFINEMENT_IDS) or
        (dungeon_options["Spell Scrolls"] and is_spell_scroll(item))
    )
    if selected: return dungeon_valuables_bag or Player.Backpack.Serial
    if dungeon_options["Wands"] and item_name(item).lower()=="wand":
        return dungeon_magic_bag or Player.Backpack.Serial
    if dungeon_options["Magic Items"]:
        tier=magic_tier(item)
        if tier is not None and tier>=dungeon_magic_tier_index: return dungeon_magic_bag or Player.Backpack.Serial
    return None


def kotl_category(item):
    iid = int(item.ItemID)

    # Kotl artifacts use the same fast hue-only detection approach as the
    # proven Dungeon Chest Pro logic. Do not request names or properties here.
    try:
        if int(item.Hue) == KOTL_ARTIFACT_HUE:
            return "Kotl Artifacts"
    except:
        pass

    if iid in GOLD_IDS:
        return "Gold"
    if iid in GEM_IDS:
        return "Gems"
    if iid == STASIS_POWER_CORE_ID:
        return "Stasis Chamber Power Core"

    # Named Kotl items still require identity checks until all graphics are
    # confirmed. Artifact detection itself remains strictly hue-only.
    text = item_text(item)
    if "stasis chamber power core" in text or "power core" in text:
        return "Stasis Chamber Power Core"
    if "card of semidar" in text or "cards of semidar" in text:
        return "Cards of Semidar"
    if "inoperative automaton head" in text or "automaton head" in text:
        return "Inoperative Automaton Head"
    if "rare book" in text or "book" in text:
        return "Rare Books"
    return None


def kotl_destination(item):
    category=kotl_category(item)
    if category=="Kotl Artifacts": return Player.Backpack.Serial
    if not category or not kotl_options.get(category,False): return None
    if category in ("Gold","Gems"): return kotl_valuables_bag or Player.Backpack.Serial
    return kotl_item_bag or Player.Backpack.Serial


def shop_category(item):
    if has_entry(rare_items,item): return "Rare Items"
    for e in shop_items:
        if entry_matches(e,item): return normalize_shop_category(e.get("category") or infer_shop_category(item))
    # Generic categories can be recognized without learning.
    return infer_shop_category(item)


def shop_is_eligible(item):
    if has_entry(rare_items,item): return True
    if has_entry(shop_items,item): return bool(shop_options.get(shop_category(item),False))
    return False


def loot_container(chest,destination_fn,unknown_warning=False):
    """Use the original Dungeon Chest Pro move loop without shared-wrapper timing."""
    cm_msg("You begin searching the chest for valuable treasures.", HUE_BLUE)

    moved_any = True

    while moved_any:
        moved_any = False

        try:
            Items.WaitForContents(chest, 3000)
            Misc.Pause(250)
            chest = Items.FindBySerial(chest.Serial)
        except:
            pass

        try:
            if chest is None or chest.Contains is None:
                cm_msg("You find nothing else of value.", HUE_ENABLED)
                return
            contents = list(chest.Contains)
        except:
            cm_msg("You find nothing else of value.", HUE_ENABLED)
            return

        for item in contents:
            if over_weight():
                cm_msg("Your pack is nearly full.", HUE_DISABLED)
                return

            destination = destination_fn(item)

            if destination:
                is_recorded_rare = has_entry(rare_items, item)

                if move_item(item, destination):
                    if is_recorded_rare:
                        play_rare_found()

                    moved_any = True
                    Misc.Pause(250)
                    break

    cm_msg("You find nothing else of value.", HUE_ENABLED)

    if unknown_warning:
        try:
            remaining = list(Items.FindBySerial(chest.Serial).Contains or [])
            if any(not dungeon_item_is_known(item) for item in remaining):
                cm_msg("Something unfamiliar catches your eye.", HUE_ORANGE)
        except:
            pass

def target_container(prompt):
    item=request_item(prompt)
    if not item: cm_msg("No chest was selected.",HUE_DISABLED); return None
    return item


def run_dungeon():
    chest=target_container("")
    if not chest: return
    if not pick_lock(chest): return
    if not remove_trap(chest,dungeon_trap_method): return
    if dungeon_trap_method==TRAP_MAGIC and journal_has(MAGIC_UNTRAP_WRONG_TARGET):
        cm_msg("Another action interrupted Magic Untrap. The chest remains closed. Try again when you are ready.",HUE_DISABLED)
        return
    if dungeon_trap_method==TRAP_MAGIC and journal_has(BANDAGE_TARGET_COLLISION):
        cm_msg("Another action interrupted Magic Untrap. The chest remains closed. Try again when you are ready.",HUE_DISABLED)
        return
    contents=open_with_repick(chest,"chest")
    if contents is None: return
    if loot_enabled: loot_dungeon_snapshot(chest,contents)


def run_kotl():
    case=target_container("Target the Kotl Regal Case.")
    if not case: return
    if not pick_lock(case): return
    if not remove_trap(case,kotl_trap_method): return
    if not open_with_repick(case,"Regal Case"): return
    if loot_enabled: loot_container(case,kotl_destination,False)


def _shop_candidates(chest):
    """Return a fresh prioritized list of Shop items currently eligible to steal."""
    try:
        Items.WaitForContents(chest, 2000)
        refreshed = Items.FindBySerial(chest.Serial)
        contents = list(refreshed.Contains or [])
    except:
        contents = []

    rares = [item for item in contents if has_entry(rare_items, item)]
    learned = [
        item for item in contents
        if not has_entry(rare_items, item) and shop_is_eligible(item)
    ]
    return rares + learned


def _shop_destination(item):
    if has_entry(rare_items, item):
        return shared_rare_item_bag or Player.Backpack.Serial
    if shop_category(item) == "Gems":
        return shop_valuables_bag or Player.Backpack.Serial
    return shop_item_bag or Player.Backpack.Serial


def run_shop_target():
    global current_shop_chest, shop_steal_ready_at
    chest = target_container("")
    if not chest:
        return
    if not pick_lock(chest):
        return
    # Shop chests always use Remove Trap.
    if not remove_trap(chest, TRAP_SKILL):
        return
    if not open_with_repick(chest, "shop chest"):
        return

    current_shop_chest = chest.Serial
    candidates = _shop_candidates(chest)
    if candidates:
        shop_steal_ready_at = time.time() + SHOP_STEAL_COOLDOWN_SECONDS
        cm_msg(
            "You wait for the shop owner to turn their back before stealing the item.",
            HUE_INFO
        )
    else:
        shop_steal_ready_at = 0.0
        cm_msg("You find nothing else worth risking discovery for.", HUE_INFO)


def steal_next():
    global current_shop_chest, shop_steal_ready_at
    if not current_shop_chest:
        cm_msg("Target a shop chest before choosing an item to steal.", HUE_DISABLED)
        return

    if time.time() < shop_steal_ready_at:
        cm_msg("You are not yet ready to make another attempt.", HUE_DISABLED)
        return

    try:
        chest = Items.FindBySerial(current_shop_chest)
    except:
        chest = None
    if not chest:
        cm_msg("The shop chest can no longer be found.", HUE_DISABLED)
        current_shop_chest = None
        shop_steal_ready_at = 0.0
        return

    candidates = _shop_candidates(chest)
    if not candidates:
        shop_steal_ready_at = 0.0
        cm_msg("You find nothing else worth risking discovery for.", HUE_INFO)
        return

    item = candidates[0]
    is_recorded_rare = has_entry(rare_items, item)

    try:
        Journal.Clear()
    except:
        pass

    if not use_targeted(lambda: Player.UseSkill(STEALING_SKILL), item):
        cm_msg("You cannot attempt to steal that item.", HUE_DISABLED)
        return

    result = wait_journal(STEAL_SUCCESS, STEAL_FAIL, 5000)
    if result == "success":
        # Allow the stolen item to arrive in the backpack before sorting it.
        Misc.Pause(700)
        try:
            stolen = Items.FindBySerial(item.Serial)
        except:
            stolen = None

        if stolen:
            destination = _shop_destination(stolen)
            if destination != Player.Backpack.Serial:
                move_item(stolen, destination)
            if is_recorded_rare:
                play_rare_found()

        # A fresh post-steal scan controls both the cooldown and journal text.
        remaining = _shop_candidates(chest)
        if remaining:
            shop_steal_ready_at = time.time() + SHOP_STEAL_COOLDOWN_SECONDS
            cm_msg(
                "You wait for another opportunity to steal the next item.",
                HUE_INFO
            )
        else:
            shop_steal_ready_at = 0.0
            cm_msg("You find nothing else worth risking discovery for.", HUE_INFO)

    elif result == "hard":
        cm_msg("That item lies beyond your reach.", HUE_DISABLED)
    elif journal_has(ACTION_WAIT_MESSAGES):
        cm_msg("You are not yet ready to make another attempt.", HUE_DISABLED)
    else:
        cm_msg(
            "Your attempt draws too much attention, and you withdraw your hand.",
            HUE_DISABLED
        )


# Override list display for persisted entries.
def get_active_list():
    if active_list_name == "rare":
        return rare_items, "Rare Dungeon Items"
    return shop_items, "Shop Items"


def dungeon_rare_count_message():
    count = len(rare_items)
    if count == 0:
        text = "Your Rare Dungeon Items list contains no recorded treasures."
    elif count == 1:
        text = "Your Rare Dungeon Items list contains 1 recorded treasure."
    else:
        text = "Your Rare Dungeon Items list contains {} recorded treasures.".format(count)
    cm_msg(text, HUE_JOURNAL_OPTION)


def draw_list_gump():
    global active_list_page

    close_all_test_gumps()
    entries, title = get_active_list()

    page_count = max(1, int((len(entries) + LIST_ITEMS_PER_PAGE - 1) / LIST_ITEMS_PER_PAGE))
    active_list_page = max(0, min(active_list_page, page_count - 1))

    start_index = active_list_page * LIST_ITEMS_PER_PAGE
    visible_entries = entries[start_index:start_index + LIST_ITEMS_PER_PAGE]

    width = DL["list_width"]
    height = DL["list_height"]
    footer_y = DL["list_footer_y"]

    gd = Gumps.CreateGump(True)
    Gumps.AddPage(gd, 0)

    add_release_background(gd, width, height, [
        (DL["list_main_x"], DL["list_main_y"], DL["list_main_w"], DL["list_main_h"], INNER_ART),
        (DL["list_footer_x"], footer_y, DL["list_footer_w"], DL["list_footer_h"], INNER_ART)])

    add_chestloot_title(gd, 10, 10, width - 20, 26)
    add_centered_title(gd, width, DL["list_title_y"], title)

    if not visible_entries:
        Gumps.AddLabel(gd, DL["list_empty_x"], DL["list_empty_y"], HUE_DISABLED, "No entries recorded.")
    else:
        for page_index, entry in enumerate(visible_entries):
            absolute_index = start_index + page_index
            offset = page_index * DL["list_row_spacing"]
            Gumps.AddLabel(gd, DL["list_row_label_x"], DL["list_row_label_y"] + offset, HUE_TEXT, entry.get("name", "Unknown Item"))
            add_art_button(
                gd,
                DL["list_row_button_x"],
                DL["list_row_button_y"] + offset,
                CLOSE_BUTTON_NORMAL,
                CLOSE_BUTTON_PRESSED,
                BTN_LIST_REMOVE_BASE + absolute_index
            )
            Gumps.AddLabel(gd, DL["list_remove_label_x"], DL["list_remove_label_y"] + offset, HUE_DISABLED, "Remove")

    page_text = "Page {} of {}".format(active_list_page + 1, page_count)
    Gumps.AddLabel(gd, DL["list_page_x"], DL["list_page_y"], HUE_TEXT, page_text)

    if active_list_page > 0:
        add_art_button(gd, DL["list_prev_button_x"], DL["list_prev_button_y"], LEFT_ARROW_NORMAL, LEFT_ARROW_PRESSED, BTN_LIST_PREV)
        Gumps.AddLabel(gd, DL["list_prev_label_x"], DL["list_prev_label_y"], HUE_GOLD, "Prev")

    add_art_button(gd, DL["list_back_button_x"], DL["list_back_button_y"], LEFT_ARROW_NORMAL, LEFT_ARROW_PRESSED, BTN_LIST_BACK)
    Gumps.AddLabel(gd, DL["list_back_label_x"], DL["list_back_label_y"], HUE_GOLD, "Back")

    if active_list_page < page_count - 1:
        add_art_button(gd, DL["list_next_button_x"], DL["list_next_button_y"], ACTION_BUTTON_NORMAL, ACTION_BUTTON_PRESSED, BTN_LIST_NEXT)
        Gumps.AddLabel(gd, DL["list_next_label_x"], DL["list_next_label_y"], HUE_GOLD, "Next")

    Gumps.SendGump(
        LIST_GUMP_ID,
        Player.Serial,
        GUMP_X,
        GUMP_Y,
        gd.gumpDefinition,
        gd.gumpStrings
    )


# Override option handlers to save every change.
def handle_bag_target(button_id): set_bag(button_id)

_old_dungeon=_legacy_handle_dungeon_option
_old_kotl=_legacy_handle_kotl_option
_old_shop=_legacy_handle_shop_option

def handle_dungeon_option(button_id): _old_dungeon(button_id); save_all()
def handle_kotl_option(button_id): _old_kotl(button_id); save_all()
def handle_shop_option(button_id): _old_shop(button_id); save_all()


def handle_main_screen():
    global current_screen,loot_enabled,gump_closed
    button_id=get_button_id(MAIN_GUMP_ID)
    if button_id is None:return
    if button_id==0:gump_closed=True
    elif button_id==BTN_PROFILE_SELECT:
        Misc.SetSharedValue("ChestLootPro_ReturnToModeSelection",1)
        gump_closed=True
    elif button_id==BTN_TOGGLE_LOOT:loot_enabled=not loot_enabled;save_all();draw_main_gump()
    elif button_id==BTN_OPEN_OPTIONS:current_screen="options";draw_options_gump()
    elif button_id==BTN_LEARN_RARE and active_profile in (PROFILE_DUNGEON,PROFILE_SHOP):learn_rare();draw_main_gump()
    elif button_id==BTN_LEARN_SHOP_ITEM and active_profile==PROFILE_SHOP:learn_shop();draw_main_gump()
    elif button_id==BTN_STEAL_ITEM and active_profile==PROFILE_SHOP:steal_next();draw_main_gump()
    elif button_id==BTN_TARGET:
        if active_profile==PROFILE_DUNGEON:run_dungeon()
        elif active_profile==PROFILE_KOTL:run_kotl()
        else:run_shop_target()
        draw_main_gump()


def handle_profile_screen():
    global active_profile,current_screen,gump_closed
    button_id=get_button_id(PROFILE_GUMP_ID)
    if button_id is None:return
    if button_id==0:gump_closed=True
    elif button_id in (BTN_PROFILE_DUNGEON,BTN_PROFILE_KOTL,BTN_PROFILE_SHOP):
        active_profile={BTN_PROFILE_DUNGEON:PROFILE_DUNGEON,BTN_PROFILE_KOTL:PROFILE_KOTL,BTN_PROFILE_SHOP:PROFILE_SHOP}[button_id]
        current_screen="main";save_all();draw_main_gump()


def handle_list_screen():
    global current_screen,gump_closed,active_list_page
    button_id=get_button_id(LIST_GUMP_ID)
    if button_id is None:return
    if button_id==0:current_screen="options";active_list_page=0;draw_options_gump();return
    if button_id==BTN_LIST_BACK:current_screen="options";draw_options_gump();return
    if button_id==BTN_LIST_PREV:active_list_page-=1;draw_list_gump();return
    if button_id==BTN_LIST_NEXT:active_list_page+=1;draw_list_gump();return
    if button_id>=BTN_LIST_REMOVE_BASE:
        entries,title=get_active_list();index=button_id-BTN_LIST_REMOVE_BASE
        if 0<=index<len(entries):
            removed=entries.pop(index);cm_msg("{} has been removed from your Rare Dungeon Items list.".format(removed.get("name","Unknown Item")),HUE_JOURNAL_OPTION);save_all()
        draw_list_gump()


def run():
    global gump_closed,current_screen,active_profile
    load_all(); active_profile=PROFILE_DUNGEON; close_all_test_gumps(); gump_closed=False; current_screen="main"
    dungeon_rare_count_message()
    draw_main_gump()
    while not gump_closed:
        if current_screen=="main":handle_main_screen()
        elif current_screen=="profile":handle_profile_screen()
        elif current_screen=="options":handle_options_screen()
        elif current_screen=="list":handle_list_screen()
        Misc.Pause(50)
    save_all();close_all_test_gumps()


def run_mode():
    run()
