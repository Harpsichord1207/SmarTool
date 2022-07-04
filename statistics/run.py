from urllib import request

host = 'https://pypistats.org/'
package = 'SmarTool'.lower()

python_minor_endpoint = f'api/packages/{package}/python_minor'
system_endpoint = f'api/packages/{package}/system'


if __name__ == '__main__':
    resp = request.urlopen(host+python_minor_endpoint)
    print(resp.read().decode())
