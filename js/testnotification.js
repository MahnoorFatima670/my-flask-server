const admin = require('firebase-admin');
admin.messaging().sendToDevice(
    '<device-token>', // Replace with an actual device token
    {
        notification: {
            title: 'Test Notification',
            body: 'This is a test notification'
        }
    }
)
.then(response => {
    console.log('Notification sent successfully:', response);
})
.catch(error => {
    console.error('Error sending notification:', error);
});

