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
