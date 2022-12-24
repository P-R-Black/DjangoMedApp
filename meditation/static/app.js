const hamburger = document.querySelector('.hamburger_menu');
const navElements = document.querySelector('.nav_elements');

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navElements.classList.toggle("active");
    console.log('Check 1')
})

const test = document.querySelectorAll(".nav_elem").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navElements.classList.toggle("active");
}))

// Get Time of Day
    const setGreeting = () => {
        const greeting = document.querySelector('.greeting');
        let today = new Date();
        let hour = today.getHours();
        if (hour < 12){
            greeting.textContent = "Good Morning"
        } else if(hour < 18 ){
            greeting.textContent = "Good Afternoon"
        } else {
            greeting.textContent = "Good Evening"
        }
}

    const song = document.querySelector('.meditation_choice');
    const ending = document.querySelector('.end_of_mediation');
    const play = document.querySelector('.start_meditation');

    const timeDisplay = document.querySelector('.time_display');
    const timeSelect = document.querySelectorAll('.times button');
    const timeSelected = document.querySelector('.select_time');

    const currSound = document.querySelector('.current_sound');
    const sounds = document.querySelectorAll('.sounds button')

    const soundBtn = document.querySelectorAll('.sound_btn');
    const newSong = document.getElementById('myAudio')

    const moods = document.querySelectorAll('.mood_btn');

    let ul = document.getElementById('unordered_mood');

    let volume = document.querySelector('.meditation_choice').volume;
    document.querySelector('.meditation_choice').volume = 0.5;

    let volume_two = document.querySelector('.end_of_mediation').volume;
    document.querySelector('.end_of_mediation').volume_two = 0.1;


    let fakeDuration = 10; //300
    let duration = 0;

    song.autoplay = false;
    ending.autoplay = false;


    // Select Sound to Meditate To
    const selectSound = () => {
        sounds.forEach(options => {
        options.addEventListener('click', function(){
        currSound.textContent = options.textContent
        soundBtn.src = this.getAttribute('data-sound');
        console.log('soundBtn:', soundBtn.src)
        newSong.src = '/../media/' + soundBtn.src
        // console.log('newSong:', newSong.src)
            })
        })
        return newSong.src
    }


    // play audio
    const playAudio = song => {
        if (song.paused){
            song.play();
        } else {
            song.pause();
        }
    };


    //Play sound
    play.addEventListener("click", function(e) {
        e.preventDefault()
  	    playAudio(song);
    });


    // Select Mood
    const selectMood = () => {
        moods.forEach(moodMove => {
        moodMove.addEventListener('click', function(){
        li = document.createElement("li")
        ul.appendChild(li).classList.add('current_mood')
        const currMoods = document.querySelector('.current_mood');
        li.textContent = currMoods.textContent
        currMoods.textContent = moodMove.innerHTML;

        if (ul.childNodes.length > 6) {
            ul.removeChild(ul.firstChild);
            alert('Max is 5')
                }
            });
        });

    }


    // Select Time
    const theSelectedTime = () => {
        timeSelect.forEach(option => {
        option.addEventListener('click', function(){
        fakeDuration = this.getAttribute('data-time');
        timeDisplay.textContent = `${Math.floor(fakeDuration / 60)}:${Math.floor(fakeDuration % 60)}0`;
        timeSelected.textContent = timeDisplay.textContent.split(':')[0] + ' Minutes'
            });
        });
    }

    const timerCountdown = () => {
        song.ontimeupdate = () => {
            let currentTime = song.currentTime;
            let elapsed = fakeDuration - currentTime;
            let seconds = Math.floor(elapsed % 60);
            let minutes = Math.floor(elapsed / 60);

            // Animate the text
            if (seconds < 10){
                timeDisplay.textContent = `${minutes}:0${seconds}`;
            } else {
                timeDisplay.textContent = `${minutes}:${seconds}`;
            }

            if (currentTime >= fakeDuration) {
                song.pause();
                song.currentTime = 0;
                ending.play();
                sendPost();
            }

        }

    }


const moodSummary = () => {
    let ul = document.getElementById('unordered_mood');
    const listItems = ul.getElementsByTagName('li');

    let moodsList = []
    for(let i =0; i <= listItems.length - 1; i++){
    	// console.log('listItems', listItems[i].textContent)
      moodsList.push(listItems[i].textContent)
    }
    return moodsList
}

const finalBackdropSummary = () => {
    let finalBackdrop = document.querySelector('.current_sound');
    finalBackdrop = finalBackdrop
    return finalBackdrop.innerHTML.trim()
}


const finalTimeSummary = () => {
    let finalTime = document.querySelector('.select_time')
    let finalMinute = finalTime.innerHTML.split(' ')[0]
    return finalMinute
}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const sendPost = () => {
    $(document).ready(function(){
    setTimeout(function(){
    $.ajax({
    url: "/ajax_test/",
    method: 'POST',
    headers: {
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
  },
    credentials: "same-origin",
    data: {
    'moods_before_meditation': String(moodSummary()),
    'meditation_music': String(finalBackdropSummary()),
    'meditation_time': String(finalTimeSummary()),
        },
    datatype: 'json',
    success: function(res){
                }
            })
        }); // timer countdown, that should allow post request after timer done
    });
}

selectSound()
selectMood()
theSelectedTime()
timerCountdown()
