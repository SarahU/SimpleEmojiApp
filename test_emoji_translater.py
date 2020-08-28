import unittest

from emoji_translator import EmojiTranslator

translator = EmojiTranslator()


class TestEmojiTranslations(unittest.TestCase):
    def test_thumbs_up_translation(self):
        command_N = 3
        command_code = ':thumbsup:'
        expected_output = '👍👍👍'

        actual_output = translator.translate_command(command_N, command_code, 1, '', False)
        self.assertEqual(expected_output, actual_output)

    def test_ok_translation(self):
        command_N = 5
        command_code = ':ok:'
        expected_output = '👌👌👌👌👌'

        actual_output = translator.translate_command(command_N, command_code, 1, '', False)
        self.assertEqual(expected_output, actual_output)


class TestCommandReading(unittest.TestCase):
    def test_command_known(self):
        # command format: 'N :emoji:'
        command_N = 3
        command_code = ':thumbsup:'
        expected_output = '👍👍👍'

        actual_output = translator.translate_command(command_N, command_code)
        self.assertEqual(expected_output, actual_output)


class TestOptionalParameters(unittest.TestCase):
    def test_command_multiplier(self):
        command_N = 3
        command_code = ':thumbsup:'
        multiplier = 3
        expected_output = '👍👍👍👍👍👍👍👍👍'

        actual_output = translator.translate_command(command_N, command_code, multiplier=multiplier)
        self.assertEqual(expected_output, actual_output)

    def test_command_separator(self):
        command_N = 3
        command_code = ':thumbsup:'
        separator = ','
        expected_output = '👍,👍,👍'

        actual_output = translator.translate_command(command_N, command_code, separator=separator)
        self.assertEqual(expected_output, actual_output)

    def test_command_disable_emoji_translation(self):
        command_N = 3
        command_code = ':thumbsup:'
        disable_emoji_translation = True
        expected_output = ':thumbsup::thumbsup::thumbsup:'

        actual_output = translator.translate_command(command_N, command_code,
                                                     disable_translation=disable_emoji_translation)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
