# class Play(object):
#
#     def __init__(cls):
#         print("Inside init")
#         return super().__init__()
#
#     def __new__(cls, *args, **kwargs):
#         print("Inside New")
#         return super().__new__(cls, *args, **kwargs)
#
#     # def __call__(cls, *args, **kwargs):
#     #     print("Inside Call")
#     #     return super().__call__(*args, **kwargs)
#     #
#
# class SubPlay(metaclass=Play):
#     pass
#
# playobj = SubPlay()

class Play(object):

    def __init__(self):
        print("Inside init")
        return super().__init__()

    def __new__(cls, *args, **kwargs):
        print("Inside New")
        return super().__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("Inside Call")
        return super().__call__(*args, **kwargs)


a = Play()
a()