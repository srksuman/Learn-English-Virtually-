//for joke
const joke_btn = document.getElementById('btn_joke')
const divJoke = document.getElementById('joke')
joke_btn.addEventListener('click',getJoke);

    async function getJoke() {
        const jokeData = await fetch("https://icanhazdadjoke.com/", {
          headers: {
            Accept: "application/json"
          }
        });
        const jokeObj = await jokeData.json();
        divJoke.innerHTML = jokeObj.joke;
        
      }


// For Word
const word_btn = document.getElementById('btn_Word')
const divWord = document.getElementById('Word')
const url = window.location.href+"word";
word_btn.addEventListener('click',getWord);

function getWord(){
  const xhr = new XMLHttpRequest()

  xhr.open("GET",url,true);
  // xhr.responseType = "json";
  // xhr.getResponseHeader('Content-type','application/json')

  xhr.onprogress =function() {
   console.log("working");
  }
  xhr.onload = ()=> {
   if(xhr.status === 200){
     let obj = JSON.parse(xhr.responseText)
     divWord.innerHTML = obj['word']
   }
  }
  xhr.send();
}

//for Facts

const btn_fact = document.getElementById('btn_Fact')
btn_fact.addEventListener('click',getFact);

const nxt_url = window.location.href+"fact"
function getFact(){
  xhr = new XMLHttpRequest()
  xhr.open("GET",nxt_url,true)
  xhr.onprogress =(err)=>{
  
  }
  xhr.onload = ()=>{
    if(xhr.status === 200){
      let res = JSON.parse(xhr.responseText)
      document.getElementById('Fact').innerHTML = res['fact']
    }
  }
  xhr.send()
}