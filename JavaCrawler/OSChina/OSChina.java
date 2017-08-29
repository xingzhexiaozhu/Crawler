package OSChina;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class OSChina {
    public static void main(String[] args){

        //创建HttpClient
        CloseableHttpClient httpClient = HttpClients.createDefault();

        //目标网址
        String url = "http://www.oschina.net/";

        //创建请求方法
        HttpGet httpGet = new HttpGet(url);

        //设置Header模拟浏览器行为
        httpGet.setHeader("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36");

        try {
            //发送请求，收取响应
            CloseableHttpResponse httpResponse = httpClient.execute(httpGet);

            if(httpResponse.getStatusLine().getStatusCode() == 200){
                //解析响应
                String entity = EntityUtils.toString(httpResponse.getEntity());
                System.out.println(entity);
            }

            EntityUtils.consume(httpResponse.getEntity());
            httpResponse.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
