#!/usr/bin/env python3
import os
import subprocess
import socket


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def display():
    print("\t\t************************************\n"
          "\t\t*****" + bcolors.OKGREEN, bcolors.BOLD + "Ping Test Troubleshooter " + bcolors.ENDC + "*****\n"
                                                                                                     "\t\t************************************\n\n\n"
                                                                                                     "Enter Selection: \n"
                                                                                                     "1 - Test connectivity to your gateway\n"
                                                                                                     "2 - Test for remote connectivity\n"
                                                                                                     "3 - Test for DNS resolution\n"
                                                                                                     "4 - Display gateway IP Address\n\n"
                                                                                                     "Please enter a" + bcolors.OKGREEN,
          bcolors.BOLD + "number (1-4)" + bcolors.ENDC + " or" + bcolors.OKGREEN,
          bcolors.BOLD + '"Q/q"' + bcolors.ENDC + " to quit the program "
          )


def user_input():
    while True:
        display()
        options = input()
        if options == "1":
            output = subprocess.run(["ip", "route"], capture_output=True, text=True)
            gateway_ip = output.stdout.split()[2]
            os.system('clear')
            test_connectivity(gateway_ip, "Testing connectivity to your gateway...\n")
            os.system("sleep 1")
            os.system('clear')
            user_input()
        elif options == "2":
            remote_ip = "8.8.8.8"
            os.system('clear')
            test_connectivity(remote_ip, "Testing for remote connectivity... trying IP address 8.8.8.8")
            os.system("sleep 1")
            os.system('clear')
            user_input()
            os.system('clear')
        elif options == "3":
            dns = "www.google.com"
            os.system('clear')
            resolve_dns(dns, "Resolving DNS: trying URL... " + dns)
            os.system("sleep 1")
            os.system('clear')
            user_input()
        elif options == "4":
            os.system('clear')
            output = subprocess.run(["ip", "route"], capture_output=True, text=True)
            gateway_ip = output.stdout.split()[2]
            print("Your gateway IP address is " + bcolors.WARNING,
                  bcolors.BOLD + gateway_ip + bcolors.ENDC)
            os.system("sleep 1")
            os.system('clear')
            user_input()
        elif options == "Q" or "q":
            os.system("clear")
            print("Quiting program: returning to shell.\n")
            print(bcolors.WARNING,bcolors.BOLD+"Have a wonderful day!" + bcolors.ENDC)
            os.system("sleep 1")
            exit()
        else:
            print("You entered an " + bcolors.FAIL,
                  bcolors.BOLD + "invalid option!" + bcolors.ENDC)
            os.system("sleep 1")
            os.system("clear")
            user_input()


def test_connectivity(ip, message):
    print(message)
    os.system("sleep 1")
    os.system('clear')
    print("Running test, please wait.")
    os.system("sleep 1")
    output = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
    if output.returncode == 0:
        print("Please inform your system administrator that the test was" + bcolors.WARNING,
              bcolors.BOLD + "SUCCESSFUL!" + bcolors.ENDC)
    else:
        print("Please inform your system administrator that the test was" + bcolors.FAIL,
              bcolors.BOLD + "Failed!" + bcolors.ENDC)


def resolve_dns(dns, message):
    os.system("clear")
    print(message)
    os.system("sleep 2")
    os.system("clear")
    print("Running Test, Please wait.")
    os.system("sleep 1")
    try:
        data = socket.gethostbyname(dns)

        print("Please inform your system administrator that the test was" + bcolors.WARNING,
              bcolors.BOLD + "SUCCESSFUL!" + bcolors.ENDC)
    except Exception:
        print("Please inform your system administrator that the test was" + bcolors.FAIL,
              bcolors.BOLD + "Failed!" + bcolors.ENDC)


def main():
    user_input()


if __name__ == "__main__":
    main()
