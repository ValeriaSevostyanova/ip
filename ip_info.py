import requests
import folium
import socket


def get_ip_by_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    
    except socket.gaierror as error:
        return f'Неверный адрес - {error}'




def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for i, j in data.items():
            print(f'{i} : {j}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('Проверьте подключение к интернету!')
        
        

if __name__ == '__main__':
    hostname = input('Введите домен сайта: ')
    get_info_by_ip(get_ip_by_hostname(hostname))
    
    
    