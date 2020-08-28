import argparse

from emoji_translator import EmojiTranslator


class TranslatorService:
    def get_args(self, command_string):

        split_args = command_string.split(' ')

        parser = argparse.ArgumentParser(description='Emoji Translation App!')
        argparse.ArgumentParser()
        parser.add_argument('count', type=int)
        parser.add_argument('emoji_code', type=str)
        parser.add_argument('-n', type=int, help='multiplier')
        parser.add_argument('-s', type=str, help='separator')
        parser.add_argument('-r', type=bool, help='translate or not')

        args = parser.parse_args(args=split_args)
        return args

    def run_translation(self, command):
        try:
            args = self.get_args(command)

            translator = EmojiTranslator()
            return translator.translate_command(args.count, args.emoji_code, args.n, args.s, args.r)

        except:
            return 'Unknown command: ' + command

