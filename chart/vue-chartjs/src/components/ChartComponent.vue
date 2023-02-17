<script setup lang="ts">
import Chart from 'chart.js/auto';
import { onMounted } from 'vue';

const labels = ['Meter0, Meter1'];

const data = {
    labels: labels,
    dataset: [{
        labels: labels,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 122)',
        data: [0, 10],
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {}
};

onMounted(() => {
    const myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
})

</script>

<template>
    <h3> Meter status</h3>

    <div>
        <canvas id="myChart"></canvas>
    </div>
</template>