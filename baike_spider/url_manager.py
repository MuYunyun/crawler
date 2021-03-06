# coding:utf8

class UrlManager(object):
      def __init__(self):
          self.new_urls = set() # 待爬取 url 列表
          self.old_urls = set() # 爬取过 url 列表

      def add_new_url(self, url):
          if url is None:
              return
          if url not in self.new_urls and url not in self.old_urls:
              self.new_urls.add(url)

      def add_new_urls(self, urls):
          if urls is None or len(urls) == 0:
              return
          for url in urls:
              self.add_new_url(url)

      def has_new_url(self):
          return len(self.new_urls) != 0

      def get_new_url(self):
          new_url = self.new_urls.pop()
          self.old_urls.add(new_url)
          return new_url

