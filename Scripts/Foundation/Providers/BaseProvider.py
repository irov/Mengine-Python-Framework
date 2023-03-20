class BaseProvider(object):
    s_name = None
    s_methods = {}
    s_allowed_methods = []

    @classmethod
    def _isMethodsValid(cls, methods):
        is_valid = True

        for name, method in methods.items():
            if name not in cls.s_allowed_methods:
                Trace.log("Provider", 0, "Unknown method {!r} ({})".format(name, method))
                is_valid = False

        return is_valid

    @classmethod
    def setProvider(cls, name, methods):
        if _DEVELOPMENT is True:
            if isinstance(methods, dict) is False:
                Trace.log("Provider", 0, "Wrong type {} must be dict".format(type(methods)))
                return False

            if cls._isMethodsValid(methods) is False:
                return False

        cls.s_methods = methods
        cls.s_name = name

        return True

    @classmethod
    def setDevProvider(cls):
        if _DEVELOPMENT is False:
            return
        cls._setDevProvider()

    @staticmethod
    def _setDevProvider():
        pass

    @classmethod
    def getName(cls):
        return cls.s_name

    @classmethod
    def removeProvider(cls):
        cls.s_name = None
        cls.s_methods = {}

    @classmethod
    def _call(cls, name, *args, **kwargs):
        fn = cls.s_methods.get(name)

        if fn is None:
            Trace.log("Provider", 1, "Not found method {}".format(name))
            return False

        return fn(*args, **kwargs)
