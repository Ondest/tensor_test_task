import pytest
import argparse
from unittest.mock import patch
from cli import parse_args


def test_parse_args_valid():
    test_args = ["cli.py", "sample.json", "1"]
    with patch("sys.argv", test_args):
        args = parse_args()
        assert args.json_file == "sample.json"
        assert args.employee_id == 1


def test_parse_args_invalid_json_file():
    test_args = ["cli.py", "invalid.txt", "1"]
    with patch("sys.argv", test_args):
        with pytest.raises(argparse.ArgumentTypeError):
            parse_args()


def test_parse_args_nonexistent_file():
    test_args = ["cli.py", "nonexistent.json", "1"]
    with patch("sys.argv", test_args):
        with pytest.raises(argparse.ArgumentTypeError):
            parse_args()
