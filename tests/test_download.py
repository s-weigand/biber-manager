import pytest
from biber_manager.download import find_valid_biber_versions
from biber_manager.download import is_valid_version


@pytest.mark.parametrize(
    "version_str, expected",
    (
        ("current", True),
        ("0.9.9", True),
        ("2.17", True),
        ("1.3", True),
        ("multiscript", False),
    ),
)
def test_is_valid_version(version_str: str, expected: bool):
    assert is_valid_version(version_str) is expected


def test_find_biber_versions():
    version_dict = find_valid_biber_versions()
    assert "current" in version_dict
    assert (
        version_dict["current"]
        == "https://sourceforge.net/projects/biblatex-biber/files/biblatex-biber/current/"
    )
    assert "2.17" in version_dict
    assert (
        version_dict["2.17"]
        == "https://sourceforge.net/projects/biblatex-biber/files/biblatex-biber/2.17/"
    )
