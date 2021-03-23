let time = 1500,
    indexImg = 0,
    images = document.querySelectorAll("#slider img")
    maxImg = images.length;


    function nextImage() {

        images[indexImg].classList.remove("select")

        indexImg++

        if(indexImg >= maxImg)
            indexImg = 0

        images[indexImg].classList.add("select")
    }


function start() {
    setInterval(() => {
        nextImage()
    }, time)
}


window.addEventListener("load", start)