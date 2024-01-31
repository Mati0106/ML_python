def predict_output_1(list_):
    result = [x * 2 for x in list_ if x % 2 == 0]
    return result


numbers = [1, 2, 3, 4, 5]
output_5 = predict_output_1(numbers)




def predict_output_2():
    text = "Hello, World!"
    result = text[-2:]
    return result


output_2 = predict_output_2()







def predict_output_3(list_):
    len_ = len(list_)
    list_[1:-1] = [0] * (len_ - 2)

    return list_


output_3 = predict_output_3([2, 3, 4, 5, 6])







def predict_output_4(callable_: callable, logger, *args):
    logger.info(f"Calling {callable_.__name__} with {args}")
    return callable_(*args)


import logging
logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger("Root")


def operation(a, b):
    return a ** b / 10 // 1


output_4 = predict_output_4(operation, logger, 2, 4)







def predict_output_dicts(dict1, dict2):
    dict3 = {}
    for key in dict1:
        dict3[key] = dict1[key] + dict2.get(key, 0)
    for key in dict2:
        if key not in dict3:
            dict3[key] = dict2[key]

    return sum(dict3.values())



dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 =         {'b': 2, 'c': 3, 'd': 4}
output_dicts =  predict_output_dicts(dict1, dict2)




from abc import ABC, abstractmethod
class BaseValidator(ABC):

    @abstractmethod
    def validate(self, str_: str) -> bool:
        ...


class Validator(BaseValidator):
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, str_: str):
        return self.validate(str_)

    def validate(self, str_: str):
        if not isinstance(str_, str):
            raise ValueError("Input must be a string")

        if len(str_) < self.min_length:
            return False

        if len(str_) > self.max_length:
            return False

        return True


fns = (str.lower,
       str.capitalize,
       lambda x: f'<<{x}>>',
       Validator(5, 10),
       )


def predict_output_6(*functions):
    def _predict_output_6(x):
        result = x
        print(x)
        for f in functions:
            print(f)
            result = f(result)
        return result
    return _predict_output_6


output_6 = predict_output_6(*fns)("HELLO")


import time
from contextlib import contextmanager


# In this example, predict what will be printed to the console.

@contextmanager
def ctx_mngr_example(label: str):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start}')


def fn(raise_error=True):
    time.sleep(1)
    if raise_error:
        raise RuntimeError("Something went wrong")
    time.sleep(1)


with ctx_mngr_example('Sleeping 1'):
    fn(True)
    with ctx_mngr_example('Sleeping 2'):
        fn(False)