import json
import tempfile
import unittest
from pathlib import Path

import cyberhelper


class LocalPersistenceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        root = Path(self.temp_dir.name)

        self.original_favorites_file = cyberhelper.FAVORITES_FILE
        self.original_settings_file = cyberhelper.SETTINGS_FILE

        cyberhelper.FAVORITES_FILE = root / "favorites.json"
        cyberhelper.SETTINGS_FILE = root / "settings.json"

    def tearDown(self):
        cyberhelper.FAVORITES_FILE = self.original_favorites_file
        cyberhelper.SETTINGS_FILE = self.original_settings_file
        self.temp_dir.cleanup()

    def test_save_and_load_favorites_round_trip(self):
        favorites = [
            {"title": "SQL injection notes", "content": "Example defensive notes"},
            {"title": "Network checklist", "content": "Review firewall rules"},
        ]

        cyberhelper.save_favorites(favorites)

        self.assertTrue(cyberhelper.FAVORITES_FILE.exists())
        self.assertEqual(cyberhelper.load_favorites(), favorites)

    def test_load_favorites_returns_empty_list_for_invalid_json(self):
        cyberhelper.FAVORITES_FILE.write_text("{not-valid-json", encoding="utf-8")

        self.assertEqual(cyberhelper.load_favorites(), [])

    def test_save_api_key_preserves_existing_settings(self):
        existing = {
            "system_prompt": "custom prompt",
            "theme": "nord",
        }
        cyberhelper.SETTINGS_FILE.write_text(
            json.dumps(existing),
            encoding="utf-8",
        )

        cyberhelper.save_api_key("test-placeholder-key")

        saved = json.loads(cyberhelper.SETTINGS_FILE.read_text(encoding="utf-8"))
        self.assertEqual(saved["api_key"], "test-placeholder-key")
        self.assertEqual(saved["system_prompt"], "custom prompt")
        self.assertEqual(saved["theme"], "nord")

    def test_save_api_key_creates_settings_file_when_missing(self):
        self.assertFalse(cyberhelper.SETTINGS_FILE.exists())

        cyberhelper.save_api_key("test-placeholder-key")

        saved = json.loads(cyberhelper.SETTINGS_FILE.read_text(encoding="utf-8"))
        self.assertEqual(saved, {"api_key": "test-placeholder-key"})


if __name__ == "__main__":
    unittest.main()
