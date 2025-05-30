const express = require('express');  // Import Express
const sendPushNotification = require('./notifications'); // Import the notification function

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send('Server is running...');
});

// Test Route to Send Notification
app.get('/send-notification', async (req, res) => {
    const userDeviceToken = 'dummytoken123456';  // Replace with the real device token
    const message = {
        title: 'Reminder!',
        body: 'It’s time to check your mood!',
    };

    try {
        await sendPushNotification(userDeviceToken, message);
        res.send('Push notification sent successfully!');
    } catch (error) {
        res.status(500).send('Error sending notification');
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
