Date: 2016-06-11 16:02
Title:   springBoot与MyBatis整合示例
springBoot与MyBatis整合示例
====
###MyBatis的配置的一般步骤：

1. 数据源的配置
2. 配置MyBatis的映射xml
3. 配置mybatis的sqlSessionFactory


###Mybatis的相关jar
以下是gradle的引jar的包的方式：

    complie "org.springframework.boot:
    spring-boot-starter-jdbc:1.2.3.RELEASE"
    compile "org.mybatis:mybatis:3.2.8"
    compile "org.mybatis:mybatis-spring:1.2.1"
    compile "com.alibaba:druid:1.0.13"
    compile "mysql:mysql-connector-java:5.1.35"
    compile "com.alibaba:fastjson:1.1.41"
    
    
使用springBoot的最大好处是可以使用javaConfig来配置属性，其实它类似与spring中的xml配置，在springBoot中可以使用yml文件来配置一些属性，下面就是用yml来配置数据源和mybatis的xml映射关系的：application.yml,配置如下：

    druid:
      dataSource:
    	driverClassName: com.mysql.jdbc.Driver
    	url: jdbc:mysql://localhost:3306/test
    	username: root
   		password: 
        initialSize: 5
        maxActive: 200
        minIdle: 5
        maxWait: 60000
        validationQuery: SELECT 1 FROM DUAL
        removeAbandoned: true
        removeAbandonedTimeout: 180
        mapperLocations: classpath*:com.mapper.*/ *Mapper.xml    
        
以下是javaConfig的配置

1.首先创建个DataSourceSettings来加载数据库的来源：
	
	import com.alibaba.druid.pool.DruidDataSource;
    import org.springframework.boot.context.properties.
    ConfigurationProperties;

	/**
	 * Created by tangxiewen on 2016/5/31.
 	 */
	@ConfigurationProperties(prefix = 		DataSourceSettings.PREFIX)
	public class DataSourceSettings extends 	DruidDataSource {
  	  public static final String PREFIX = "druid.dataSource";

    private String mapperLocations;

    public String getMapperLocations() {
        return mapperLocations;
    }

    public void setMapperLocations(String mapperLocations) {
        this.mapperLocations = mapperLocations;
    }
    }
    
2.在创建个DataSourceAutoConfiguration用于注册SqlSessionFactoryBean，源码如下：

	import org.mybatis.spring.SqlSessionFactoryBean;
	import org.mybatis.spring.annotation.MapperScan;
	import org.slf4j.Logger;
	import org.slf4j.LoggerFactory;
	import 	org.springframework.beans.factory.annotation.Autowired;
	import org.springframework.boot.context.properties.EnableConfigurationProperties;
	import org.springframework.context.ApplicationContext;
	import org.springframework.context.annotation.Bean;
	import 	org.springframework.context.annotation.Configuration;

	import java.io.IOException;

	/**
	 * Created by tangxiewen on 2016/5/31.
	 */
		@Configuration
	@MapperScan(basePackages = {"com.mapper"})
	@EnableConfigurationProperties(DataSourceSettings.class)
	public class DataSourceAutoConfiguration {
    private static final Logger logger = 	LoggerFactory.getLogger(DataSourceAutoConfiguration.class);

    @Autowired
    DataSourceSettings settings;

    @Bean
    public SqlSessionFactoryBean sqlSessionFactory(ApplicationContext applicationContext) throws IOException {
        SqlSessionFactoryBean sqlSessionFactory = new SqlSessionFactoryBean();
        sqlSessionFactory.setDataSource(settings);
        sqlSessionFactory.setMapperLocations(applicationContext.getResources(settings.getMapperLocations()));
        return sqlSessionFactory;
    }
	}
    
最后要在src/main/resources/创建一个META-INF文件夹在里面放置一个spring.factories文件，主要用于告知springBoot用我们的配置代替默认的配置											
org.springframework.boot.autoconfigure.EnableAutoConfigur	ation=\com.jdbc.DataSourceAutoConfiguration
			
等于后面是类的全类名的形式即包名＋类名
###注意点
就是用使用myBatis时mapper中的java类和xml的包名要一致，还是就是用idea注意一下他的包结构，不然会报绑定错误！！！




    



