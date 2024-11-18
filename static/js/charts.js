function createChart() {
    const ctxDoughnut = document.getElementById('doughnutChart');

    if (ctxDoughnut) {
        const screenWidth = window.innerWidth;
        let aspectRatio, legendPosition, fontSize, boxWidth;

        if (screenWidth <= 480) {
            aspectRatio = 1;
            legendPosition = 'bottom';
            fontSize = 10;
            boxWidth = 5;
        } else if (screenWidth <= 700) {
            aspectRatio = 1;
            legendPosition = 'bottom';
            fontSize = 12;
            boxWidth = 5;
        } else if (screenWidth <= 768) {
            aspectRatio = 1;
            legendPosition = 'bottom';
            fontSize = 12;
            boxWidth = 5;
        } else if (screenWidth <= 900) {
            aspectRatio = 1;
            legendPosition = 'bottom';
            fontSize = 14;
            boxWidth = 8;
        } else {
            aspectRatio = 2;
            legendPosition = 'right';
            fontSize = 16;
            boxWidth = 10;
        }

        const chartConfig = {
            type: 'doughnut',
            data: {
                labels: choiceData.map(choice => `${choice.text}`),
                datasets: [{
                    data: choiceData.map(choice => choice.votes),
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#CDEE2E']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: aspectRatio,
                plugins: {
                    legend: {
                        position: legendPosition,
                        align: 'center',
                        labels: {
                            generateLabels: function (chart) {
                                return chart.data.labels.map((label, index) => {
                                    const maxChars = 26;
                                    const truncatedLabel = label.length > maxChars
                                        ? label.substring(0, maxChars) + '...'
                                        : label;
                                    return {
                                        text: truncatedLabel,
                                        fillStyle: chart.data.datasets[0].backgroundColor[index],
                                        hidden: false
                                    };
                                });
                            },
                            padding: 10,
                            font: {
                                size: fontSize
                            },
                            boxWidth: boxWidth
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                const value = context.raw;
                                const totalVotes = choiceData.reduce((acc, choice) => acc + choice.votes, 0);
                                const percentage = ((value / totalVotes) * 100).toFixed(1);
                                return `${value} votes (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        };

        return new Chart(ctxDoughnut, chartConfig);
    }
}

let myChart = createChart();

window.addEventListener('resize', function () {
    if (myChart) {
        myChart.destroy();
    }
    myChart = createChart();
});

  

