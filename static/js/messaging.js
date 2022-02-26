var firebaseConfig = {
    apiKey: "AIzaSyDyuGBDhnQvPGFOeDQwIFTqYOju_7Y1VEw",
    authDomain: "bms-project-6d6a4.firebaseapp.com",
    projectId: "bms-project-6d6a4",
    storageBucket: "bms-project-6d6a4.appspot.com",
    messagingSenderId: "6566135751",
    appId: "1:6566135751:web:63d6d32bb4085c8c06bbe2"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


const messaging = firebase.messaging();

function showToken(currentToken) {
    console.log(currentToken)
}

messaging.onTokenRefresh(function () {
    messaging.getToken()
    .then(function(refreshedToken) {
        console.log('Token Refreshed.');
        sendTokenToServer(currentToken); 

        showToken(refreshedToken)

    })
    .catch(function (err) {
        console.log('Unable to retrieve refreshed token', err);
    });
});

messaging.onMessage(function (payload) {
console.log("Message received. ", payload);
// Update the UI to include the received message.
alert(JSON.stringify(payload,null,2))
});

function startMessagingApp(){
    console.log('Token Obtained');
    messaging.getToken().then(function(currentToken) {
        if(currentToken){
            showToken(currentToken);
            sendTokenToServer(currentToken);
            }
            else{
                console.log("It is not a valid instance for token,check permissions");
            }
    }).catch(function(err){
        console.log("There was an error trying to get the token.",err);
    })
}

function sendTokenToServer(currentToken) {
    fetch('http://127.0.0.1:8000/api/devices/',{
        method:"POST",
        headers:{
            'Content-Type' : "application/json",
            'X-CSRFToken':getCookie("csrftoken"),
            //'Authorization' : 'Token: '+ getCookie('token')
        },
        body: JSON.stringify({
            'registration_id': currentToken,
            'type':'web',
            //'csrfmiddlewaretoken' : getCookie('csrftoken')
        }),
        credentials:"include"
    }).then(function (response) {
        console.log(response)
    }).catch(function(err) {
        console.log(err);
    })
        
}

startMessagingApp();