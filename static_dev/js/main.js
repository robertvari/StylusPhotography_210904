let menu_visible = false

function mobile_menu_clicked(){
    let nav_menu = document.getElementById("nav-menu")

    if(menu_visible){
        // hide menu
        menu_visible = false
        nav_menu.style.display = "none"
    }else{
        // show menu
        menu_visible = true
        nav_menu.style.display = "flex"
    }
}
