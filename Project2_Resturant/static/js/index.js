var lastScrollTop;
let navbar = document.querySelector('.navbar');
window.addEventListener('scroll',function(){
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if(scrollTop > lastScrollTop){
        var navbarHight = Number.parseInt(getComputedStyle(navbar).height)
        navbar.style.top= -Number(navbarHight+10)+'px'
        // close the list too
    }
    else{
    navbar.style.top='0';
    }
    lastScrollTop = scrollTop;
});
let landingfood = document.querySelector(".landing img")
let i =1
setInterval(function(){
    if(i === 1){
        landingfood.src = `/static/imgs/landingfood${i}.png`
        // landingfood.style.animation = ""
        i++
    }
    else if(i ===2){
        landingfood.src = `/static/imgs/landingfood${i}.png`
        // landingfood.style.animation = ""
        i++
    }
    else{
        landingfood.src = `/static/imgs/landingfood${i}.png`
        // landingfood.style.animation = "fading 2s"
        i = 1
    }
},10000)
console.log("test")




// start comment section
let comments = [
    "Adults should be able to go out and enjoy a quiet dinner. There are plenty of family restaurants that allow children... should be nothing wrong with having a few for adults.",
    "Coffe smells better than is tastes and chocolate tastes better than it smells.",
    "No one should suffer from food insecurity when they work 40 hours a week.",
    "i like dessert made with lemon better than chocolate - lemo meringue pie over chocolate cake.",
    "Different pasta shapes MAKE THE PASTA TASTE DIFFERENT , shells being the best."
]
let comment = document.querySelector(".Comments .container .commentSection")
let beforeBtn = document.querySelector(".Comments .container .UserDeatils .control #left")
let AfterBtn = document.querySelector(".Comments .container .UserDeatils .control #rigth")
let CommentIndex = 0
AfterBtn.onclick = function(){
    comment.removeChild(comment.lastElementChild)
    let text1 = document.createElement("p")
    text1.classList.add("fs-5")
    text1.setAttribute("data-aos","fade")
    text1.setAttribute("data-aos-duration","1000")
    CommentIndex++
    if(CommentIndex === comments.length-1){
        CommentIndex = 0
    }
    text1.textContent = comments[CommentIndex]
    comment.appendChild(text1)    
    console.log(CommentIndex)
}
beforeBtn.onclick = function(){
    comment.removeChild(comment.lastElementChild)
    let text1 = document.createElement("p")
    text1.setAttribute("data-aos","fade")
    text1.textContent = comments[CommentIndex]
    CommentIndex--
    if(CommentIndex === 0){
        CommentIndex = comments.length - 1
    }
    comment.appendChild(text1)  
    console.log(CommentIndex)

}