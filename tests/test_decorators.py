from src.decorators import log


@log(filename="mylog.txt")
def func(x: int | str, y: int | str) -> int:
    try:
        return int(x) + int(y)
    except ValueError:
        print("Ошибка! Вводите только целые числа")
        raise ValueError


def test_log_file() -> None:
    result = func(1, 6)
    assert result == 7


def test_log_cap(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(5, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
