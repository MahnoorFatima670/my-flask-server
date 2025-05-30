const admin = require('./firebase');  // Import Firebase configuration

const sendPushNotification = async (deviceToken, message) => {
    const payload = {
        notification: {
            title: message.title,
            body: message.body,
        },
    };

    try {
        const response = await admin.messaging().sendToDevice(deviceToken, payload);
        console.log('Notification sent successfully:', response);
    } catch (error) {
        console.error('Error sending notification:', error);
    }
};

module.exports = sendPushNotification;
