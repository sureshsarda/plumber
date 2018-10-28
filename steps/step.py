class Step:

    def __call__(self, *args, **kwargs):
        raise NotImplementedError('Unknwon step type')

    def execute(self, **kwargs):
        raise NotImplementedError('Unknwon step type')


class Echo(Step):

    def execute(self, message):
        print(message)

    def __call__(self, message):
        print(message)
