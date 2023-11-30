import urllib.request
import urllib.parse
import json
import jsonpath


def get_request(Page):
    url_page = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page-1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = url_page + data
    headers = {
        'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_response(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()

def film(content):
    obj = json.loads(content)
    film_list = jsonpath.jsonpath(obj, '$..title')
    film_score = jsonpath.jsonpath(obj, '$..score')
    film = dict(zip(film_list, film_score))
    film = str(film)
    print(film)
    return film


def save(page, content):
    with open(f'douban_{page}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("开始页:"))
    stop_page = int(input("结束页:"))
    for page in range(start_page, stop_page+1):
        request = get_request(page)
        content = get_response(request)
        save(page, film(content))
