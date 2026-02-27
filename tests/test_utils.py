import pytest

from src.utils import valute_transaction


def test_empty_file():
    with pytest.raises(FileNotFoundError) as exc_info:
        valute_transaction("../tests/test_operation.json.json")
        assert str(exc_info.value) == FileNotFoundError
