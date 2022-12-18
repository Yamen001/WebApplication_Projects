let list_toggler = document.querySelectorAll(".menuSction .list-toggler div")
let Lists = document.querySelectorAll(".menuSction .lists .list")
let Choosnlist
let lists = ["breakfast","lunch","dinner","dessert"]
document.addEventListener("click",function(e){
    if(e.target.classList.contains("sec")){
        list_toggler.forEach((element) => {
            if(element.classList.contains("checked")){
                element.classList.remove("checked")
            }  
        })
        e.target.classList.add("checked")
        Choosnlist = lists.indexOf(e.target.classList[1])
        PutList(Choosnlist)
    }
})
function PutList(list){
    Lists.forEach((e,i)=>{
        if(i===list){
            e.classList.add('d-flex')
            e.classList.remove('d-none')
            // e.setAttribute("data-aos","fade-left")
        }
        else(
            e.classList.add("d-none")
        )
    })
}

let OrderNow = document.querySelector("#orderNow")
let OrderMenu = document.querySelector(".orderMenu")
let closebutton = document.querySelector("button.closeButton")
OrderNow.onclick= function(){
    if(OrderMenu.classList.contains("closeMenu")){
        OrderMenu.classList.remove("closeMenu")
        OrderMenu.classList.add("openMenu")
        document.body.style.overflow = "hidden"
    }
    // else{
    //     OrderMenu.classList.add("closeMenu")
    // }
}
closebutton.onclick = function(){
    OrderMenu.classList.add("closeMenu")
    OrderMenu.classList.remove("openMenu")
    document.body.style.overflow = "auto"
}
document.addEventListener("click",function(e){
    if(e.target.classList.contains("img")){
        console.log("yesssimg")
    }
})

// ordre menu imgs fix
// add intro section 
// clean code
