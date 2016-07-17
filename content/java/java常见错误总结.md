Date:7/12/2016 2:39:32 PM 
Title:java错误归纳
Category: java
Tags: java
##java错误归纳
1. 使用BigDecimal的divide时候要设置精确的小数点，不然在除不尽的时候会抛出java.lang.ArithmeticException: Non-terminating decimal expansion; no exact representable decimal result. 
2. Integer能使用等于号的范围是-128~127