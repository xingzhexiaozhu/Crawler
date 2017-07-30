#  读书笔记

# 宽度优先搜索策略
原因：（1）深度优先遍历可能会在深度上过“深”而陷入“黑洞”；    
      （2）重要的网页往往距离种子网页比较近，越深的网页的重要性越低；   
      （3）万维网深度最多17层，但到达某面总存在一条很短的路径，宽度优先遍历会以最快的速度达到这个网页；  
      （4）宽度优先遍历有利于多爬虫的合作抓取，多爬虫合作通常先抓取站内链接，抓取的封闭性很强；
      
      
# 解析HTML网页---Jsoup
Maven中配置：
      <dependency>
         <groupId>org.jsoup</gorup>
         <artifactId>jsoup</artifactId>
         <version>1.10.3</version>
      </dependency>
      
      
# 解析Json数据---Json
Maven中配置：
      <dependency>
         <groupId>com.alibabap</gorup>
         <artifactId>fastjson</artifactId>
         <version>1.2.35.3</version>
      </dependency>


# 评估页面的重要程度
1.链接的欢迎程度---反向链接（即指向当前URL的链接）的数量和质量决定的，定义为IB(P)；
2.链接的重要程度---关于URL字符串的函数，仅仅考察字符串本身，比如认为".com"和"home"的URL比".cc"和"map"高，定义为IL(P)；
3.平均链接的深度---根据上面所分析的宽度优先的原则，计算全站的平均链接深度，然后认为距离种子站点越近的重要性越高，定义为ID(P)；
则网页的重要性I(P)=X*IB(P)+Y*IL(P)，ID(P)由宽度优先遍历规则保证 


# 存储
内存数据结构并不适合大规模爬虫的应用，因此采用内存数据库---Berkeley DB
成熟的开源爬虫软件---Heritrix（爬虫队列）
