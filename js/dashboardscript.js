document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('pieChart').getContext('2d');
    const data = {
        labels: ['Food', 'Utility', 'Housing', 'Savings', 'Insurance', 'Transportation'],
        datasets: [{
            data: [20, 15, 25, 10, 20, 10], // Example percentages
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
        }]
    };

    const pieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false // Hide the default legend
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return data.labels[tooltipItem.dataIndex] + ': ' + data.datasets[0].data[tooltipItem.dataIndex] + '%';
                        }
                    }
                }
            }
        }
    });

    // Populate the list of values beside the pie chart
    const pieChartValues = document.getElementById('pieChartValues');
    data.labels.forEach((label, index) => {
        const li = document.createElement('li');
        const colorBox = document.createElement('span');
        colorBox.style.backgroundColor = data.datasets[0].backgroundColor[index];
        colorBox.style.display = 'inline-block';
        colorBox.style.width = '12px';
        colorBox.style.height = '12px';
        colorBox.style.marginRight = '8px';
        li.appendChild(colorBox);
        li.appendChild(document.createTextNode(label));
        pieChartValues.appendChild(li);
    });

    // Populate the list of numbers under the pie chart
    const numberList = document.getElementById('numberList');
    const numbers = [100, 200, 300, 400, 500, 600]; // Example numbers
    for (let n = 0; n < numbers.length; n++) {
        const li = document.createElement('li');
        li.textContent = data.labels[n] + ": $" + numbers[n];
        numberList.appendChild(li);
    }
    numbers.forEach(number => {
        const li = document.createElement('li');
        li.textContent = data.labels[n] + "$" + number;
        numberList.appendChild(li);
    });
});