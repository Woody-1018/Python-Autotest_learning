# 1、 id
# 2、name
# 3、class name
# 4、tag name
# 5、link text
# 6、partial link text
# 7、xpath
# 8、css selector
# 分别对应 python webdriver 中的方法为：
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name() 不靠谱
# find_element_by_tag_name() 最不靠谱
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

from selenium import webdriver
import time

# 以本地燃之为例
# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")
# 以 id 定位
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("submit").click()
time.sleep(5)
driver.quit()

# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")

# 以 name 定位,提交按钮无法由name定位，使用class name 定位
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")

# className不允许使用复合类名做参数
# <button type="submit" id="submit" class="btn btn-primary" data-loading="稍候...">登录</button>
# 1）执行driver.findElements(by.className("btn-primary")),成功定位到元素
# 2）执行driver.findElements(by.className("btn btn-primary")),定位失败，报错信息：Compound class names not permitted，意思是不允许使用复合类名称
# 分析：className的参数仅允许是一个class，此处class="btn btn-primary"是复合类名，直接使用会报错

driver.find_element_by_class_name("btn-primary").click()
time.sleep(5)
driver.quit()

# 以 link_text、partial_link_text 定位
# 1) linkText=链接文字，表示精准匹配链接文字；partialLinkText=部分链接文字，表示模糊匹配链接文字
# 2) 都对大小写敏感
# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("https://www.baidu.com/")
driver.find_element_by_link_text("新闻").click()
time.sleep(3)
driver.back()
driver.find_element_by_link_text("hao123").click()
time.sleep(3)
driver.back()
driver.find_element_by_partial_link_text("必读").click()
time.sleep(3)
driver.back()
driver.find_element_by_partial_link_text("京公网安备").click()
time.sleep(3)
driver.quit()

# 以 Xpath 定位
# xpath 的定位方法，非常强大。使用这种方法几乎可以定位到页面上的任意元素。
# xpath 这种定位方式，webdriver会将整个页面的所有元素进行扫描以定位我们所需要的元素，
# 这是个非常费时的操作，如果脚本中大量使用xpath做元素定位的话，脚本的执行速度可能会稍慢

# 绝对路径的缺点
# 一旦页面结构发生改变，改路径也随之失效，必须重新。 所以不推荐使用绝对路径的写法
#
# 绝对路径和相对路径的区别
# 绝对路径以"/"开头， 让xpath从文档的根节点开始解析
# 相对路径以"//"开头， 让xpath从文档的任何元素节点开始解析

# 常用的四种定位方法
# 第一种方法：通过绝对路径做定位（相信大家不会使用这种方式）
# By.xpath("html/body/div/form/input")
# By.xpath("//input")
# 第二种方法：通过元素索引定位
# By.xpath("//input[4]")
# 第三种方法：使用xpath属性定位（结合第2、第3中方法可以使用）
# By.xpath("//input[@id='kw1']")
# By.xpath("//input[@type='name' and @name='kw1']")
# 第四种方法：使用部分属性值匹配（最强大的方法）
# By.xpath("//input[start-with(@id,'nice')
# By.xpath("//input[ends-with(@id,'很漂亮')
# By.xpath("//input[contains(@id,'那么美')]")


# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")
driver.find_element_by_xpath("//*[@id='account']").clear()
driver.find_element_by_xpath("//*[@id='account']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='password']").clear()
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(3)
# driver.find_element_by_link_text("签退").click()
driver.find_element_by_xpath("//*[@id='bottomRightBar']/ul/li[1]/a").click()
time.sleep(3)
driver.quit()

# 以 CSS（Cascading Style Sheets） selector 定位
# CSS 定位语法比 XPath 更为简洁，定位方式更多灵活多样；不过对 CSS 理解起来要比 XPath 较难；
# 但不管是从性能还是定位更复杂的元素上，CSS 优于 XPath，笔者更推荐使用CSS定位页面元素。

# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")
driver.find_element_by_css_selector("#account").clear()
driver.find_element_by_css_selector("#account").send_keys("admin")
driver.find_element_by_css_selector("#password").clear()
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#submit").click()
time.sleep(3)
driver.find_element_by_css_selector("#bottomRightBar > ul > li:nth-child(1) > a").click()
driver.quit()

# 元素定位不到的原因及解决办法
# （1）定位属性值是动态变化的情况
#
# 现象：在我们定位元素的时候，发现有id, name或其他的属性存在，于是就用相应的定位方法去定位。可是运行的时候提示定位不到，
# 然后我们再去查看元素的时候，发现属性值和我们写代码的时候不一样了。
# 原因：通常产生这种情况的原因就是你使用的属性值是动态变化的，主要表现有属性值是一串数据，或是字符加一串数据等情况。
# 页面加载一次变化一次，每次都不相同。
# 解决办法：我们应尽量避免用这样的属性值去定位，而采用这个元素下的其他固定不变的属性值。或是向上层查找，采用Xpath定位。
# （2）Iframe中的元素定位出错的情况
#
# 现象：我们在定位元素的时候，查看网页源码，发现有iframe存在。可是我们没有做特殊处理，而是直接用通用的定位方法，
# name ,id, xpath或者CSS来定位。用Selenium IDE验证能查找到元素，可是运行测试用例的时候，总是元素找不到。
#
# 原因：在我们运行测试脚本的时候，代码获取的是页面的句柄，而iframe在句柄中是当成一个元素来处理的。
# 脚本是没有办法自己去iframe中去定位元素的，所以当搜索完页面时，发现找不到要定位的元素，就当错误处理。
#
# 解决办法：当需要定位iframe中的元素的时候，先将句柄切换到iframe中
#
# （driver.switchTo().frame("framename");）
# 然后再去定位，就能定位到要测试的元素。
#
# （3）不同页面或iframe切换时元素定位情况
#
# 现象：当我们在编写测试用例的时候，会遇到打开一个新页面，或是切换到一个新的iframe中，然后再去定位元素进行操作。
# 但是我们的定位方法写的没有问题，而且在Selenium IDE中也验证通过，可是代码运行的时候还是会提示找不到元素。
#
# 原因：其实这个和定位iframe中元素的情况是一样的，在打开一个页面或是切换到一个iframe的时候，
# driver获取的是当前页面或是iframe的句柄。当你的操作切换到新的页面或是iframe的时候，
# 如果代码不去做相应的切换，查找元素的时候还会在原来的句柄下查找，当然会出现查找不到的情况。
#
# 解决办法：当操作切换页面或是iframe的时候，我们的测试脚本也要做相应的切换，选择新打开的页面或是切换到新的iframe下。
# 然后再去定位的时候，就会在新页面或是iframe下定位了。
#
# （4）Xpath编写出错的情况
#
# 现象：如果我们对一个元素编写了对应的Xpath，然后在没有通过Selenium IDE进行验证的情况吧，就去编写代码执行测试用例。
# 会出现查找不到元素的情况，或是页面发生了变化，导致Xpath路径有了变化，也会查找不到元素。
#
# 原因：主要的问题就是Xpath编写出错了，或是页面有改动。不管是增加了新的模块或是隐藏的div，都会影响Xpath路径的。
#
# 解决办法：将代码中的Xpath拷出来，放到Selenium IDE中进行验证。如果出错了，就做相应的修改。
# 这个也是代码维护中当遇到的问题，被测试对象变化，导致测试用例的修改。
#
# （5）操作速度过快，被定位的元素没有加载出来的情况
#
# 现象：在测试用例运行过程中，会出现被定位的元素有的时候能定位的到，有的时候却定位不到的现象。
# 而我们去页面上验证我们的定位方法的时候，没有一点儿问题，显示不是定位方法写错了。
#
# 原因：这种情况多半是因为测试用例执行到代码的时候，被定位元素没有加载出来造成的。
# 网速原因，执行代码的机器原因，都会造成加载比程序执行的慢的情况。
#
# 解决办法：在我们定位元素之前，评估一下页面的加载情况，如果有加载慢的地方，需要添加一定等待时间
#
# self.sleep(5000),
# 等上几秒后再去定位操作。
#
# （6）定位页面嵌入式元素的情况
#
# 现象：在页面中会有一些儿嵌入式元素，如object,播放器等。这个时候，我们对其操作的时候，是无法定位到上面的元素的。
#
# 原因：嵌入式元素对webdriver来说是一个元素，不管里面包含多少元素，都无法操作。对于object对象，
# 网上有说要对相应的Flash重新编译，添加相应的代码或是控件才能定位。但这样一样又不安全了，
# 所以嵌入式对象一直是自动化测试的盲区。
#
# 解决办法：嵌入式对象如果是简单的单击操作，可是用模拟鼠标单击相应的区域，就能完成操作。如果是输入操作，
# 我们可以先模拟点击输入区，然后模拟键盘进行输入。除此之外，好像也没有什么好的办法。
#
# （7）firefox安全性报错的情况
#
# 现象：firefox安全性强，不允许跨域调用出现报错，错误描述：
#
# uncaught exception: [Exception... "Component returned failure code: 0x80004005 (NS_ERROR_FAILURE)"
# " [nsIDOMNSHTMLDocument.execCommand]" nsresult: "0x80004005 (NS_ERROR_FAILURE)" location:
# 原因：这是因为firefox安全性强，不允许跨域调用。
#
# 解决办法：Firefox 要取消XMLHttpRequest的跨域限制的话，
#
# 第一是从 about:config 里设置
#
#  signed.applets.codebase_principal_support = true； （地址栏输入about:config
# 即可进行firefox设置）。
#
# 第二就是在open的代码函数前加入类似如下的代码：
#
# try{
#           netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserRead");
# }
# catch (e)
#  {
#             alert("Permission UniversalBrowserRead denied.");
#  }
# 对错误进行处理。

