import asyncio
import aiohttp
import execjs
import time


def get_word_url(text):
    # text = text.replace(' ','20%')
    ctx = execjs.compile("""
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
    tk = ctx.call("TL", text)

    fromlang = 'fr'
    tolang = 'en'
    param = {'tk': tk, 'q': text, 'sl': fromlang, 'tl': tolang}

    resp = yield from aiohttp.request(url="""http://translate.google.cn/translate_a/single?client=t&
           &hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
           &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", method='GET',params=param)
    result = yield from resp.text()
    print(result)



def main():

    loop = asyncio.get_event_loop()
    to_do = []

    path = 'C:\\Users\\15708\\Desktop\\跨境电商数据\\ebay\\eBay_French_all.csv'
    ebay_French_list = open(path, 'r', encoding='utf-8')
    num = 1
    for line in ebay_French_list:
        line = line.replace("\n", '')
        item_list = line.split(';')
        to_do.append(get_word_url(item_list[-9]))
        if num > 100:
            break
        num = num + 1
    print("start")
    start = time.time()
    wait_coro = asyncio.wait(to_do)
    loop.run_until_complete(wait_coro)
    loop.close()
    end = time.time()
    print("共花时间"+str(end-start)+"秒")

if __name__ == '__main__':
    main()


