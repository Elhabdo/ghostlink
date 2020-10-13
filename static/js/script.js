function copy (text) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
    var btn_c = document.getElementById("cpy")
  btn_c.innerHTML= "Copied!"
}