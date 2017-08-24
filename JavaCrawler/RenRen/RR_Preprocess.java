package RenRen;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;

/**
 * 获取得到人人网的登录页面:
 * http://www.renren.com/PLogin.do
 */

public class RR_Preprocess {

    final static Logger log = LoggerFactory.getLogger(RR_Preprocess.class);

    public static void main(String[] args) throws IOException {

        //创建HttpClient
        CloseableHttpClient httpClient = HttpClients.createDefault();

        //目标网址
        String url = "http://www.renren.com";

        //请求方法
        HttpGet httpGet = new HttpGet(url);

        //发送请求，获得响应
        CloseableHttpResponse httpResponse = httpClient.execute(httpGet);

        //判断响应码
        int statusCode = httpResponse.getStatusLine().getStatusCode();
        if(statusCode == 200){
            //获取网页实例
            String entity = EntityUtils.toString(httpResponse.getEntity());

            //Jsoup解析网页
            Document document = Jsoup.parse(entity);

            log.info(document.toString());
        }
    }
}
