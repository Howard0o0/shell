import os
import re
import socket

os_type = 'windows'
#os_type = 'linux'


def find_github_fastly_net_ip():
    ip = socket.gethostbyname("github.global.ssl.fastly.Net")
    return ip


def find_github_com_ip():
    ip = socket.gethostbyname("github.com")
    return ip


def update_github_fastly_net_ip_in_dns_file(new_ip):
    file_content_to_write = ''
    hosts_file = ''

    if os_type == 'windows':
        hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
    else:
        hosts_file = '/etc/hosts'

    with open(hosts_file, 'r') as f:
        for line in f.readlines():
            if(line.find('github.global.ssl.fastly.Net') > 0):
                line = '%s github.global.ssl.fastly.Net ' % (new_ip) + '\n'

            file_content_to_write += line

    with open(hosts_file, 'r+') as f:
        f.writelines(file_content_to_write)


def update_github_com_ip_in_dns_file(new_ip):
    file_content_to_write = ''
    hosts_file = ''

    if os_type == 'windows':
        hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
    else:
        hosts_file = '/etc/hosts'

    with open(hosts_file, 'r') as f:
        for line in f.readlines():
            if(line.find('github.com') > 0):
                line = '%s github.com' % (new_ip) + '\n'

            file_content_to_write += line

    with open(hosts_file, 'r+') as f:
        f.writelines(file_content_to_write)


def main():
    github_fastly_net_ip = find_github_fastly_net_ip()
    github_com_ip = find_github_com_ip()

    update_github_fastly_net_ip_in_dns_file(github_fastly_net_ip)
    update_github_com_ip_in_dns_file(github_com_ip)

    if os_type == 'linux':
        os.system('/etc/init.d/networking restart')

    else:
        os.system('ipconfig /flushdns')


def test():
    pass


if __name__ == "__main__":
    main()

    # test()
