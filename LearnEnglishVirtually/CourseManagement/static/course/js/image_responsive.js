window.addEventListener('load',function(){
    var divTag = document.getElementById('mainCont')
    
    // divTag.style.justifyContent = "center";
    // var styles = {
    // "font-size": "larger !important",
    // "margin-top": "15px !important",
    // "margin-bottom": "15px !important"
    // }

    
    // Object.assign(divTag.getElementsByTagName("h1")[0].style,styles);
    // divTag.getElementsByTagName("h1")[0].setAttribute("class","h1_tag");
    divTag.getElementsByTagName("h1")[0].setAttribute("style", "margin-top: 15px;font-weight:bolder; margin-bottom: 15px; font-size: 50px !important; text-align:center !important");
    var tables = divTag.getElementsByTagName("TABLE");
    // console.log(divTag);
    for (let i = 0; i < tables.length; i++) {
        tables[i].setAttribute('class','table table-hover');
        tables[i].setAttribute('style','justify-content:center;');
        $( tables[i] ).wrapAll( "<div style=overflow-x:auto;} />");
      }

      
      var paragraph = divTag.getElementsByTagName("P");
      for(var i=0;i<paragraph.length;i++){
        //   console.log(paragraph[i].textContent)
          paragraph[i].setAttribute("style","text-align: justify;");
          if(paragraph[i].innerHTML == "&nbsp;" ){
            // console.log("empty") ;
            paragraph[i].innerHTML="";
            
          }
      }

      var h2_tags = divTag.getElementsByTagName('H2')
      for (var i=0;i<h2_tags.length;i++){
          h2_tags[i].setAttribute("style","font-weight:bold; font-size:30px; margin:15px 0 15px 0;");
      }
    
    for(var i=0; i<divTag.getElementsByTagName("img").length;i++){
        divTag.getElementsByTagName("img")[i].setAttribute("class", "demo-image img-pop-up rounded"); 
    }
    
    
})