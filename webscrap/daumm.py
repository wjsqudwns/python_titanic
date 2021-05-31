from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen


class Daumm(object):
    url = 'https://movie.daum.net/ranking/boxoffice/weekly?date=20210517'
    class_name = ''
    m_name = []
    m_dict = {}
    df = None

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), "html.parser")
        all_tag = soup.find_all("strong", {"class":self.class_name})
        [self.m_name.append([i.find("a").text])for i in all_tag]


    def dict(self):
        rank = 0
        for i in range(0,len(self.m_name)):
            rank += 1
            self.m_dict[rank] = self.m_name

    def dict_to_df(self):
        self.df = pd.DataFrame.from_dict(self.m_dict, orient='index')

    def dict_to_csv(self):
        path = './movie/daumm.csv'
        self.df.to_csv(path, sep='n', na_rep='NaN')

    @staticmethod
    def csv_to_excel():

        xlsxname = pd.ExcelWriter('daumm.xlsx')  # 저장할 엑셀 파일이름
        xlsxpath = pd.read_csv('./movie/daumm.csv', error_bad_lines=False, engine="python")  # csv의 파일을 읽어옴
        xlsxpath.to_excel(xlsxname, index=False)
        xlsxname.save()

if __name__ == '__main__':
    d = Daumm()
    d.class_name = (input('입력: '))
    d.scrap()
    d.dict()
    d.dict_to_df()
    d.dict_to_csv()
    d.csv_to_excel()