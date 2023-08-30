function navtog() {
    var x = document.getElementById("menus");
    if (x.className === "menus") {
      x.className += " responsive";
    } else {
      x.className = "top";
    }
  } 