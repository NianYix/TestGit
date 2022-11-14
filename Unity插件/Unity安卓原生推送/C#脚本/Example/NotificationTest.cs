using UnityEngine;
using System.Collections;
using System;
using UnityEngine.UI;

public class NotificationTest : MonoBehaviour
{
    [SerializeField] private Text _mText;
    private string _textStr;
    //=========================NEW==========================
    public void TS_15_NotTimeout()
    {
        int offlineMaxTime = 15;
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);

        LocalNotification.SendNotification(timeSpan,
                                           "Title-01",
                                           "使用TimeSpan-15秒-无timeout",
                                           new Color32(0xff, 0x44, 0x44, 255),
                                           true, true, true/*, "app_icon", "boing", "default"*/);
    }
    public void TS_8dian_NotTimeout()
    {
        DateTime nowTime = DateTime.Now;
        DateTime nextTime = nowTime.AddDays(1);
        DateTime newTime = new DateTime(nextTime.Year, nextTime.Month, nextTime.Day, 8, 0, 0, DateTimeKind.Local);
        int offlineMaxTime = (int)(newTime - nowTime).TotalSeconds;
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);

        LocalNotification.SendNotification(timeSpan,
                                           "Title-02",
                                           "使用TimeSpan-8点-无timeout",
                                           new Color32(0xff, 0x44, 0x44, 255),
                                           true, true, true/*, "app_icon", "boing", "default"*/);
    }

    public void TS_15_Timeout()
    {
        //DateTime nowTime = DateTime.Now;
        //DateTime nextTime = nowTime.AddDays(1);
        //DateTime newTime = new DateTime(nextTime.Year, nextTime.Month, nextTime.Day, 8, 0, 0, DateTimeKind.Local);
        int offlineMaxTime = 15;//(newTime - nowTime).Seconds;
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);

        TimeSpan timeout = new TimeSpan(0, 0, 0, 10);
        LocalNotification.SendRepeatingNotification(timeSpan,
                                                    timeout,
                                                    "Title-03",
                                                    "使用TimeSpan-15秒-timeout",
                                                    new Color32(0xff, 0x44, 0x44, 255),
                                                    true, true, true/*, "app_icon", "boing", "default"*/);
    }

    public void TS_8dian_Timeout()
    {
        DateTime nowTime = DateTime.Now;
        DateTime nextTime = nowTime.AddDays(1);
        DateTime newTime = new DateTime(nextTime.Year, nextTime.Month, nextTime.Day, 8, 0, 0, DateTimeKind.Local);
        int offlineMaxTime = (int)(newTime - nowTime).TotalSeconds;
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);

        TimeSpan timeout = new TimeSpan(0, 0, 0, 10);
        LocalNotification.SendRepeatingNotification(timeSpan,
                                                    timeout,
                                                    "Title-04",
                                                    "使用TimeSpan-8点-timeout",
                                                    new Color32(0xff, 0x44, 0x44, 255),
                                                    true, true, true/*, "app_icon", "boing", "default"*/);
    }

    /// <summary>
    /// 两小时（不重复）
    /// </summary>
    public void TS00_3600_NotTimeout()
    {
        int offlineMaxTime = 3600;
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);
        _textStr += $"\n两小时:{timeSpan.TotalSeconds}";
        _mText.text = _textStr;

        LocalNotification.SendNotification(timeSpan,
                                           "Title-0010"+DateTime.Now,
                                           "使用TimeSpan-3600秒-无timeout",
                                           new Color32(0xff, 0x44, 0x44, 255),
                                           true, true, true/*, "app_icon", "boing", "default"*/);
    }

    /// <summary>
    /// 每天八点
    /// </summary>
    public void TS00_8dian_Timeout()
    {
        DateTime nowTime = DateTime.Now;
        DateTime nextTime = nowTime.AddDays(1);
        DateTime newTime = new DateTime(nextTime.Year, nextTime.Month, nextTime.Day, 8, 0, 0, DateTimeKind.Local);
        int offlineMaxTime =(int)((newTime - nowTime).TotalSeconds);
        int day = Mathf.CeilToInt(offlineMaxTime / (24 * 60 * 60));
        int hour = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60)) / (60 * 60));
        int minute = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60)) / (60));
        int second = Mathf.CeilToInt((offlineMaxTime - day * (24 * 60 * 60) - hour * (60 * 60) - minute * 60));
        TimeSpan timeSpan = new TimeSpan(day, hour, minute, second);

        TimeSpan timeout = new TimeSpan(1, 0, 0, 0);
        _textStr += $"\n八点 timeSpan:{timeSpan.TotalSeconds} \n timeout:{timeout.TotalSeconds}";
        _mText.text = _textStr;
        LocalNotification.SendRepeatingNotification(timeSpan,
                                                    timeout,
                                                    "Title-0011" + DateTime.Now,
                                                    "使用TimeSpan-8点-timeout",
                                                    new Color32(0xff, 0x44, 0x44, 255),
                                                    true, true, true/*, "app_icon", "boing", "default"*/);
    }

    //private void OnApplicationQuit()
    //{
    //    TS00_3600_NotTimeout();
    //    TS00_8dian_Timeout();
    //}
    //=========================OLD==========================
    void Awake()
    {
        LocalNotification.ClearNotifications();
    }

    public void OneTime()
    {
        LocalNotification.SendNotification(1, 5000, "Title", "Long message text", new Color32(0xff, 0x44, 0x44, 255));
    }

    public void OneTimeBigIcon()
    {
        LocalNotification.SendNotification(1, 5000, "Title", "Long message text with big icon", new Color32(0xff, 0x44, 0x44, 255), true, true, true, "app_icon");
    }

    public void OneTimeWithActions()
    {
        LocalNotification.Action action1 = new LocalNotification.Action("background", "In Background", this);
        action1.Foreground = false;
        LocalNotification.Action action2 = new LocalNotification.Action("foreground", "In Foreground", this);
        LocalNotification.SendNotification(1, 5000, "Title", "Long message text with actions", new Color32(0xff, 0x44, 0x44, 255), true, true, true, null, "boing", "default", action1, action2);
    }

    public void Repeating()
    {
        LocalNotification.SendRepeatingNotification(1, 5000, 60000, "Title", "Long message text", new Color32(0xff, 0x44, 0x44, 255));
    }

    public void Stop()
    {
        LocalNotification.CancelNotification(1);
    }

    public void OnAction(string identifier)
    {
        Debug.Log("Got action " + identifier);
    }


}
