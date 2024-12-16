from dataclasses import dataclass


@dataclass
class Note:
    note_id: int
    note_fields: str
    deck_id: int
    deck_name: str
    deck_name: str

    @property
    def german_word(self):
        fields = self.note_fields.split('\x1f')
        return fields[1]

    @property
    def german_sentence(self):
        fields = self.note_fields.split('\x1f')
        return fields[4]


NOTE_QUERY = """
SELECT n.id AS note_id, n.flds AS note_fields,
       d.name AS deck_name, d.id as deck_id
FROM notes n
JOIN cards c ON n.id = c.nid
JOIN decks d ON c.did = d.id
WHERE d.id = 1695978227665;  --frequency deck
"""
