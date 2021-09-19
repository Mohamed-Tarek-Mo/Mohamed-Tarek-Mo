// Create a new date instance dynamically with JS
let d = new Date();
let newDate = (d.getMonth() + 1) + '.' + d.getDate() + '.' + d.getFullYear();

/* Global Variables */
const keyAPI = '40aba43e8c42e5a47ae893f1cb20ac2d';

const genButton = document.getElementById("generate").addEventListener('click', weather);

async function weather() {
    const cityZip = document.getElementById('zip').value;
    const personFeeling = document.getElementById('feelings').value;

    if(!cityZip && !personFeeling){
        alert("please enter a zip code and your feelings");
    }else if(!cityZip){
        alert("please enter a zip code");
    }else if(!personFeeling){
        alert("please enter your feelings");
    }

    const webURL = `http://api.openweathermap.org/data/2.5/weather?zip=${cityZip}&appid=${keyAPI}&units=metric`;

    try{

        const response = await fetch(webURL);
        
        const tempData = await response.json();
        const tempDegree = tempData.main.temp;

        await fetch('/weatherPost', {
            method: 'POST',
            credentials: 'same-origin',
            headers: { 'content-Type': 'application/json' },
            body: JSON.stringify({
                dayDate: newDate,
                cityTemp: tempDegree,
                personalFeeling: personFeeling
            })
        });

        const returnedData = await fetch('/weatherGetter');
        const fullTempData = await returnedData.json();
        
        
        
        document.getElementById("date").innerHTML = `the date is ${fullTempData.dayDate} today`;
        document.getElementById("temp").innerHTML = `the temprature is ${fullTempData.cityTemp}C degree today`;
        document.getElementById("content").innerHTML = `you feel ${fullTempData.personalFeeling} today`;

    }catch(error){
        
        console.log("An Error has occured: ", error);
    
    }
}

