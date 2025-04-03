import unittest
import pandas as pd
from datetime import datetime

class TestReconciliationLogic(unittest.TestCase):

    def setUp(self):
        self.today = pd.to_datetime(datetime.today().date())
        self.mock_rights = pd.DataFrame({
            "track_id": ["T0001", "T0002"],
            "owner_name": ["Label A", "Label B"],
            "valid_from": [self.today.replace(year=self.today.year - 2)] * 2,
            "valid_to": [self.today.replace(year=self.today.year - 1), self.today.replace(year=self.today.year + 1)]
        })

    def test_expired_rights_detection(self):
        expired = self.mock_rights[self.mock_rights["valid_to"] < self.today]
        self.assertEqual(len(expired), 1)

if __name__ == '__main__':
    unittest.main()
