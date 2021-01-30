import argparse, os, sys, subprocess
parser = argparse.ArgumentParser(description="Утилита для упрощения работы с openvpn")
parser = argparse.ArgumentParser(add_help=False)

# Аргументы
parser.add_argument("-a", dest='add_name', nargs="+", help="Добавить новый сертификат")
parser.add_argument("-r", dest="revoke_name", nargs="+", help="Отозвать сертификат" )
parser.add_argument("-s", "--status", action="store_true", help="Показать статус текущих подключений")
parser.add_argument("-l", "--log", action="store_true", help="Показать лог службы")
parser.add_argument("-u", "--users", action="store_true", help="Показать активные сертификаты")
parser.add_argument("-d", "--dell", action="store_true", help="Показать отозванные сертификаты")
parser.add_argument("-h","--help",action='help', default=argparse.SUPPRESS, help="Вывод справочной информации")
args = parser.parse_args() # парсим аргументы

auser = args.add_name
ruser = args.revoke_name

if len(sys.argv) == 1:
    print ('nERROR! You must specify at least one option')
    parser.print_help()

# workdir = '/usr/share/easy-rsa/3.0/' # определяем путь к дир-рии программы (раб. дир.)
# os.chdir(workdir)   # переходим в раб. дир.


def main():
    class ArgsException(Exception):
        pass  # класс исключения уникальности аргумента

    try:
        if auser and ruser:
            raise ArgsException()

        if auser:
            add(auser)
        elif ruser:
            revoke(ruser)
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':


    except ArgsException:
        print("\nОшибка! Ожидается параметр -a или -r, но не оба сразу.\n")


# Функцмя создания сертификата(ов)
def add(auser):
    subprocess.call('./vars')
    subprocess.call(["./easyrsa", "gen-req", auser])
    print(auser)














def revoke(ruser):
    print(ruser)


main()