"""Download functionality for biber binaries."""
from __future__ import annotations

import re

from requests_html import HTMLSession

BASE_URL = "https://sourceforge.net"
FILES_URL = f"{BASE_URL}/projects/biblatex-biber/files/biblatex-biber"
DOC_TEX_URL = "https://raw.githubusercontent.com/plk/biber/dev/doc/biber.tex"

VALID_VERSION_PATTERN = re.compile(r"^(\d+\.\d+(\.\d+)?|current)$")
VERSION_TABLE_BODY_PATTER = re.compile(
    r"\\midrule\n(?P<rows>.+?)\\bottomrule.+\\caption\{\\biber\/\\biblatex\\ compatibility matrix",
    re.DOTALL,
)
VERSION_TABLE_VERSION_PATTER = re.compile(
    r"(?P<biber_version>\d\.[.\d]+) & (?P<biblatex_version>\d\.[.\d]+)\\\\\n"
)

VERSION_DOWNLOAD_EXTENSION = {
    "win32": "binaries/Windows/biber-MSWIN64.zip",
    "cygwin": "binaries/Cygwin/biber-cygwin64.tar.gz",
    "linux": "binaries/Linux/biber-linux_x86_64.tar.gz",
    "darwin": "binaries/MacOS/biber-darwin_universal.tar.gz",
}


def is_valid_version(version_str: str) -> bool:
    """Verify that a version string has a valid value.

    Parameters
    ----------
    version_str: str
        Version string to validate.

    Returns
    -------
    bool
        Whether or not the version string is valid.
    """
    return VALID_VERSION_PATTERN.match(version_str) is not None


def find_valid_biber_versions() -> dict[str, str]:
    """Find available biber versions on sourceforge.

    Returns
    -------
    dict[str, str]
        Valid versions with version string as key and partial download paths as value.

    See Also
    --------
    is_valid_version
    """
    version_dict = {}
    session = HTMLSession()
    resp = session.get(FILES_URL)
    for link in resp.html.find("tr.folder th a"):
        version_span = link.find("span", first=True)
        if version_span is not None:
            version_str = version_span.text
            if is_valid_version(version_str) is True:
                version_dict[version_str] = f"{BASE_URL}{link.attrs['href']}"

    return version_dict


def fetch_biber_biblatex_version_table() -> list[dict[str, str]]:

    session = HTMLSession()
    resp = session.get(DOC_TEX_URL)

    rows_match = VERSION_TABLE_BODY_PATTER.search(resp.text)
    if rows_match is None:
        raise ValueError("Could not find table pattern.")

    return [row.groupdict() for row in VERSION_TABLE_VERSION_PATTER.finditer(rows_match["rows"])]
