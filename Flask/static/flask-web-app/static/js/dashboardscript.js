document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('pieChart').getContext('2d');
    const data = {
        labels: ['Food', 'Utility', 'Housing', 'Savings', 'Insurance', 'Transportation', 'Disposable'],
        datasets: [{
            data: [20, 15, 20, 10, 15, 10, 10], // Example percentages
            total: 900, // Example total
            backgroundColor: ['#1E3A8A', '#60A5FA', '#274BDB', '#93C5FD', '#3B82F6', '#AFCBFF', '#5A9BD5']
        }]
    };

    const pieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false 
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const percentage = data.datasets[0].data[tooltipItem.dataIndex];
                            const amount = data.datasets[0].total * (percentage / 100);
                            return percentage + '% ($' + amount.toFixed(2) + ')';
                        }
                    }
                }
            }
        }
    });

    // Beside the pie chart
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

    // Under the pie chart
    const numberList = document.getElementById('numberList');
    for (let n = 0; n < data.datasets[0].data.length; n++) {
        const li = document.createElement('li');
        li.textContent = data.labels[n] + ": $" + (data.datasets[0].total * (data.datasets[0].data[n] / 100)).toFixed(2);
        numberList.appendChild(li);
    }

    // Example paragraph
    const budgetPlanDescription = "This is your updated monthly budget plan based on the data provided. Please review the numbers and make adjustments as necessary to ensure you stay within your budget.";
    document.getElementById('budgetPlanDescription').textContent = budgetPlanDescription;
});