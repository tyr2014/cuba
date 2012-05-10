import re
from scrapy.http.request import Request
from scrapy.selector.lxmlsel import HtmlXPathSelector
from scrapy.spider import BaseSpider
from douban.items import Activity

class TongChengSpider(BaseSpider):
  name = "TongCheng"
  allowed_domains = ["douban.com"]
  start_urls = [
    "http://beijing.douban.com/events/future/travel",
    #"http://shanghai.douban.com/events/future/travel",
  ]

  def _get_item(self, node, type='/text()'):
    try:
      text = node.select(type).extract()
    except Exception:
      text = ''

    if isinstance(text, list):
      return text[0].strip()
    else:
      return text.strip()

  def text(self, node):
    return self._get_item(node, type='text()')

  def href(self, node):
    return self._get_item(node, type='@href')

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    last_page_node = hxs.select("//div[@class='paginator']/a[last()]")

    last_page = int(self.href(last_page_node).split('=')[1])
    pages = range(10, last_page, 10)
    pages = []

    for page in pages:
      page_url = response.url + '?start=' + str(page)
      self.log('Found page url: %s' % page_url)
      yield Request(page_url, callback = self.parse_list)

    # process first page
    # self.parse_list(response)
    yield Request(response.url, callback=self.parse_list)

  def parse_list(self, response):
    hxs = HtmlXPathSelector(response)
    activity_nodes = hxs.select("//li[@class='list-entry']/div[2]/div/a")

    for node in activity_nodes:
      activity_url = self.href(node)
      self.log('Found activity url: %s' % activity_url)
      yield Request(activity_url, callback = self.parse_activity)

  def parse_activity(self, response):
      hxs = HtmlXPathSelector(response)
      event_info_node = hxs.select('//div[@class="event-info"]')
      title = self.text(event_info_node.select('h1'))
      event_detail_nodes = event_info_node.select('div[@class="event-detail"]')
      details = {}
      for n in event_detail_nodes:
        self.log(n.extract())
        key = self.text(n.select('span')).strip().replace(':','')
        value = re.sub('<[^<]+?>', '', n.extract()).split(':')[1].strip()
        details[key] = value

      description = '\n'.join(hxs.select('//div[@class="related_info"]/div/div/text()').extract())
      photo_urls = hxs.select('//ul[contains(@class,"event-detail-photo")]/li/a/img/@src').extract()
      photo_urls = map(lambda x:x.replace('albumicon', 'photo'), photo_urls)

      entry = Activity()
      entry['title'] = title
      entry['description'] = description
      entry['images'] = photo_urls
      entry['details'] = details

      return entry

