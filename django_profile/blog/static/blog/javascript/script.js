//toogle navigation menu

const toogleMenu = ()=>{

    const burger = document.querySelector(".burger");
    const links = document.querySelector(".navLinks");

    burger.addEventListener("click", openNav)

    function openNav(){
        links.classList.toggle("navLinks-open");
        burger.classList.toggle("burger-close");
    }
}

toogleMenu();