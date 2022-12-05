from fileutils import Fileutils


def test_is_file_not_2day(filepath="./../../confid/bypass.tok"):
    assert Fileutils().is_file_not_2day(filepath) is False
