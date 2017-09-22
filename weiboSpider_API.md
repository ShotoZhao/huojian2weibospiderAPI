## Preface
* this is a simple spider to "m.weibo.cn" which is much easier than "weibo.com" without **login**.
* for now, it can spider original articles of a user. for more functions, you can modify it according to your purpose.
* only you need to do is to find out weibo **API** entrance.like this "https://m.weibo.cn/api/container/getIndex?uid=54147469&type=uid&value=54147469&containerid=1076035414746957&page=0"(you cant open it for i've modifie this address)

## Ddependency
* this project is based on python 2.7 in windows system,  Scrapy frame. but python3.x is ok i guess.

## Usage
1. download this project, and put it into your IDE. (e.g.Pycharm)
1. firstly, you need modify spider.py. the "start urls", "page"(how many pages you want to spider)  and "parse_item"(what item you want to spider?).
1. second, modify items.py according to formerly modified "parse_item".
1. finally, modify pipeline.py, to tell where you want to put your items. i write items into json file. you can input these into Mysql or Mongodb  whatever.


## PS
* actually, this project is just an idea to find an easier way to spider weibo.com. unfortunately, The API entrance is always not easy to disclose.
* if you can, more items are approachable such as user information, news, hot incidents and so on.
* ***if you like this project, please star it, thanks.***