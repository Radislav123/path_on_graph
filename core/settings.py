class Settings:
    instance: "Settings" = None

    def __new__(cls, *args, **kwargs) -> "Settings":
        if cls.instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls.instance = instance
        else:
            instance = cls.instance

        return instance

    def __init__(self) -> None:
        if hasattr(self, "inited"):
            return

        self.APP_NAME = "path_on_graph"

        self.RESOURCES_FOLDER = "resources"
        self.STYLESHEET_FOLDER = f"{self.RESOURCES_FOLDER}/stylesheets"

        self.inited = True

    # noinspection PyPep8Naming
    def PRETTY_APP_NAME(self) -> str:
        return self.APP_NAME.capitalize().replace('_', ' ')
