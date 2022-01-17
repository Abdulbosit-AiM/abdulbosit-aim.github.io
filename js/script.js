const heading = document.querySelector('h1')
const heading2 = document.querySelector('h2')
const main = document.querySelector('main')

heading.onclick = () => { hide(heading) }
heading2.onclick = () => { hide(heading2) }

function hide(elem){
    elem.style.visibility = 'hidden'
}


document.body.onkeyup = function(e){
    if(e.keyCode == 32){
        main.innerHTML = ''
    }
}