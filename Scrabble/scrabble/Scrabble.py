from itertools import islice

from data.scrabble_points import SCRABBLE_POINT_DICT


class Scrabble:

    def __init__(self, word_list):

        # Private variables to reference input word list and
        # corresponding word point list
        self._word_list = word_list
        self._points_list = []

        # Variables to reference dict containers as output values
        self._scrabble_word_point_dict = {}
        self._scrabble_word_point_dict_sorted = {}
        self._top_result_dict = {}

    def __len__(self):
        return len(self._word_list)

    @classmethod
    def _calculate_word_value(self, _word_total, word):
        """
        Description
        -----------
        Private class method to lookup and sum up letter values for each
        input word. Look up values are stored in `SCRABBLE_POINT_DICT`.
        Function returns integer variable `_word_total`.
        """
        for each_letter in word:
            _word_total += SCRABBLE_POINT_DICT[each_letter]
        return _word_total

    def calculate_points(self):
        """
        Description
        -----------
        Public class method to generate a collection of input word values
        and their corresponding Scrabble points. Function returns
        a Python dictionary `_scrabble_word_point_dict`.
        """
        for word in self._word_list:
            _word_total = 0
            self._points_list.append(
                self._calculate_word_value(_word_total, word))
        # Zip together word_list and points_list into a dict
        self._scrabble_word_point_dict = dict(
            zip(
                self._word_list,
                self._points_list,
                ))
        return self._scrabble_word_point_dict

    def calculate_points_sorted(self):
        """
        Description
        -----------
        Public class method to generate a collection of input word values
        and their corresponding Scrabble points reverse sorted by
        Scrabble word value. Function returns a Python dictionary
        `_scrabble_word_point_dict_sorted`.
        """
        self._scrabble_word_point_dict_sorted = dict(sorted(
            self.calculate_points().items(), key=lambda x: x[1], reverse=True))
        return self._scrabble_word_point_dict_sorted

    @classmethod
    def _slice(self, dict_data, partition):
        """
        Description
        -----------
        Private class method to yield an iterable Python dictionary
        of partitioned data.
        """
        dict_data_iter = iter(dict_data)
        for _ in range(0, len(dict_data), partition):
            yield {k: dict_data[k] for k in islice(dict_data_iter, partition)}

    def partition_results(self, partition_by):
        """
        Description
        -----------
        Public class method to generate an ordered Python dictionary of
        dictionary elements, partitioned by the number of segments required.
        Function returns a Python dictionary `_top_result_dict`.
        """
        # Variable to define partition size
        _partition = len(self._word_list) // partition_by
        # Incrementing counter variable to act as dict key for
        # each partition
        _partition_label_counter = 0
        # Loop through each partition and add to return dictionary
        for each_dict_partition in self._slice(
                                            self.calculate_points_sorted(),
                                            _partition):
            self._top_result_dict[
                _partition_label_counter] = each_dict_partition
            _partition_label_counter += 1
        return self._top_result_dict
