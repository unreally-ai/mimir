// reads the input claim(s)
function readInput() {
    //todo: check if file uploaded (and if txt, pdf file)
    if (1 == 2) {
        print("math is no more")
        return 666
    }
    else {
        //else read from bar
        let text = document.getElementById('search-bar-input').value
        // check if empty
        if(text.length == 0) {
            return 1
        }
        
        console.log(text)
        return text
    }
}

function changeButtonMode(buttonState) {
    if (buttonState == 0) {
        document.getElementById("gobuttonDefault").style.display = "none"; 
        document.getElementById("gobuttonLoad").style.display = "block";
    }
    else if (buttonState == 1) {
        document.getElementById("gobuttonDefault").style.display = "block"; 
        document.getElementById("gobuttonLoad").style.display = "none";
    }
}

function openOverlay() {
    // read the input
    readInput()

    // todo: call backend to get prediciton

    // stop loading

    // open overlay
    document.getElementById("overlay-container").style.height = "100%";
}

function closeOverlay() {
    document.getElementById("overlay-container").style.height = "0%";
    changeButtonMode(1)
}
