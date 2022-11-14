package com.hw.unitynotification;

import android.annotation.TargetApi;
import android.app.Activity;
import android.app.AlarmManager;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.media.AudioAttributes;
import android.media.RingtoneManager;
import android.content.res.Resources;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import com.unity3d.player.UnityPlayer;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import androidx.core.app.TaskStackBuilder;
import androidx.core.app.NotificationCompat;

public class UnityNotificationManager  extends BroadcastReceiver {
   private static Set<String> channels = new HashSet<>();

   public static void CreateChannel(String identifier, String name, String description, int importance, String soundName, int enableLights, int lightColor, int enableVibration, long[] vibrationPattern, String bundle) {
     if (Build.VERSION.SDK_INT < 26) {
       return;
     }
     channels.add(identifier);

     NotificationManager nm = (NotificationManager)UnityPlayer.currentActivity.getSystemService("notification");
     NotificationChannel channel = new NotificationChannel(identifier, name, importance);
     channel.setDescription(description);
     if (soundName != null) {
       Resources res = UnityPlayer.currentActivity.getResources();
       int id = res.getIdentifier("raw/" + soundName, null, UnityPlayer.currentActivity.getPackageName());
       AudioAttributes audioAttributes = (new AudioAttributes.Builder()).setUsage(5).setContentType(4).build();
       channel.setSound(Uri.parse("android.resource://" + bundle + "/" + id), audioAttributes);
     }
     channel.enableLights((enableLights == 1));
     channel.setLightColor(lightColor);
     channel.enableVibration((enableVibration == 1));
     if (vibrationPattern == null)
       vibrationPattern = new long[] { 1000L, 1000L };
     channel.setVibrationPattern(vibrationPattern);
     nm.createNotificationChannel(channel);
   }

   @TargetApi(24)
   private static void createChannelIfNeeded(String identifier, String name, String soundName, boolean enableLights, boolean enableVibration, String bundle) {
     if (channels.contains(identifier))
       return;
     channels.add(identifier);

     CreateChannel(identifier, name, identifier + " notifications", 3, soundName, enableLights ? 1 : 0, -16711936, enableVibration ? 1 : 0, null, bundle);
   }


   public static void SetNotification(int id, long delayMs, String title, String message, String ticker, int sound, String soundName, int vibrate, int lights, String largeIconResource, String smallIconResource, int bgColor, String bundle, String channel, ArrayList<NotificationAction> actions) {
     if (Build.VERSION.SDK_INT >= 26) {
       if (channel == null)
         channel = "default";
       createChannelIfNeeded(channel, title, soundName, (lights == 1), (vibrate == 1), bundle);
     }

     Activity currentActivity = UnityPlayer.currentActivity;
     AlarmManager am = (AlarmManager)currentActivity.getSystemService("alarm");
     Intent intent = new Intent((Context)currentActivity, UnityNotificationManager.class);
     intent.putExtra("ticker", ticker);
     intent.putExtra("title", title);
     intent.putExtra("message", message);
     intent.putExtra("id", id);
     intent.putExtra("color", bgColor);
     intent.putExtra("sound", (sound == 1));
     intent.putExtra("soundName", soundName);
     intent.putExtra("vibrate", (vibrate == 1));
     intent.putExtra("lights", (lights == 1));
     intent.putExtra("l_icon", largeIconResource);
     intent.putExtra("s_icon", smallIconResource);
     intent.putExtra("bundle", bundle);
     intent.putExtra("channel", channel);
     Bundle b = new Bundle();
     b.putParcelableArrayList("actions", actions);
     intent.putExtra("actionsBundle", b);
     if (Build.VERSION.SDK_INT >= 23) {
       am.setExact(0, System.currentTimeMillis() + delayMs, PendingIntent.getBroadcast((Context)currentActivity, id, intent, 134217728));
     } else {
       am.set(0, System.currentTimeMillis() + delayMs, PendingIntent.getBroadcast((Context)currentActivity, id, intent, 134217728));
     }
   }


   public static void SetRepeatingNotification(int id, long delayMs, String title, String message, String ticker, long rep, int sound, String soundName, int vibrate, int lights, String largeIconResource, String smallIconResource, int bgColor, String bundle, String channel, ArrayList<NotificationAction> actions) {
     if (Build.VERSION.SDK_INT >= 26) {
       if (channel == null)
         channel = "default";
       createChannelIfNeeded(channel, title, soundName, (lights == 1), (vibrate == 1), bundle);
     }

     Activity currentActivity = UnityPlayer.currentActivity;
     AlarmManager am = (AlarmManager)currentActivity.getSystemService("alarm");
     Intent intent = new Intent((Context)currentActivity, UnityNotificationManager.class);
     intent.putExtra("ticker", ticker);
     intent.putExtra("title", title);
     intent.putExtra("message", message);
     intent.putExtra("id", id);
     intent.putExtra("color", bgColor);
     intent.putExtra("sound", (sound == 1));
     intent.putExtra("soundName", soundName);
     intent.putExtra("vibrate", (vibrate == 1));
     intent.putExtra("lights", (lights == 1));
     intent.putExtra("l_icon", largeIconResource);
     intent.putExtra("s_icon", smallIconResource);
     intent.putExtra("bundle", bundle);
     intent.putExtra("channel", channel);
     Bundle b = new Bundle();
     b.putParcelableArrayList("actions", actions);
     intent.putExtra("actionsBundle", b);
     am.setRepeating(0, System.currentTimeMillis() + delayMs, rep, PendingIntent.getBroadcast((Context)currentActivity, id, intent, 134217728));
   }


   public void onReceive(Context context, Intent intent) {
     Log.d("tag", context.toString());
     NotificationManager notificationManager = (NotificationManager)context.getSystemService("notification");

     String ticker = intent.getStringExtra("ticker");
     String title = intent.getStringExtra("title");
     String message = intent.getStringExtra("message");
     String s_icon = intent.getStringExtra("s_icon");
     String l_icon = intent.getStringExtra("l_icon");
     int color = intent.getIntExtra("color", 0);
     String bundle = intent.getStringExtra("bundle");
     Boolean sound = Boolean.valueOf(intent.getBooleanExtra("sound", false));
     String soundName = intent.getStringExtra("soundName");
     Boolean vibrate = Boolean.valueOf(intent.getBooleanExtra("vibrate", false));
     Boolean lights = Boolean.valueOf(intent.getBooleanExtra("lights", false));
     int id = intent.getIntExtra("id", 0);
     String channel = intent.getStringExtra("channel");
     Bundle b = intent.getBundleExtra("actionsBundle");
     ArrayList<NotificationAction> actions = null;
     if (b != null && b.containsKey("actions")) {
       actions = b.getParcelableArrayList("actions");
     }

     Resources res = context.getResources();

     Intent notificationIntent = context.getPackageManager().getLaunchIntentForPackage(bundle);

     TaskStackBuilder stackBuilder = TaskStackBuilder.create(context);
     stackBuilder.addNextIntent(notificationIntent);

     PendingIntent pendingIntent = PendingIntent.getActivity(context, 0, notificationIntent, 134217728);

     if (channel == null) {
       channel = "default";
     }
     NotificationCompat.Builder builder = new NotificationCompat.Builder(context, channel);

     builder.setContentIntent(pendingIntent)
       .setAutoCancel(true)
       .setContentTitle(title)
       .setContentText(message);

     if (Build.VERSION.SDK_INT >= 21) {
       builder.setColor(color);
     }
     if (ticker != null && ticker.length() > 0) {
       builder.setTicker(ticker);
     }
     if (s_icon != null && s_icon.length() > 0) {
       builder.setSmallIcon(res.getIdentifier(s_icon, "drawable", context.getPackageName()));
     }
     if (l_icon != null && l_icon.length() > 0) {
       builder.setLargeIcon(BitmapFactory.decodeResource(res, res.getIdentifier(l_icon, "drawable", context.getPackageName())));
     }
     if (sound.booleanValue()) {
       if (soundName != null) {
         int identifier = res.getIdentifier("raw/" + soundName, null, context.getPackageName());
         builder.setSound(Uri.parse("android.resource://" + bundle + "/" + identifier));
       } else {
         builder.setSound(RingtoneManager.getDefaultUri(2));
       }
     }
     if (vibrate.booleanValue()) {
       builder.setVibrate(new long[] { 1000L, 1000L });
     }

     if (lights.booleanValue()) {
       builder.setLights(-16711936, 3000, 3000);
     }
     if (actions != null) {
       for (int i = 0; i < actions.size(); i++) {
         NotificationAction action = actions.get(i);
         int icon = 0;
         if (action.getIcon() != null && action.getIcon().length() > 0)
           icon = res.getIdentifier(action.getIcon(), "drawable", context.getPackageName());
         builder.addAction(icon, action.getTitle(), buildActionIntent(action, i, context));
       }
     }

     Notification notification = builder.build();
     notificationManager.notify(id, notification);
   }

   private static PendingIntent buildActionIntent(NotificationAction action, int id, Context context) {
     Intent intent = new Intent(context, UnityNotificationActionHandler.class);
     intent.putExtra("id", id);
     intent.putExtra("gameObject", action.getGameObject());
     intent.putExtra("handlerMethod", action.getHandlerMethod());
     intent.putExtra("actionId", action.getIdentifier());
     intent.putExtra("foreground", action.isForeground());
     return PendingIntent.getBroadcast(context, id, intent, 134217728);
   }


   public static void CancelPendingNotification(int id) {
     Activity currentActivity = UnityPlayer.currentActivity;
     AlarmManager am = (AlarmManager)currentActivity.getSystemService("alarm");
     Intent intent = new Intent((Context)currentActivity, UnityNotificationManager.class);
     PendingIntent pendingIntent = PendingIntent.getBroadcast((Context)currentActivity, id, intent, 134217728);
     am.cancel(pendingIntent);
   }


   public static void ClearShowingNotifications() {
     Activity currentActivity = UnityPlayer.currentActivity;
     NotificationManager nm = (NotificationManager)currentActivity.getSystemService("notification");
     nm.cancelAll();
   }
}
