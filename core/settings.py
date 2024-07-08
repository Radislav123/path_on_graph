class Settings:
    instance: "Settings" = None

    def __new__(cls, *args, **kwargs) -> "Settings":
        if cls.instance is None:
            instance = super().__new__(cls, *args, **kwargs)
        else:
            instance = cls.instance

        return instance

    def __init__(self) -> None:
        self.APP_NAME = "path_on_graph"

    # noinspection PyPep8Naming
    def PRETTY_APP_NAME(self) -> str:
        return self.APP_NAME.capitalize().replace('_', ' ')
