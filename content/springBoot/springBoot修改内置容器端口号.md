Date:2016-7-13 21:08:11PM
Title:springBoot修改内置容器的端口号   
Tags:springBoot  

##SpringBoot修改内置容器的方法
1. 第一个最简单的方法就是在application.yml配置，配置方法如下：

	    # Server settings
         server:
         port: 8080
         
2. 实现EmbeddedServletContainerCustomizer的customize的方法  
        
        container.setPort(8000)
   



