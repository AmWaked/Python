import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_init(self):
        self.assertIs((self.__str__()), 'Power = False, Channel = 0, Volume = 0')

    def test_power(self):
        self.assertTrue(self.tv.power())
        self.assertFalse(self.tv.power())

    def test_mute(self):
        self.tv.power()
        self.assertTrue(self.tv.mute())
        self.assertFalse(self.tv.mute())
        self.tv.power()
        self.assertTrue(self.tv.mute)
        self.assertFalse(self.tv.mute())

    def test_channel_up(self):
        self.tv.power()
        self.assertEqual(self.tv.channel_up(), 1)
        self.assertEqual(self.tv.channel_up(), 2)
        self.assertEqual(self.tv.channel_up(), 3)
        self.assertEqual(self.tv.channel_up(), 0)
        self.tv.power()
        self.assertEqual(self.tv.channel_up(), 0)
        self.assertEqual(self.tv.channel_up(), 0)
        self.assertEqual(self.tv.channel_up(), 0)
        self.assertEqual(self.tv.channel_up(), 0)

    def test_channel_down(self):
        self.tv.power()
        self.assertEqual(self.tv.channel_down(), 3)
        self.assertEqual(self.tv.channel_down(), 2)
        self.assertEqual(self.tv.channel_down(), 1)
        self.assertEqual(self.tv.channel_down(), 0)
        self.tv.power()
        self.assertEqual(self.tv.channel_down(), 0)
        self.assertEqual(self.tv.channel_down(), 0)
        self.assertEqual(self.tv.channel_down(), 0)
        self.assertEqual(self.tv.channel_down(), 0)

    def test_volume_up(self):
        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.volume_up(), 1)
        self.assertEqual(self.tv.volume_up(), 2)
        self.assertEqual(self.tv.volume_up(), 2)
        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.volume_up(), 2)
        self.assertEqual(self.tv.volume_up(), 2)

    def test_volume_down(self):
        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.volume_down(), 0)
        self.assertEqual(self.tv.volume_down(), 0)
        self.assertEqual(self.tv.volume_down(), 0)
        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.volume_down(), 0)
        self.assertEqual(self.tv.volume_down(), 0)




