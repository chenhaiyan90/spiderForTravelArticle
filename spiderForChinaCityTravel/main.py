from scrapy import cmdline
# cmdline.execute('scrapy crawl amazon_products -o items.csv -t csv'.split()) 例子
name=['travelPeople','cnta']
cmd='scrapy crawl {0} {1}'.format(name)
cmdline.execute(cmd.split())
# cmdline.execute('scrapy crawl travelPeople'.split())
# －o 代表输出文件 －t 代表文件格式  运行这个就爬取