import pytest
from addDataWin import AddDataWindow


@pytest.fixture
def db_connection():
    # Подключение к базе данных
    return MockDBConnection()


def test_add_data(db_connection):
    add_window = AddDataWindow(db_connection)
    add_window.add_record("Новая запись")

    assert add_window.get_last_record() == "Новая запись"


def test_edit_data(db_connection):
    add_window = AddDataWindow(db_connection)
    add_window.add_record("Старая запись")
    add_window.edit_record(1, "Измененная запись")

    assert add_window.get_last_record() == "Измененная запись"


def test_invalid_data_reaction(db_connection):
    add_window = AddDataWindow(db_connection)

    with pytest.raises(ValueError) as exc_info:
        add_window.add_record("")

    assert str(exc_info.value) == "Пустая строка не допускается"
