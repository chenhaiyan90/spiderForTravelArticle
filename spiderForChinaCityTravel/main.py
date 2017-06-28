from scrapy import cmdline
# cmdline.execute('scrapy crawl amazon_products -o items.csv -t csv'.split()) 例子
names=['cnta','travelPeople']
for val in names:
    cmd = 'scrapy crawl {0}'.format(val)
    cmdline.execute(cmd.split())


# cmdline.execute('scrapy crawl travelPeople'.split())
# －o 代表输出文件 －t 代表文件格式  运行这个就爬取