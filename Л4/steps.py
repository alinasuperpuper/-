from behave import given, when, then
from PyQt6.QtWidgets import QApplication
from Test.BDD.database.scripts.db import Data
import sys

app = QApplication(sys.argv)


@given('база данных очищена')
def step_impl(context):
    context.db = Data("database/service_center.db")
    context.db.clear()


@when('я добавляю запись с данными "{data}"')
def step_impl(context, data):
    context.db.add_record(data)


@then('новая запись должна быть добавлена в базу данных')
def step_impl(context):
    assert context.db.record_exists("Тестовая запись")


@given('база данных содержит запись "{data}"')
def step_impl(context, data):
    context.db.add_record(data)


@when('я открываю окно просмотра')
def step_impl(context):
    context.window = context.db.open_view_window()


@then('я вижу запись "{data}"')
def step_impl(context, data):
    displayed_data = context.window.get_displayed_data()
    assert data in displayed_data


@when('я редактирую запись "{old_data}" на "{new_data}"')
def step_impl(context, old_data, new_data):
    context.db.edit_record(old_data, new_data)


@then('запись "{data}" должна существовать')
def step_impl(context, data):
    assert context.db.record_exists(data)


@when('я удаляю запись "{data}"')
def step_impl(context, data):
    context.db.delete_record(data)


@then('записи "{data}" не должно быть в базе данных')
def step_impl(context, data):
    assert not context.db.record_exists(data)


@when('я пытаюсь добавить запись с некорректными данными')
def step_impl(context):
    context.error_msg = context.db.add_record("Некорректные данные")


@then('я получаю сообщение об ошибке')
def step_impl(context):
    assert context.error_msg == "Ошибка в данных"


@when('я нажимаю на кнопку "{button}"')
def step_impl(context, button):
    context.window.click_button(button)


@then('окно просмотра открыто')
def step_impl(context):
    assert context.window.is_open()


@then('я вижу данные "{data}"')
def step_impl(context, data):
    displayed_data = context.window.get_displayed_data()
    assert data in displayed_data
