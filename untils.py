from datetime import datetime


def logger(some_function):
    def new_function(*args, **kwargs):
        start = datetime.now()
        result = some_function(*args, **kwargs)
        with open('logs.txt', 'a', encoding='utf-8') as l:
           l.write(f"""
           Вызвана функция {some_function.__name__}. Время вызова: {start}, время окончания: {datetime.now()}.
           Время работы: {datetime.now() - start}
                     """)
        return result

    return new_function


def logger(path):
    def logger_(some_function):
        def new_function(*args, **kwargs):
            start = datetime.now()
            result = some_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log:
               log.write(f"""
               Вызвана функция {some_function.__name__}  c аргументами {args} и {kwargs}. 
               Время вызова: {start}, время окончания: {datetime.now()}.
               Время работы: {datetime.now() - start}
                         """)
            return result

        return new_function
    return logger_

