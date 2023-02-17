<template>
  <Bar :data="data" :options="options" />
  <!-- getAPI() -->
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'
import * as chartConfig from './chartConfig.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const apiUrl = "http://127.0.0.1:8000/my-first-api"
var meter0Data = [], meter1Data = []


export default {
  name: 'App',
  components: {
    Bar
  },
  methods: {
    
  },
  data() {
    getMeterData()
    console.log("meter data", meter0Data)
    chartConfig.data.datasets[0].data = meter0Data
    chartConfig.data.datasets[1].data = meter1Data
    return chartConfig
  }
}

async function getMeterData() {
  const apiUrl = "http://127.0.0.1:8000/my-first-api"

  const response = await fetch(apiUrl)
  const barChatData = await response.json()
  
  const barChartmeter0 = barChatData.meter0
  const barChartmeter1 = barChatData.meter1

  meter0Data = barChartmeter0
  meter1Data = barChartmeter1

  console.log(meter0Data)


}
</script>
