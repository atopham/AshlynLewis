function editDropdown(id){
    var dropdown = document.getElementById(id)
    if (dropdown.style.display == "none"){
        dropdown.style.display = 'table-row'
    }
    else{
        dropdown.style.display = "none"
    }
    
}