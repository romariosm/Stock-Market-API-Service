class ParameterAPI:
    def __init__(self, name):
        self.__name = name

    @staticmethod
    def is_valid(value):
        pass

    @property
    def get_name(self):
        return self.__name


class IntegerParameter(ParameterAPI):
    """
    Integer parameter service API
    """

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def is_valid(value):
        """
        validates parameter sent is int type
        """
        return isinstance(value, int)


class StringParameter(ParameterAPI):
    """
    String parameter service API
    """

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def is_valid(value):
        """
        Validates parameter sent is string type
        """
        return isinstance(value, str)
