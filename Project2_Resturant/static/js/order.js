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
let orderList = document.querySelector(".orderMenu .orderList")
let OrderMenu = document.querySelector(".orderMenu")
let closebutton = document.querySelector("button.closeButton")
OrderNow.onclick= function(){
    if(OrderMenu.classList.contains("closeMenu")){
        OrderMenu.classList.remove("closeMenu")
        OrderMenu.classList.add("openMenu")
        document.body.style.overflow = "hidden"
    }
}
closebutton.onclick = function(){
    OrderMenu.classList.add("closeMenu")
    OrderMenu.classList.remove("openMenu")
    document.body.style.overflow = "auto"
    orderList.style.display="block"
    OrderedFoodForm.style.display="none"
    refactorFoodList()
}
document.addEventListener("click",function(e){
    if(e.target.classList.contains("img")){
        // open deatils
        // console.log(e.target.getAttribute("data-foodName"))
        let item = e.target 
        // console.log(item.firstElementChild.src)
        let itemimg = item.firstElementChild.src
        let itemName = item.getAttribute("data-foodName")
        console.log(itemimg , itemName)
        ToggleLists()
        SetOrderedFood(itemimg , itemName)
    }
})
function ToggleLists(){
    orderList.style.display="none"
    OrderedFoodForm.style.display="flex"
}
function SetOrderedFood(itemimg , itemName){
    orderedFoodImg.src = itemimg
    orderedFoodName.textContent = itemName
}




let OrderedFoodForm = document.querySelector(".orderedFood-form")
let orderedFoodImg = document.querySelector(".orderedFood-form img")
let orderedFoodName = document.querySelector(".orderedFood-form .FoodName")
let orderedFoodinput = document.querySelector('.orderedFood-form input')
let orderedFoodinput2 = document.querySelector('.orderedFood-form textarea')
let gobackButton = document.querySelector(".orderedFood-form .goback")
let sizelist = document.querySelectorAll(".orderedFood-form .orderedFood-info  .size ul li button")
let order = document.querySelector(".orderedFood-form .button")


document.addEventListener("click",function(e){
    if(e.target.classList.contains("sec1")){
        sizelist.forEach((element) => {
            if(element.classList.contains("clicked")){
                element.classList.remove("clicked")
            }  
        })
        e.target.classList.add("clicked")
    }
})
gobackButton.onclick = function(){
    orderList.style.display="block"
    OrderedFoodForm.style.display="none"
    refactorFoodList()
}
function refactorFoodList(){
    orderedFoodinput.value = "1"
    orderedFoodinput2.value = ""
    sizelist.forEach((e,i) =>{
        if(i===0){
            e.classList.add("clicked")
        }
        else{
            e.classList.remove("clicked")
        }
    })
}


function CreateItem(){
    let itme = document.createElement("div")
    item.classList.add(item)
    // let itemId = 
    let itemName = document.createElement("span")
    itemName.className = "itme-name"
}
// responsive lists fix
// ordre menu imgs fix
// add intro section 
// clean code
