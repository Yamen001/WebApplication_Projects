let state = false
let countres = document.querySelectorAll(".counter-circle span")
console.log(countres)
let timerSection = document.querySelector(".timer-section")
console.log(timerSection.getBoundingClientRect().top)


window.addEventListener('scroll',()=>{
    console.log(window.scrollY)
    if(window.scrollY> timerSection.getBoundingClientRect().top - 200  && !state){
        console.log('onnnnnn')
        state = true
        console.log(countres)
        countres.forEach((e)=>{
            let goal = e.parentElement.getAttribute("counter-data")
            startCount(e, goal)
        })
    }
})


function startCount(element , goal){
    let timer = setInterval(() => {
        if(element.textContent === goal){
            clearInterval(timer)
        }
        element.textContent++
    }, 3000 / goal);

}