package RenRen;

import org.apache.http.Header;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

/**
 * 由RR_Preprocess.java得到登录跳转页面
 * 这里先以Post方法请求登录页面，然后再以Get方法请求登录后的页面
 */

public class RR_Login {

    public static void main(String[] args){
        //创建HttpClient
        CloseableHttpClient httpClient = HttpClients.createDefault();

        //请求的目标网址
        String rr_url = "http://www.renren.com/PLogin.do";

        HttpPost httpPost = new HttpPost(rr_url);

        //以Post方式请求，设置登录用户名和密码
        List<NameValuePair> nameValuePairs = new ArrayList<>();
        nameValuePairs.add(new BasicNameValuePair("email", "156******")); //这里改为自己的用户名
        nameValuePairs.add(new BasicNameValuePair("password", "*******"));//这里改为自己的密码

        try {
            httpPost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
            CloseableHttpResponse httpResponse = httpClient.execute(httpPost);

            //获取请求头
            Header header = httpResponse.getFirstHeader("Location");
            if(header != null){

                //以Get方法请求得到重定向的URL
                HttpGet httpGet = new HttpGet(header.getValue());

                ResponseHandler<String> responseHandler = new BasicResponseHandler();
                String res = httpClient.execute(httpGet, responseHandler);

                System.out.println(res);
            }

        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (ClientProtocolException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
