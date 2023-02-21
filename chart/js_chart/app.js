const xlabels = ['From sensor 0', 'From sensor 1']
var currentMax = 20;

const config = {
    type: 'bar',
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
                        max: currentMax
                    }
                }]
        }
    }
}

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
        function checkMax(barChartRegular, barChartForward){
            console.log(barChartRegular)
            if (barChartRegular.some(el => el > currentMax)){
                currentMax = Math.max.apply(Math, barChartRegular) + 20;
                chart.config.options.scales.yAxes[0].ticks.max = currentMax;
            }
            if (barChartForward.some(el => el > currentMax)){
                currentMax = Math.max.apply(Math, barChartForward) + 20;
                chart.config.options.scales.yAxes[0].ticks.max = currentMax;
            }
        }
        checkMax(barChartRegular, barChartForward)
        chart.update();
    })
};
setInterval(updateChart, 5000);
