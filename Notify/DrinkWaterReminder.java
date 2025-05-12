import java.awt.*;
import java.awt.TrayIcon.MessageType;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class DrinkWaterReminder {
    public static void main(String[] args) {
        if (SystemTray.isSupported()) {
            ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
            scheduler.scheduleAtFixedRate(new Runnable() {
                public void run() {
                    showNotification("Hydration Reminder", "Time to drink some water!");
                }
            }, 0, 60, TimeUnit.MINUTES); // Notify every 60 minutes
        } else {
            System.err.println("System tray not supported!");
        }
    }

    private static void showNotification(String title, String message) {
        try {
            SystemTray tray = SystemTray.getSystemTray();
            Image image = Toolkit.getDefaultToolkit().createImage("path-to-icon.png");
            TrayIcon trayIcon = new TrayIcon(image, "Drink Water Reminder");
            trayIcon.setImageAutoSize(true);
            trayIcon.setToolTip("Drink Water Reminder");
            tray.add(trayIcon);

            trayIcon.displayMessage(title, message, MessageType.INFO);
        } catch (AWTException e) {
            e.printStackTrace();
        }
    }
}
