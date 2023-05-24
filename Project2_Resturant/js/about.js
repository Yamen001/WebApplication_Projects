console.log('test')

let btn = document.querySelector("button.test")
let state = false
let countres = document.querySelectorAll(".counter-circle span")
console.log(countres)
btn.addEventListener("click",()=>{
    if(!state){
        console.log(countres)
        countres.forEach((e)=>{
            let goal = e.parentElement.getAttribute("counter-data")
            startCount(e, goal)
        })
    }
    console.log("hello")
    state = true
})


function startCount(element , goal){
    let timer = setInterval(() => {
        if(element.textContent === goal){
            clearInterval(timer)
        }
        element.textContent++
    }, 3000 / goal);

}