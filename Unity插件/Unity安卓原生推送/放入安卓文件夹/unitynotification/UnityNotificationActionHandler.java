package com.hw.unitynotification;

import android.app.NotificationManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import com.unity3d.player.UnityPlayer;
import com.unity3d.player.UnityPlayerActivity;

public class UnityNotificationActionHandler
  extends BroadcastReceiver
 {
  public void onReceive(Context context, Intent intent) {
     int id = intent.getIntExtra("id", 0);
     String gameObject = intent.getStringExtra("gameObject");
     String handlerMethod = intent.getStringExtra("handlerMethod");
     String actionId = intent.getStringExtra("actionId");
     boolean foreground = intent.getBooleanExtra("foreground", true);

     NotificationManager notificationManager = (NotificationManager)context.getSystemService("notification");
     notificationManager.cancel(id);

     if (foreground) {
       Intent launchIntent = new Intent(context, UnityPlayerActivity.class);
       launchIntent.setPackage(null);
       launchIntent.addFlags(805306368);
       context.startActivity(launchIntent);
     }

     UnityPlayer.UnitySendMessage(gameObject, handlerMethod, actionId);
   }
 }
