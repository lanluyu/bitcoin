bitcoin说明文档
==
介绍
 - 
bitcoin是一个基于Scrapy的比特币新闻爬虫，爬取了巴比特网站有关比特币的新闻。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

### 其它
目前只是爬取了该网站上的部分文章，如有需要，可以做全站爬虫，爬取该网站有关区块链、链创投、链研报、链周刊的有关信息。

爬取结果
-
在巴比特网站上总共爬取了50448条有关比特币的文章。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![文章信息截图](https://github.com/lanluyu/bitcoin/blob/master/%E6%96%87%E7%AB%A0%E4%BF%A1%E6%81%AF%E6%88%AA%E5%9B%BE.PNG)
