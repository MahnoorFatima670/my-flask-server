const admin = require('firebase-admin');
const serviceAccount = require('./serviceAccountKey.json');  // Replace this with the correct path to your JSON file

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

module.exports = admin;


