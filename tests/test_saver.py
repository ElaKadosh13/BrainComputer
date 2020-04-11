from braincomputer.db import Db
from braincomputer.saver.saver import save


def mock_init_db(self, url):
    pass


def mock_save_to_db(self, *args):
    pass


def mock_close_db(self):
    pass


def test_save(monkeypatch, capsys):
    monkeypatch.setattr(Db, "__init__", value=mock_init_db)
    monkeypatch.setattr(Db, "save_to_db", value=mock_save_to_db)
    monkeypatch.setattr(Db, "close_db", value=mock_close_db)
    save('mongodb://127.0.0.1:27017', '', 'tests/sources/parsed_data.txt')
    c, err = capsys.readouterr()
    assert err == ''
