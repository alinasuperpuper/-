import pytest
from mainWin import MainWindow


def test_widgets_exist(main_window):
    assert main_window.some_widget is not None
    assert main_window.another_widget is not None


def test_button_click(main_window):
    main_window.some_button.click()
    assert main_window.some_action_performed()
