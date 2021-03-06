import tempfile

import pytest
from click.testing import CliRunner

import symmetry_representation as sr
from symmetry_representation._cli import cli


def test_filter_symmetries_noop(unstrained_poscar, symmetries_file):
    runner = CliRunner()
    with tempfile.NamedTemporaryFile() as out_file:
        run = runner.invoke(
            cli, [
                'filter_symmetries', '-s', symmetries_file, '-l',
                unstrained_poscar, '-o', out_file.name
            ],
            catch_exceptions=False
        )
        result = sr.io.load(out_file.name)
    reference = sr.io.load(symmetries_file)
    assert len(result) == len(reference)
    assert len(result[1].symmetries) == len(reference[1].symmetries)


def test_filter_symmetries_strained(strained_poscar, symmetries_file):
    runner = CliRunner()
    with tempfile.NamedTemporaryFile() as out_file:
        run = runner.invoke(
            cli, [
                'filter_symmetries', '-s', symmetries_file, '-l',
                strained_poscar, '-o', out_file.name
            ],
            catch_exceptions=False
        )
        result = sr.io.load(out_file.name)
    reference = sr.io.load(symmetries_file)
    assert len(result) == len(reference)
    assert len(result[1].symmetries) == 4
