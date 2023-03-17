// reads the input claim(s)
function readInput() {
    //todo: check if file uploaded (and if txt, pdf file)
    
    //else read from bar
    let text = document.getElementById('search-bar-input').value
    // check if empty
    if(text.length == 0) {
        return 1
    }

    console.log(text)
    return text
}

function openOverlay() {
    // to do: function chain that reads input or document & dislpays it in overlay
    // read the input
    readInput()
    // open overlay
    ocument.getElementById("overlay-container").style.width = "100%";
}

function closeOverlay() {
    document.getElementById("overlay-container").style.width = "0%";
}
