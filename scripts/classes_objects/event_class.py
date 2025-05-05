class ButtonEvent:
    def __init__(self, name, **kwargs):
        self.__name = name
        # for i in kwargs.items():
        #     if not isinstance(i, int) and not isinstance(i, str):
        #         raise TypeError('event got not str and not int parameter')
        self.__parameter = kwargs

    @property
    def name(self):
        return self.__name

    @property
    def parameter(self):
        return self.__parameter