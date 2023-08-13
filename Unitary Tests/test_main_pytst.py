import pytest
from main_pytst import escribir

def test_tmp_dir(tmpdir):
    data_in = "CodinEric"
    fpath = f"{tmpdir}/test.txt"
    escribir(fpath,data_in)

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == "data_out"
