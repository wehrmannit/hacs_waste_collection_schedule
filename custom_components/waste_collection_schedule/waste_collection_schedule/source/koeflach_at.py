from datetime import datetime
import requests
from waste_collection_schedule import Collection
from waste_collection_schedule.service.ICS import ICS


TITLE = "KOEFLACH"
DESCRIPTION = "Source for Koeflach."
URL = "https://koeflach.at"
TEST_CASES = {
    "Köfach - Ackerweg": {
        "street": "Ackerweg",
        "mfh": False,
    },
    "Köfach - Am Wald": {
        "street": "Am Wald",
        "mfh": True,
    },
    "Köfach - Lagerstraße": {
        "street": "Lagerstraße",
        "mfh": True,
    }

}

COUNTRY = "at"

API_URL = 'https://koeflach-ics-e15792009a61.herokuapp.com'

ICON_MAP = {
    "Restmüll": "mdi:trash-can",
    "Restmüll Zwischenabholung": "mdi:trash-can",
    "Bio-Tonne": "mdi:leaf",
    "Bio-Tonne Reinigung": "mdi:leaf",
    "Papiertonne": "mdi:package-variant",
    "Papier": "mdi:package-variant",
    "Papiertonne Zwischenabholung": "mdi:package-variant",
    "Leichtverpackung": "mdi:recycle",
}


class Source:
    def __init__(self, street: str, mfh: bool):
        self._street: str = street
        self._mfh: bool = mfh
        self._ics = ICS()

    def fetch(self):

        full_url = API_URL + "?street=" + \
            str(self._street) + "&mfh=" + str(self._mfh).lower()

        r = requests.get(full_url)
        r.raise_for_status()

        # parse ics file
        r.encoding = "utf-8"
        dates = self._ics.convert(r.text)

        entries = []

        for d in dates:
            entries.append(
                Collection(
                    date=d[0],  # Collection date
                    t=d[1],  # Collection type
                    icon=ICON_MAP.get(d[1]),  # Collection icon
                )
            )

        return entries
