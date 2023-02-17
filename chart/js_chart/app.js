var meterRegular = [], meterForward = []
const xlabels = ['From sensor 0', 'From sensor 1']


const config = {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: xlabels,
        datasets: [
            {
              label: 'Regular',
              backgroundColor: '#f87979',
            //   data: meterRegular
            },
            {
              label: 'Forward',
              backgroundColor: '#ff0088',
            //   data: meterForward
            }
          ]
    },

    options: {
        scales: {
            yAxes: [{
                    display: true,
                    ticks: {
                        beginAtZero: true,
                        steps: 5,
                        stepValue: 5,
                        // max: 50
                    }
                }]
        }
    }
}

// async function meterChart() {
//   await getMeterData()




// setTimeout(meterChart, 5000);

// }

// meterChart()



const ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, config);
updateChart()


function updateChart(){
    async function fetchData(){
        const apiUrl = "http://127.0.0.1:8000/meter_status";
        const response = await fetch(apiUrl);
        const barChatData = await response.json();
        return barChatData;
    }

    fetchData().then(barChatData => { 
        const barChartRegular = barChatData.regular;
        const barChartForward = barChatData.forward;

        chart.config.data.datasets[0].data = barChartRegular;
        chart.config.data.datasets[1].data = barChartForward;
        chart.update();
    })

    console.log('update');
};
setInterval(updateChart, 5000);


//Fetch Data from API

// async function getMeterData() {
//   const apiUrl = "http://127.0.0.1:8000/meter_status"

//   const response = await fetch(apiUrl)
//   const barChatData = await response.json()
  
//   console.log(barChatData)
//   const barChartRegular = barChatData.regular
//   const barChartForward = barChatData.forward

//   meterRegular = barChartRegular
//   meterForward = barChartForward

//   console.log(meterRegular, meterForward)
// }