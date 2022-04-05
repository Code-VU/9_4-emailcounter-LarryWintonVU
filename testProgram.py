import io
from random import randint
from unittest.mock import Mock
import counter

def test_calculate_printsLineCountSmallFile(capfd, monkeypatch):
    input = ['']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    counter.countEmail()

    out, err = capfd.readouterr()
    assert "cwen@iupui.edu 5" in out

def test_calculate_printsLineCountLargeFile(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    counter.countEmail()

    out, err = capfd.readouterr()
    
    assert "zqian@umich.edu 195" in out