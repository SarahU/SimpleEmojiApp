from translator_service import TranslatorService


def main():
    user_input = input("Input emoji codes. E to exit: ")
    while user_input != "E":
        translator_service = TranslatorService()
        print(translator_service.run_translation(user_input))
        user_input = input("Input emoji codes. E to exit: ")


if __name__ == '__main__':
    main()
