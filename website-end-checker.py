import requests

print('''
        Name = Website end checker
        Author = Subnetix
        Version = 1.0
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
            print("End {} doesn't exist ".format(value))

except:
    pass

    
