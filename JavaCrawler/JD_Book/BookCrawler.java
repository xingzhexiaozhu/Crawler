package JD;

import JD.model.Book;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class BookCrawler {
    static final Logger logger = LoggerFactory.getLogger(BookCrawler.class);

    public static void main(String[] args) throws IOException, SQLException, ClassNotFoundException {
        //创建HttpClient
        CloseableHttpClient httpClient = HttpClients.createDefault();

        //要爬取的URL
        String url = "http://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&pt=1&vt=2&cid2=3287&stock=1&click=3";

        //以Get方法请求页面内容
        HttpGet httpGet = new HttpGet(url);
        CloseableHttpResponse httpResponse = httpClient.execute(httpGet);

        //爬取的图书列表
        List<Book> books = new ArrayList<>();

        //获取响应码
        int statusCode = httpResponse.getStatusLine().getStatusCode();
        if(statusCode == 200){
            String entity = EntityUtils.toString(httpResponse.getEntity(), "utf-8");

            //采用Jsoup解析抓取到的网页
            Document doc = Jsoup.parse(entity);

            //获取HTML标签中的内容
            Elements elements = doc.select("ul[class=gl-warp clearfix]").select("li[class=gl-item]");
            for (Element ele : elements){
                String bookID = ele.attr("data-sku");
                String bookPrice = ele.select("div[class=p-price]").select("strong").select("i").text();
                String bookName = ele.select("div[class=p-name]").select("em").text();

                //从中提取出书籍对象
                Book book = new Book();
                book.setBookID(bookID);
                book.setBookName(bookName);
                book.setBookPrice(bookPrice);
                books.add(book);
            }
        }
        EntityUtils.consume(httpResponse.getEntity());

        if(exeInsertData(books))
            logger.info("Insert success!");
        else logger.info("Insert Fail!");

        httpResponse.close();
    }

    /**
     * 连接数据库，将爬取到的数据插入数据库中
     * @param books
     * @return
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    public static Boolean exeInsertData(List<Book> books) throws ClassNotFoundException, SQLException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1/learn?useUnicode=true&characterEncoding=utf-8&&useSSL=false&serverTimezone=UTC","root", "admin");
        String sql = "insert into book (bookID, bookName, bookPrice) values (?, ?, ?)";
        PreparedStatement exeUpdate = conn.prepareStatement(sql);

        for(Book book : books){
            exeUpdate.setString(1, book.getBookID());
            exeUpdate.setString(2, book.getBookName());
            exeUpdate.setString(3,book.getBookPrice());
            if(exeUpdate.executeUpdate() == 0){
                logger.info("insert fail");
                return false;
            }
        }
        exeUpdate.close();
        conn.close();

        return true;
    }
}
