# #  读书笔记

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
