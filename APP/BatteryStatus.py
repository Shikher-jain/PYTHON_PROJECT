# On Windows, make sure "Focus Assist" is disabled.

from plyer import notification, battery

# Show a notification
notification.notify(
    title="Battery Status",
    message=f"Battery level: {battery.status.get('percentage', 'Unknown')}%",
    app_name="Battery Monitor"
)
