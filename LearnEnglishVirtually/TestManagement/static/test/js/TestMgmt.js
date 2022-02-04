const url = window.location.href

const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
var timer;
const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b><i class="fas fa-stopwatch" style="font-size:24px;color:red"></i>  0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b><i class="fas fa-stopwatch" style="font-size:24px;color:red"></i>  ${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

     timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = `<b><i class="fas fa-stopwatch" style="font-size:24px;color:red"></i>  00:00</b>`
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }
        timerBox.innerHTML = `<b><i class="fas fa-stopwatch" style="font-size:24px;color:red"></i>  ${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans primary-radio" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
            
        });
        activateTimer(response.time)  
    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {} 
    data['csrfmiddlewaretoken'] = csrf[0].value
    
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    console.log(data)
   var datas = {
       'dt':'dt'
   }
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            clearInterval(timer)
            const results = response.results
            console.log(results)
            quizForm.classList.add('d-none')

            scoreBox.innerHTML = `${response.passed ? '<b> Congratulations! </b>' : '<b>Opps!!! :( </b>'}<b>Your Result is ${response.score.toFixed(2)}% </b><br><br>`

            results.forEach(res=>{
                const collapseDiv = document.getElementById('collapseBtn');
                collapseDiv.innerHTML = ` <a class="btnn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                View Test Details
              </a> 
              
              `
              console.log("Hello")
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){

                    // resDiv.innerHTML += `<i class="fa fa-check-circle" style="font-size:24px"></i>${question}`
                    const cls = ['container', 'p-4', 'text-light', 'h2', 'rounded']
                    resDiv.classList.add(...cls)

                    if (resp=='not answered') {
                        resDiv.innerHTML += `<i class="fas fa-times-circle" style="font-size:24px"></i> ${question}`
                        resDiv.innerHTML += '- Not Answered'
                        resDiv.classList.add('bg-danger')
                    }
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.innerHTML += `<i class="fa fa-check-circle" style="font-size:24px"></i> ${question}`
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` Answered: ${answer}`
                        } else {
                            resDiv.innerHTML += `<i class="fas fa-times-circle" style="font-size:24px"></i> ${question}`
                            resDiv.classList.add('bg-danger')
                            // resDiv.innerHTML += ` | Wrong Answer`
                            // resDiv.innerHTML += ` | Correct Answer: ${correct}`
                            resDiv.innerHTML += ` | Answered: ${answer}`
                        }
                    }
                }
                resultBox.append(resDiv)
            })
        },
        error: function(error){
            console.log("someting went wrong")
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})