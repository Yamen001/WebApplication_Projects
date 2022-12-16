let list_toggler = document.querySelectorAll(".menuSction .list-toggler div")
let Lists = document.querySelectorAll(".menuSction .lists div.list")
console.log(Lists)

list_toggler.forEach(element => {
    document.addEventListener("click",function(e){
        if(e.target.classList.contains("sec")){
            if(element.classList.contains("checked")){
                element.classList.remove("checked")
            }
            e.target.classList.add("checked")
            // console.log(e.target.classList[1])
            PutList(e.target.classList[1])
        }
        else{
            console.log("no")
        }
    })
});
function PutList(list){
    console.log(list)
    Lists.forEach(function(e){
        if(e.classList.contains(list)){
            e.classList.add("addList")
            console.log("hre")
        }
        else{
            e.classList.remove("addList")
        }
    })
}