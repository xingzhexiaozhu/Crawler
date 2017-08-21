package Demo;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class HttpTest {
    public static void main(String[] args){
        CloseableHttpClient httpClient = HttpClients.createDefault();
        String url = "https://www.zhihu.com/";
        HttpGet httpGet = new HttpGet(url);
        System.out.println(httpGet);

        HttpPost httpPost = new HttpPost(url);
        System.out.println(httpPost);

        try {
            CloseableHttpResponse httpResponse = httpClient.execute(httpGet);
            System.out.println(httpResponse);

            //获取响应码
            int status = httpResponse.getStatusLine().getStatusCode();
            System.out.println(status);

            if(status == 200){
                String entity = EntityUtils.toString(httpResponse.getEntity());
                System.out.println(entity);
                EntityUtils.consume(httpResponse.getEntity());
            }else{
                EntityUtils.consume(httpResponse.getEntity());
            }
            httpResponse.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
