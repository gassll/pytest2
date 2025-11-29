from utils import dicts

def test_get_value():
    assert dicts.get_val({'vsc' : 'Красотка!'}, 'vsc') == 'Красотка!'
    assert dicts.get_val({'vsc' : 'Красотка!'}, 'vsc', 'git') == 'Красотка!'
    assert dicts.get_val({}, 'vsc', 'git') == 'git'