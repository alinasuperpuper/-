import pytest
from db import DatabaseClass


@pytest.fixture(scope='session')
def db_connection():
    # Создаём подключение к базе данных
    connection = sqlite3.connect(':memory:')
    yield connection
    connection.close()


@pytest.mark.parametrize("name", ["Запись 1", "Запись 2"])
def test_add_record(db_connection, name):
    db = DatabaseClass(db_connection)
    db.add_record(name)

    assert db.get_all_records() == [(1, name)]


def test_update_record(db_connection):
    db = DatabaseClass(db_connection)
    db.add_record("Старая запись")
    db.update_record(1, "Обновленная запись")

    assert db.get_all_records() == [(1, "Обновленная запись")]


def test_delete_record(db_connection):
    db = DatabaseClass(db_connection)
    db.add_record("Подлежит удалению")
    db.delete_record(1)

    assert db.get_all_records() == []


def test_get_all_records(db_connection):
    db = DatabaseClass(db_connection)
    db.add_record("Запись A")
    db.add_record("Запись B")

    assert db.get_all_records() == [(1, "Запись A"), (2, "Запись B")]
