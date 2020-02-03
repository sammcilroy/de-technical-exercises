import pytest

from utility.FileParser import FileParser
from scrabble.Scrabble import Scrabble


# Tests for FileParser Class
def test_readf_empty_file():
    # Given
    file_path_empty = "./Scrabble/data/test-empty-word-file.txt"
    fp = FileParser()
    # Then
    with pytest.raises(IOError):
        fp.readf(file_path_empty)


def test_readf_single_word_file():
    # Given
    file_path_single = "./Scrabble/data/data/test-single-word-file.txt"
    # When
    fp = FileParser()
    word_list = fp.readf(file_path_single)
    # Then
    assert ["abracadabra"] == word_list


def test_readf_invalid_char_file():
    # Given
    file_path_single = "./Scrabble/data/test-invalid-word-file.txt"
    # When
    fp = FileParser()
    word_list = fp.readf(file_path_single)
    # Then
    assert ["abracadabra"] == word_list


# Tests for Scrabble Class
def test_calculate_points():
    # Given
    example_word = ["abracadabra"]
    # When
    scrabble = Scrabble(example_word)
    scrabble_json = scrabble.calculate_points()
    # Then
    expected_json = {
        "abracadabra": 18
    }
    assert expected_json == scrabble_json


def test_calculate_points_sorted():
    # Given
    example_word_mult = ["abracadabra", "a", "zzzzzzzzzzz"]
    # When
    scrabble = Scrabble(example_word_mult)
    scrabble_json_srt = scrabble.calculate_points()
    # Then
    expected_json = {
        "zzzzzzzzzzz": 110,
        "abracadabra": 18,
        "a": 1
    }
    assert expected_json == scrabble_json_srt


def test_partition_result():
    # Given
    example_word_mult = ["abracadabra", "a", "zzzzzzzzzzz"]
    # When
    scrabble = Scrabble(example_word_mult)
    scrabble_json_prt = scrabble.partition_results(partition_by=3)
    # Then
    first_part = {
        "zzzzzzzzzzz": 110,
    }
    second_part = {
        "abracadabra": 18
    }
    third_part = {
        "a": 1
    }
    assert first_part == scrabble_json_prt[0]
    assert second_part == scrabble_json_prt[1]
    assert third_part == scrabble_json_prt[2]
