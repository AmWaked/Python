class Television:
    """

    A class representing details for a television object.

    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=0, channel=0) -> None:
        """
        method to set default values for the television object
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        """

        method to switch tv on or off

        """
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False

    def mute(self) -> None:
        """
        method to mute or unmute the tv
        
        """
        if self.__status is True:
            saved_volume = self.__volume
            if self.__muted is False:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            elif self.__muted is True:
                self.__muted = False
                self.__volume = saved_volume

    def channel_up(self) -> None:
        """

        method to change tv channel upwards by 1
 
        """
        if self.__status is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel != Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1

    def channel_down(self) -> None:
        """

        method to change tv channel downwards by 1
   
        """
        if self.__status is True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel != Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1

    def volume_up(self) -> None:
        """

        method to change tv volume upwards by 1

        """
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume = self.__volume + 1
     

    def volume_down(self) -> None:
        """

        method to change tv volume downwards by 1

        """
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """

        method to display current tv values

        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'