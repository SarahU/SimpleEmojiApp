class EmojiTranslator:
    emoji_map = {':thumbsup:': '👍', ':thumbsdown:': '👎', ':ok:': '👌', ':crossed:': '🤞'}

    def translate_command(self, repeat_code_count, emoji_code, multiplier=1, separator='', disable_translation=False):
        # command format: 'N :emoji:'
        if disable_translation:
            single_emoji = emoji_code
        else:
            single_emoji = self.emoji_map[emoji_code]
        emojis = single_emoji * repeat_code_count * multiplier
        emojis = separator.join(emojis)

        return emojis
