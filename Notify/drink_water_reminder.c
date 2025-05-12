#include <libnotify/notify.h>
#include <unistd.h> // for sleep function
void send_notification(const char *title, const char *message) {
    notify_init("Drink Water Reminder");
    NotifyNotification *n = notify_notification_new(title, message, NULL);
    notify_notification_set_timeout(n, 3000); // Timeout in milliseconds
    notify_notification_show(n, NULL);
    g_object_unref(G_OBJECT(n));
    notify_uninit();
}
int main() {
    const int interval = 60 * 60; // Time interval between notifications in seconds (60 minutes)
    while (1) {
        send_notification("Hydration Reminder", "Time to drink some water!");
        sleep(interval);
    }
    return 0;
}