本插件主要是用于移动本地端推送。（仅在Android端测试过推送，IOS端暂未测试）
一共有三个文件夹：
	1、放入安卓文件夹：将文件夹里的 unitynotification 文件夹放入如 图片1 所示的文件目录；
						AndroidManifest.xml文件里的两行代码（图片2所示）拷入对应工程的AndroidManifest.xml文件里；
	2、放入Unity工程文件夹：将文件夹里的 Android 文件夹放入如 图片3 所示的Unity工程目录（Assets\Plugins）里；
	3、C#脚本：LocalNotification.cs脚本里面是调用unitynotification文件夹里的java脚本方法；
				Example文件夹：NotificationTest.cs脚本调用LocalNotification.cs脚本的测试代码，可以参照里面的方法，不用拷贝。

主要参考链接：
安卓推送git仓库链接：https://github.com/Agasper/unity-android-notifications
库的引入问题： https://blog.csdn.net/qq_42351033/article/details/121307101
AndroidManifest增加receiver：http://t.zoukankan.com/GuyaWeiren-p-4830854.html