from translator_service import TranslatorService

translator_service = TranslatorService()


def run_example():
    in_text = "3 :thumbsup: -n 2 -s *"
    print("Example input:", in_text)
    print("Output:", translator_service.run_translation(in_text))


def main():
    user_input = input("Input emoji codes. E to exit. X for example: ")
    while user_input != "E":
        if user_input == "X":
            run_example()
        else:
            print(translator_service.run_translation(user_input))
        user_input = input("Input emoji codes. E to exit: ")


if __name__ == '__main__':
    main()
