import requests
import execjs
import time

class Py4Js():

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def translate(tk, content):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return

    fromlang = 'fr'
    tolang = 'en'
    param = {'tk': tk, 'q': content, 'sl': fromlang, 'tl': tolang}

    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&
        &hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)
        # "https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN"
    # 返回的结果为Json，解析为一个嵌套列表
    tranlate_result = result.json()[0][0]
    return tranlate_result[0]
    # for item in result.json():
    #     print(item)

def main():
    js = Py4Js()
    content = "电脑"
    tk = js.getTk(content)
    translate(tk, content)



if __name__ == "__main__":
    start_time = time.time()
    js = Py4Js()
    path = 'C:\\Users\\15708\\Desktop\\跨境电商数据\\ebay\\eBay_French_all.csv'
    ebay_French_list = open(path, 'r', encoding='utf-8')
    deal_list = []
    num = 1
    for line in ebay_French_list:
        line = line.replace("\n",'')
        item_list = line.split(';')
        tk = js.getTk(item_list[-9])
        title = translate(tk, item_list[-9])
        print(item_list[-9]+" | "+title)
        if num >100:
            break
        num = num + 1
    end_time = time.time()

    print("共有"+str(num)+"条记录 , 共花时间 " + str(end_time-start_time)+" 秒")