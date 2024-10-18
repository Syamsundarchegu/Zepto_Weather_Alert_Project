document.addEventListener('DOMContentLoaded', function () {
    fetch('/daily_summary')
        .then(response => response.json())
        .then(data => {
            const summaryDiv = document.getElementById('summary');
            summaryDiv.innerHTML = data.map(item => `
                <div class="card">
                    <h3>${item[0]}</h3>
                    <p>Date: ${item[1]}</p>
                    <p>Average Temp: ${item[2].toFixed(2)}°C</p>
                    <p>Max Temp: ${item[3].toFixed(2)}°C</p>
                    <p>Min Temp: ${item[4].toFixed(2)}°C</p>
                    <p>Condition: ${item[5]}</p>
                </div>
            `).join('');

            const labels = data.map(item => item[0]);
            const avgTemps = data.map(item => item[2]);
            const maxTemps = data.map(item => item[3]);
            const minTemps = data.map(item => item[4]);

            const summaryCtx = document.getElementById('summaryChart').getContext('2d');
            new Chart(summaryCtx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Average Temp (°C)',
                            data: avgTemps,
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Max Temp (°C)',
                            data: maxTemps,
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Min Temp (°C)',
                            data: minTemps,
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });

    const threshold = 20;  // Lower threshold for testing
    fetch('/alerts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ threshold: threshold })
    })
    .then(response => response.json())
    .then(data => {
        const alertsDiv = document.getElementById('alerts');
        if (data.alert !== 'No alert') {
            alertsDiv.innerHTML = `
                <div class="card">
                    <h3>⚠️ Alert!</h3>
                    <p>${data.alert}</p>
                    <p><strong>Locations:</strong> ${data.data.map(item => item.city).join(', ')}</p>
                    <p><strong>Data:</strong> ${data.data.map(item => `City: ${item.city}, Temp: ${item.temp}°C, Time: ${new Date(item.dt * 1000).toLocaleString()}`).join('<br>')}</p>
                </div>
            `;
        } else {
            alertsDiv.innerHTML = '<p>No alerts at the moment.</p>';
        }
    });

    fetch('/historical_trends')
        .then(response => response.json())
        .then(data => {
            const historyLabels = data.map(item => item.date);
            const historyTemps = data.map(item => item.avg_temp);

            const historyCtx = document.getElementById('historyChart').getContext('2d');
            new Chart(historyCtx, {
                type: 'line',
                data: {
                    labels: historyLabels,
                    datasets: [{
                        label: 'Average Temp (°C)',
                        data: historyTemps,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});

