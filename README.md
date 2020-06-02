<!--
 * @Author         : yanyongyu
 * @Date           : 2020-06-02 11:08:28
 * @LastEditors    : yanyongyu
 * @LastEditTime   : 2020-06-02 16:26:30
 * @Description    : None
 * @GitHub         : https://github.com/yanyongyu
-->

# Nazo-backend

## 相关链接

- <https://nazo.cs181.com.cn/>
- <https://github.com/yanyongyu/nazo-frontend>

## 谜题详解

### Lv1 开始

直接输入 `Key` 即可过关。

### Lv2 空

`Key` 就在题目下方哦！`检查元素` 或者 `鼠标选中` 即可看到，手机可以长按选择。

```css
.transparent {
  color: transparent !important;
}
```

### Lv3 白

一片白，鼠标似乎能选中几个换行符？

检查元素即可看到一串乱码：

```html
<span>
  &zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;
</span>

<br />

<span>
  &zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwj;
</span>

<br />

<span>
  &zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;
</span>

<br />

<span>
  &zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwj;&zwj;
</span>

<br />

<span>
  &zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwj;&zwnj;&zwnj;&zwj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwj;&zwj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;
</span>
```

全是由 `&zwj;` `&zwnj;` 组成的文本。

`&zwj;` 是 unicode 中的 `Zero Width Joiner` ，即零宽连字空格，对应 unicode 为 `U+200D`。

`&zwnj;` 是 unicode 中的 `Zero Width Non-Joiner` ，即零宽不连字空格，对应 unicode 为 `U+200C`。

这两个字符是 `零宽字符` ，所以看上去就像没有一样。

将所有的 `&zwj;` 替换为空格，`&zwnj;` 替换为 1 即可看到字符画 `UNICODE`。

```plain
 11    11 11   11 11  111111  111111  1111111  1111111
 11    11 111  11 11 11      11    11 11    11 11
 11    11 11 1 11 11 11      11    11 11    11 11111
 11    11 11  111 11 11      11    11 11    11 11
  111111  11   11 11  111111  111111  1111111  1111111
```

### Lv4 色彩

这题直接使用 `取色器` 或者 `检查元素` 即可看到四个颜色的区别。

前排提示：Chrome 自带取色器哦！检查元素之后点击 `element.style` 右下角的小工具 `⠇` 中的油漆桶，然后选择吸管即可在网页中取色。

```css
.red {
  background-color: rgb(244, 67, 53);
}
```

### Lv5 平平无奇的数学小天才

230 － 220×0.5 ＝ 5！

这个感叹号是阶乘哦～

### Lv6 宇宙终极问题

x<sup>3</sup> ＋ y<sup>3</sup> ＋ z<sup>3</sup> ＝ 42

这看上去是个简单的问题，但是，不要妄想自己解出来啦！

2019 年 2 月，布里斯托大学数学教授安德鲁·布克(Andrew Booker)创建了一个算法，来寻找 x<sup>3</sup> ＋ y<sup>3</sup> ＋ z<sup>3</sup> ＝ k 的解，该算法运行时涉及到 10<sup>16</sup> 次数值，在算法运行几周后获得了 33 的答案：(8,866,128,975,287,528)<sup>3</sup> ＋ (–8,778,405,442,862,239)<sup>3</sup> ＋ (–2,736,111,468,807,040)<sup>3</sup> ＝ 33

2019 年 9 月，来自麻省理工学院研究人员 Andrew Sutherland 和英国布里斯托尔大学的 Andrew Booker 合作进行了一项超长时间计算，他们使用了超 100 万小时的慈善引擎计算后，终于破解了 42，(-80538738812075974)<sup>3</sup> ＋ (80435758145817515)<sup>3</sup> ＋ (12602123297335631)<sup>3</sup> ＝ 42。

### Lv7 地址

题目链接到了华理的官网，地址不是门牌号，自然就是指 `IP地址` 了

方法一：

```shell
$ ping www.ecust.edu.cn -c 1
PING www.ecust.edu.cn (202.120.108.164) 56(84) bytes of data.
64 bytes from 202.120.108.164 (202.120.108.164): icmp_seq=1 ttl=50 time=6.20 ms

--- www.ecust.edu.cn ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 6.204/6.204/6.204/0.000 ms
```

可以看到服务器的 `IP地址` 为 `202.120.108.164`

方法二：

使用 `DNS查询` 工具

```shell
$ dig www.ecust.edu.cn
; <<>> DiG 9.11.3-1ubuntu1.12-Ubuntu <<>> www.ecust.edu.cn
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6484
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;www.ecust.edu.cn.              IN      A

;; ANSWER SECTION:
www.ecust.edu.cn.       964     IN      A       202.120.108.164

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Tue Jun 02 12:30:32 CST 2020
;; MSG SIZE  rcvd: 61
```

可以看到域名对应的 `A记录` 指向 IP `202.120.108.164`

### Lv8 网址

题目中给出了一个网址 `💖💻.cs181.com.cn` 。不要怀疑，他真的是一个网址！

将网址输入浏览器回车，就会发现网址变成了 `xn--1r8hkc.cs181.com.cn` 并打开了。这是由于网址使用了 `punycode` 编码，使得 `emoji` `中文` 也可以作为网址。

什么？中文也可以？

不妨试试：`错的是。世界` （PS：有些浏览器不认中文句号，Chrome 会自动转换）

回归正题，打开网页获得一串 emoji，punycode 编码后即是答案。

### Lv9 域名

这道题也给出了一个网址，但他并不能打开。

网址中提示这是一个 `txt记录` 网址，于是进行 DNS 记录查询：

```shell
$ dig txt.cs181.com.cn txt
 <<>> DiG 9.11.3-1ubuntu1.12-Ubuntu <<>> txt.cs181.com.cn txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13251
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;txt.cs181.com.cn.              IN      TXT

;; ANSWER SECTION:
txt.cs181.com.cn.       300     IN      TXT     "Key: txt dns record"

;; Query time: 886 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Tue Jun 02 16:10:42 CST 2020
;; MSG SIZE  rcvd: 77
```

即可查询到 `txt记录` `"Key: txt dns record"`

DNS 记录不仅只有指向 `IP地址` 的 `A记录` ，常见的还有如：

- `AAAA`：指向 IPv6 地址
- `CNAME`：指向另一个域名，即 `别名` 记录
- `NS`：指向另一个域名服务器
- `MX`：邮件交换记录，指向一个邮件服务器。发送邮件的时候就会查询这个记录哦～
- `TXT`：存储一段文本内容，通常用来留下联系方式、SPF 反垃圾邮件或者是 DNS Auth（DNS 验证）时会用到

### Lv10 秘密

非常简单的 `凯撒加密` 题目。

凯撒密码是一种移位密码，移回来就是了。其他类似的加密还有：`ROT5` , `ROT13` , `ROT18` , `ROT47` 等等

### Lv11 随机

同样是一串乱码，并不能找到规律，但根据上一题的经验，开头的 `ntz` 就应该是 `key` 三个字母。

那么，上 `词频分析`！什么？你不会？在线工具了解一下：<https://www.quipqiup.com/>

## 结语

非常简单的 nazo ，旨在普及一些基础的计算机相关知识以及工具技巧。

完。
