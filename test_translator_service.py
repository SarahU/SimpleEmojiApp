import unittest

from translator_service import TranslatorService

service = TranslatorService()


class TestTranslatorService(unittest.TestCase):

    def test_get_arguments(self):
        command = '3 :thumbsup: -n 5 -s * -r True'
        actual_output = service.get_args(command)

        self.assertEqual(actual_output.count, 3)
        self.assertEqual(actual_output.emoji_code, ':thumbsup:')
        self.assertEqual(actual_output.n, 5)
        self.assertEqual(actual_output.r, True)
        self.assertEqual(actual_output.s, '*')

    def test_translate(self):
        command = '3 :thumbsup: -n 2 -s *'
        expected_output = '👍*👍*👍*👍*👍*👍'
        actual_output = service.run_translation(command)
        self.assertEqual(expected_output, actual_output)

    def test_command_unknown_wrong_count(self):
        command = 'THREE :thumbsup:'
        expected_output = 'Unknown command: THREE :thumbsup:'

        actual_output = service.run_translation(command)
        self.assertEqual(expected_output, actual_output)

    def test_command_unknown_emoji_code_not_present(self):
        command = '3 :highfive:'
        expected_output = 'Unknown command: 3 :highfive:'

        actual_output = service.run_translation(command)
        self.assertEqual(expected_output, actual_output)

    def test_command_unknown_completely(self):
        command = 'thisiscompletenonsense'
        expected_output = 'Unknown command: thisiscompletenonsense'
        actual_output = service.run_translation(command)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
