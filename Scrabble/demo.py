import time

from utility.FileParser import FileParser
from scrabble.Scrabble import Scrabble


if __name__ == "__main__":

    # Path to input data file
    file_path = "./data/dictionary-large.txt"

    # Initialise file parser object
    parser = FileParser()

    # Read file into Python list
    word_list = parser.readf(file_path)

    # Initialise Scrabble object
    scrabble = Scrabble(word_list)

    # Time calculate_points()
    start_time = time.time()
    scrabble_word_dict = scrabble.calculate_points()
    end_time = time.time()
    points_time = end_time - start_time

    # Time calculate_points_sorted()
    start_time = time.time()
    scrabble_word_dict_sorted = scrabble.calculate_points_sorted()
    end_time = time.time()
    sorted_time = end_time - start_time

    # Time calculate_points_sorted()
    start_time = time.time()
    scrabble_word_dict_partition = scrabble.partition_results(partition_by=4)
    end_time = time.time()
    partition_time = end_time - start_time

    print("---------- Scrabble Demo ----------")
    print(f"INPUT FILE: {file_path}")
    print(f"NUMBER OF WORDS IN INPUT FILE: {len(scrabble)}")
    print(f"TIME TO COMPUTE POINTS: {points_time} seconds")
    print(f"TIME TO COMPUTE POINTS SORTED: {sorted_time} seconds")
    print(f"TIME TO COMPUTE POINTS PARTITIONED {partition_time} seconds")
