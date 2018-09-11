document.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
document.type = 'text/javascript';


$(function(){
  $("#socialNav").load("socialNav.html"); 
});

/* typewriter */

partA = function(callback) {
        function setupTypewriter(t) {
            var HTML = t.innerHTML;

            t.innerHTML = "";

            var cursorPosition = 0,
                tag = "",
                writingTag = false,
                tagOpen = false,
                typeSpeed = 1,
            tempTypeSpeed = 1;

            var type = function() {

                if (writingTag === true) {
                    tag += HTML[cursorPosition];
                }

                if (HTML[cursorPosition] === "<") {
                    tempTypeSpeed = 0;
                    if (tagOpen) {
                        tagOpen = false;
                        writingTag = true;
                    } else {
                        tag = "";
                        tagOpen = true;
                        writingTag = true;
                        tag += HTML[cursorPosition];
                    }
                }
                if (!writingTag && tagOpen) {
                    tag.innerHTML += HTML[cursorPosition];
                }
                if (!writingTag && !tagOpen) {
                    if (HTML[cursorPosition] === " ") {
                        tempTypeSpeed;
                    }
                    else {
                        tempTypeSpeed = (Math.random() * typeSpeed);
                    }
                    t.innerHTML += HTML[cursorPosition];
                }
                if (writingTag === true && HTML[cursorPosition] === ">") {
                    tempTypeSpeed = (Math.random() * typeSpeed);
                    writingTag = false;
                    if (tagOpen) {
                        var newSpan = document.createElement("span");
                        t.appendChild(newSpan);
                        newSpan.innerHTML = tag;
                        tag = newSpan.firstChild;
                    }
                }

                cursorPosition += 1;
                if (cursorPosition < HTML.length - 1) {
                    setTimeout(type, tempTypeSpeed/10);
                }
                else{
                    callback();
                }
            };

            return {
                type: type
            };
        }  
        
        var typer = document.getElementsByClassName('typewriter');
        typewriter = setupTypewriter(typewriter);
        typewriter.type(); 
    }