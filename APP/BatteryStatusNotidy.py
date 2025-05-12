# On Windows, make sure "Focus Assist" is disabled.


from plyer import notification, battery

# Get battery status
battery_status = battery.status
battery_limit=10
print(battery_status)

# Check if battery information is available
if battery_status:
    battery_percentage = battery_status.get('percentage', None)
    charging_status = battery_status.get('isCharging', None)
    
    # Trigger notification if battery is below 20%
    if battery_percentage is not None and battery_percentage > battery_limit:
        notification.notify(
            title="Low Battery Warning",
            message=f"Battery level is critically low: {battery_percentage}%. Please charge your device! Charinging",
            app_name="Battery Monitor"
            
                
        )
    else:
        notification.notify(
            title="Your Battery Is Charged ",
            message=f"Battery level is sufficient: {battery_percentage}%",
            app_name="Battery Monitor"
        )
else:
    notification.notify(
        title="Battery Notification",
        message="Battery status information is not available.",
        app_name="Battery Monitor"
    )    
