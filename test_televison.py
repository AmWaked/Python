import pytest
from television import Television

class Test:

    def setup_method(self):
        self.tv = Television

    def test_init():
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power():
        self.tv.power()
        assert self.tv.__status == True
        tv.power()
        assert self.tv.__status == False

    def test_mute():
        self.tv.power()
        self.tv.mute()
        assert self.tv.__muted == True
        self.tv.mute()
        assert self.tv.__muted == False

    def test_channel_up():
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__channel == 1
        self.tv.channel_up()
        assert self.tv.__channel == 2
        self.tv.channel_up()
        assert self.tv.__channel == 3
        self.tv.channel_up()
        assert self.tv.__channel == 0
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__channel == 0
        self.tv.channel_up()
        assert self.tv.__channel == 0

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__channel == 3
        self.tv.channel_down()
        assert self.tv.__channel == 2
        self.tv.channel_down()
        assert self.tv.__channel == 1
        self.tv.channel_down()
        assert self.tv.__channel == 0
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__channel == 0
        self.tv.channel_down()
        assert self.tv.__channel == 0

    def test_volume_up(self):
        self.tv.power()
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__volume == 2
        self.tv.volume_up()
        assert self.tv.__volume == 2
        self.tv.volume_up()
        assert self.tv.__volume == 2
        self.tv.power()
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__volume == 2
        self.tv.volume_up()
        assert self.tv.__volume == 2

    def test_volume_down(self):
        self.tv.power()
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__volume == 1
        self.tv.volume_down()
        assert self.tv.__volume == 0
        self.tv.volume_down()
        assert self.tv.__volume == 0
        self.tv.power()
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__volume == 0
        self.tv.volume_down()
        assert self.tv.__volume == 0




