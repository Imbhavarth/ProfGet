var audio = new Audio('assets/sentmessage.mp3');
var contactString = "<div class='social'> <a target='_blank' href='tel:+916363549133'> <div class='socialItem' id='call'><img class='socialItemI' src='images/phone.svg'/><label class='number'></label></label></div> </a> <a href='mailto:varshithvh@gmail.com'> <div class='socialItem'><img class='socialItemI' src='images/gmail.svg' alt=''></div> </a> <a target='_blank' href='https://github.com/Varshithvhegde'> <div class='socialItem'><img class='socialItemI' src='images/github.svg' alt=''></div> </a> <a target='_blank' href='https://wa.me/916363549133'> <div class='socialItem'><img class='socialItemI' src='images/whatsapp.svg' alt=''>";
var resumeString = "<img src='images/resume_thumbnail.png' class='resumeThumbnail'><div class='downloadSpace'><div class='pdfname'><img src='images/pdf.png'><label>Varshith V Hegde Resume.pdf</label></div><a href='assets/varshith_v_hegde_resume.pdf' download='varshith_v_hegde_resume.pdf'><img class='download' src='images/downloadIcon.svg'></a></div>";
var addressString = "<div class='mapview'><iframe src='https://www.google.com/maps/dir//Moodbidri+private+Bus+Stand,+Bus+Stand+Rd,+Mudbidri,+Karnataka+574227/@13.0639,74.9991985,15z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3ba4ab3d49331379:0x17be05cb5b69caa2!2m2!1d74.9957298!2d13.0680955?hl=en' class='map'></iframe></div><label class='add'><address>B2 'Asara'<br>Kodoli<br>Kolhapur, Maharashtra, INDIA 416114</address>";

function startFunction() {
    setLastSeen();
    waitAndResponce("intro");
}

function setLastSeen() {
    var date = new Date();
    var lastSeen = document.getElementById("lastseen");
    lastSeen.innerText = "last seen today at " + date.getHours() + ":" + date.getMinutes()
}


function closeFullDP() {
    var x = document.getElementById("fullScreenDP");
    if (x.style.display === 'flex') {
        x.style.display = 'none';
    } else {
        x.style.display = 'flex';
    }
}

function openFullScreenDP() {
    var x = document.getElementById("fullScreenDP");
    if (x.style.display === 'flex') {
        x.style.display = 'none';
    } else {
        x.style.display = 'flex';
    }
}


function isEnter(event) {
    if (event.keyCode == 13) {
        sendMsg();
    }
}

function sendMsg() {
    var input = document.getElementById("inputMSG");
    var ti = input.value;
    if (input.value == "") {
        return;
    }
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "sent");
    greendiv.setAttribute("class", "green");
    dateLabel.setAttribute("class", "dateLabel");
    greendiv.innerText = input.value;
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    setTimeout(function () { waitAndResponce(ti) }, 1500);
    input.value = "";
    playSound();
}

function waitAndResponce(inputText) {
    var lastSeen = document.getElementById("lastseen");
    lastSeen.innerText = "typing...";
    var name="";
    if(inputText.toLowerCase().includes("my name is")){
        name=inputText.substring(inputText.indexOf("is")+2);
        if(name.toLowerCase().includes("varshith")){
            sendTextMessage("Ohh! That's my name too");
            
        }
        inputText="input";
    }
    switch (inputText.toLowerCase().trim()) {
        case "intro":
            setTimeout(() => {
                sendTextMessage("Hello there 👋🏻,<br><br>My name is CHATBOT of <span class='bold'><a class='alink'>PROF-GET</a>.</span><br><br>I am a ChatBot as a Help Center for you... <span class='bold'>Tell me your doubts, I will guide you...👨🏻‍💻📚</span><br><br>Send <span class='bold'>'help'</span> to know more about me.<br>");
            }, 2000);
            break;
        
        

        case "help":
            sendTextMessage("<span class='sk'>Send Keyword to get what you want to know about me...<br>e.g<br><span class='bold'>'Gettingstarted'</span><br><span class='bold'>'Payment'</span><br><span class='bold'>'Safety'</span><br><span class='bold'>'Policies'</span><br><span class='bold'>'Technicalsupport'</span><br><span class='bold'>'FAQs'</span><br>");
            break;
        case "gettingstarted":
            sendTextMessage("To hire a freelancer or to work as a freelancer you have to setup your account and register your role on top right corner of website.<br> Thanks");
            break;
        case "payment":
            sendTextMessage("We have secure payment gateway for transaction. We have option of Paypal to tranfer your project budget.<br>Thanks");
            break;
        case "safety":
            sendTextMessage("Our Prof-Get is end-to-end secure website. All personal information belonging to you will be securely sent store in our database.<br> Thanks");
            break;
        case "policies":
            sendTextMessage("Our Prof-Get Policies are quite simple. We don't allow third party to enter in our environment and to join the conversation of any dealing.<br> Thanks");
            break;
        case "technicalsupport":
            sendTextMessage("Here is the toll-free number & mail-id for technical support.<br><br> +1 (123) 456 7890 <br><br><br> Mail Id : kvp2001.it@gmail.com <br> Thanks");
            break;
        case "faqs":
            sendTextMessage("You will get our FAQs section at the bottom of the home page. <br> Thanks");
            break;
                                    
        
        case "clear":
            clearChat();
            break;
        // case "about":

        //     break;
        case "time":
            var date = new Date();
            sendTextMessage("Current time is " + date.getHours() + ":" + date.getMinutes());
            break;

        case "date":
            var date = new Date();
            sendTextMessage("Current date is " + date.getDate() + "/" + date.getMonth() + "/" + date.getFullYear());
            break;

        case "hai":
            sendTextMessage("Hello there 👋🏻");
            sendTextMessage("<span class='sk'>Send Keyword to get what you want to know about me...<br>e.g<br><span class='bold'>'Gettingstarted'</span><br><span class='bold'>'Payment'</span><br><span class='bold'>'Safety'</span><br><span class='bold'>'Policies'</span><br><span class='bold'>'Technicalsupport'</span><br><span class='bold'>'FAQs'</span><br>");
            break;
        case "hello":
            sendTextMessage("Hello there 👋🏻");
            sendTextMessage("<span class='sk'>Send Keyword to get what you want to know about me...<br>e.g<br><span class='bold'>'Gettingstarted'</span><br><span class='bold'>'Payment'</span><br><span class='bold'>'Safety'</span><br><span class='bold'>'Policies'</span><br><span class='bold'>'Technicalsupport'</span><br><span class='bold'>'FAQs'</span><br>");
            break;
        
        case "hi":
            sendTextMessage("Hello there 👋🏻");
            sendTextMessage("<span class='sk'>Send Keyword to get what you want to know about me...<br>e.g<br><span class='bold'>'Gettingstarted'</span><br><span class='bold'>'Payment'</span><br><span class='bold'>'Safety'</span><br><span class='bold'>'Policies'</span><br><span class='bold'>'Technicalsupport'</span><br><span class='bold'>'FAQs'</span><br>");
            break;
        
        case "hey":
            sendTextMessage("Hello there 👋🏻");
            sendTextMessage("<span class='sk'>Send Keyword to get what you want to know about me...<br>e.g<br><span class='bold'>'Gettingstarted'</span><br><span class='bold'>'Payment'</span><br><span class='bold'>'Safety'</span><br><span class='bold'>'Policies'</span><br><span class='bold'>'Technicalsupport'</span><br><span class='bold'>'FAQs'</span><br>");
            break;
       

        case "Chatbot":
            sendTextMessage("Yes, that's me");
            break;
        case "Prof-Get":
            sendTextMessage("Yes, that's me");
            break;
 
        case "input":
            setTimeout(()=>{
                // sendTextMessage("What a coincidence!");
                sendTextMessage("Hello "+name+"! How are you?");
            },2000);
            
            break;
        default:
            setTimeout(() => {
                sendTextMessage("Hey I couldn't catch you...😢<br>Send 'help' to know more about usage.");
            }, 2000);
            break;
    }



}


function clearChat() {
    document.getElementById("listUL").innerHTML = "";
    waitAndResponce('intro');
}



function sendTextMessage(textToSend) {
    setTimeout(setLastSeen, 1000);
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.setAttribute("id", "sentlabel");
    dateLabel.id = "sentlabel";
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "received");
    greendiv.setAttribute("class", "grey");
    greendiv.innerHTML = textToSend;
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    playSound();
}


function sendResponse() {
    setTimeout(setLastSeen, 1000);
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "received");
    greendiv.setAttribute("class", "grey");
    dateLabel.setAttribute("class", "dateLabel");
    greendiv.innerText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. ";
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    playSound();
}

function playSound() {
    audio.play();
}