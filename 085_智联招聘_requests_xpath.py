# 岗位名称：//div[@class='positionlist']/div/a//span[@class='iteminfo__line1__jobname__name']/@title
# 薪酬水平：//p[@class='iteminfo__line2__jobdesc__salary']/text()
# 工作地点：//ul[@class='iteminfo__line2__jobdesc__demand']/li[1]/text()
# 学历：//ul[@class='iteminfo__line2__jobdesc__demand']/li[3]/text()
# 公司名称：//span[@class='iteminfo__line1__compname__name']/text()

# https://sou.zhaopin.com/?jl=城市代码&kw=python&el=5&p=1
# 把保定、石家庄、天津、北京 写到  python_智联招聘.csv
import requests
from lxml import etree
import csv
import time
from tqdm import tqdm


def create_request(code):
    url = 'https://sou.zhaopin.com/?'
    data = {
        'jl': str(code),
        'kw': 'python',
        'el': '5',
        'p': '1'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers, params=data)
    return response


def get_content(response):
    content = response.text
    # 解析服务器响应的文件
    tree = etree.HTML(content)
    # 岗位名称
    name_list = tree.xpath("//div[@class='positionlist']/div/a//span[@class='iteminfo__line1__jobname__name']/@title")
    # 薪酬水平
    salary_list = tree.xpath("//p[@class='iteminfo__line2__jobdesc__salary']/text()")
    # 工作地点
    location_list = tree.xpath("//ul[@class='iteminfo__line2__jobdesc__demand']/li[1]/text()")
    # 学历要求
    education_list = tree.xpath("//ul[@class='iteminfo__line2__jobdesc__demand']/li[3]/text()")
    # 公司名称
    company_list = tree.xpath("//span[@class='iteminfo__line1__compname__name']/text()")
    # 职务描述
    job_description_list = tree.xpath('//a[@class="joblist-box__iteminfo iteminfo"]/@href')

    content_rows_list = []
    for i in range(len(name_list)):
        name = name_list[i].strip()
        salary = salary_list[i].strip()
        location = location_list[i].strip()
        education = education_list[i].strip()
        company = company_list[i].strip()
        job_description =job_description_list[i].strip()
        content_rows_list.append([name, salary, location, education, company,job_description])

    return content_rows_list


def write_csv(content_rows_list):
    w.writerows(content_rows_list)


# 程序入口
if __name__ == '__main__':
    print('------开始爬取数据，请耐心等待------')
    start = time.perf_counter()
    fp = open("python_智联招聘.csv", 'w', encoding='utf-8', newline="")
    w = csv.writer(fp)
    w.writerow(['岗位名称', '薪酬水平', '工作地点', '学历要求', '公司名称','岗位描述'])
    # 城市代码：北京530  天津531 石家庄565 保定570
    city_list = [530, 531, 565, 570]
    for code in tqdm(city_list,'爬取进度'):
        # (1)请求定制
        response = create_request(code)
        # (2)获取源代码并解析
        content_rows_list = get_content(response)
        # (3)把保定、石家庄、天津、北京招聘信息 写到  python_智联招聘.csv
        write_csv(content_rows_list)
        time.sleep(2)

    fp.close()
    print('------' + '耗时' + str(round((time.perf_counter() - start) / 60, 2)) + '分钟--------')  # 打印提示信息
