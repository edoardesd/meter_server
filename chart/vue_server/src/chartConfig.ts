const apiUrl = "http://127.0.0.1:8000/my-first-api"
const xlabels = ['From sensor 1', 'From sensor 2']
console.log(xlabels)


export const data = {
  labels: xlabels,
  datasets: [
    {
      label: 'Sensor One',
      backgroundColor: '#f87979',
      data: [0,0]
    },
    {
      label: 'Sensor two',
      backgroundColor: '#ff0088',
      data: [0,0]
    },
    
  ],
};


export const options = {
  responsive: true,
  maintainAspectRatio: false,
};