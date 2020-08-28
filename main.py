import socket

from translator_service import TranslatorService

if __name__ == '__main__':
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    print ("waiting on port:", port)
    while 1:
        data, addr = s.recvfrom(1024)
        command = data.decode('utf-8')
        # print(command)

        translator_service = TranslatorService()

        print(translator_service.run_translation(command))


