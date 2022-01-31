window.addEventListener('load',function(){
    var mainDivData = document.getElementById('mainCont').getElementsByTagName("img").setAttribute("class", "democlass");;
    console.log(mainDivData)
    // var mainDivData2 =mainDivData;
    arr = [];

    for (var i = 0; i < mainDivData.length; i++) {
        arr.push(mainDivData[i].src);
    }
    
    
})