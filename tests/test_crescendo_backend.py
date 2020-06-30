import crescendobackend
from django.test import TestCase


class VersionTestCase(TestCase):
    def test_version(self) -> None:
        self.assertEqual(crescendobackend.__version__, '0.1.0')
