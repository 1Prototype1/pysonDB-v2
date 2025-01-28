import json

import pytest

from pysondb.db import PysonDB


TEST_DATA = {
    'version': 2,
    'keys': ['age', 'name'],
    'data': {
        '2352346': {
            'age': 4,
            'name': 'mathew_first'
        },
        '1234567': {
            'age': 9,
            'name': 'new_user'
        }
    }
}


@pytest.mark.parametrize(
    'condition,output',
    [
        ({'age': 4}, [{'age': 4, 'name': 'mathew_first'}]),
        ({'name': 'new_user'}, [{'age': 9, 'name': 'new_user'}]),
        ({}, [{'age': 4, 'name': 'mathew_first'},{'age': 9, 'name': 'new_user'}]),
        ({'age': 99}, []),
    ]
)
def test_fetch(tmpdir, condition, output):
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA))
    db = PysonDB(f.strpath)

    assert db.fetch(condition) == output

@pytest.mark.parametrize(
    'condition',
    [1, 2]
)
def test_fetch_type_error(tmpdir, condition):
    f = tmpdir.join('test.json')
    db = PysonDB(f.strpath)

    with pytest.raises(TypeError):
        db.fetch(condition)
