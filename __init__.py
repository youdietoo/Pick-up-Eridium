from unrealsdk import find_all
from mods_base import build_mod


ERIDIUM_DEFINITIONS = (
    "EridiumStick",
    "EridiumBar",
)


def modify_eridium():
    try:
        for definition in find_all("WillowGame.UsableItemDefinition"):
            try:
                if str(definition.Name) not in ERIDIUM_DEFINITIONS:
                    continue

                definition.bAutomaticallyPickup = True

            except Exception as e:
                print(f"[EridiumPickup] Failed modifying {definition}: {e}")

    except Exception as e:
        print(f"[EridiumPickup] Failed finding Eridium definitions: {e}")


try:
    modify_eridium()
except Exception as e:
    print(f"[EridiumPickup] Unexpected error: {e}")


build_mod()