import os
import re

def find_server_ip(ip_search_result):
        pattern = re.compile(r'Address.*?(\d+\.\d+\.\d+\.\d+)')
        for line in ip_search_result:
                match_result = pattern.match(line)
                if match_result and ('127' not in match_result.group(1)):
                        # 使用Match获得分组信息
                        return match_result.group(1)


def find_github_fastly_net_ip():
        ip_search_result = os.popen('nslookup github.global.ssl.fastly.Net')
        return find_server_ip(ip_search_result)

def find_github_com_ip():
        ip_search_result = os.popen('nslookup github.com')
        return find_server_ip(ip_search_result)

def update_github_fastly_net_ip_in_dns_file(new_ip):
        file_content_to_write = ''

        with open('/etc/hosts', 'r') as f:
                for line in f.readlines():
                        if(line.find('http://global-ssl.fastly.Net') > 0):
                                line = '%s http://global-ssl.fastly.Net' % (new_ip) + '\n'

                        file_content_to_write += line

        with open('/etc/hosts', 'r+') as f:
                f.writelines(file_content_to_write)

def update_github_com_ip_in_dns_file(new_ip):
        file_content_to_write = ''

        with open('/etc/hosts', 'r') as f:
                for line in f.readlines():
                        if(line.find('http://github.com') > 0):
                                line = '%s http://github.com' % (new_ip) + '\n'

                        file_content_to_write += line

        with open('/etc/hosts', 'r+') as f:
                f.writelines(file_content_to_write)

def main():
        github_fastly_net_ip = find_github_fastly_net_ip()
        github_com_ip = find_github_com_ip()

        update_github_fastly_net_ip_in_dns_file(github_fastly_net_ip)
        update_github_com_ip_in_dns_file(github_com_ip)

        os.system('/etc/init.d/networking restart')



def test():
        pass

if __name__ == "__main__":
        main()

        # test()  