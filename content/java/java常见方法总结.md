Date:7/12/2016 3:20:35 PM 
Title:java常见方法总结
##java常见方法总结
###1.指定随机数的生成范围
	public int getRandomRangeNum(int start,int end){
       int result=start+(int)(Math.random()*(end-start));
       return result;
	}