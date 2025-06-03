// This file contains the JavaScript code for the dashboard's frontend functionality.
// It handles user interactions and communicates with the backend.

document.addEventListener('DOMContentLoaded', function() {
    const alertButton = document.getElementById('alertButton');
    const evacuationPlanButton = document.getElementById('evacuationPlanButton');
    const alertsContainer = document.getElementById('alertsContainer');
    const evacuationPlanContainer = document.getElementById('evacuationPlanContainer');

    alertButton.addEventListener('click', function() {
        fetch('/api/alerts')
            .then(response => response.json())
            .then(data => {
                alertsContainer.innerHTML = '';
                data.alerts.forEach(alert => {
                    const alertElement = document.createElement('div');
                    alertElement.className = 'alert';
                    alertElement.innerText = alert.message;
                    alertsContainer.appendChild(alertElement);
                });
            })
            .catch(error => console.error('Error fetching alerts:', error));
    });

    evacuationPlanButton.addEventListener('click', function() {
        fetch('/api/evacuation-plan')
            .then(response => response.json())
            .then(data => {
                evacuationPlanContainer.innerHTML = '';
                const planElement = document.createElement('div');
                planElement.className = 'evacuation-plan';
                planElement.innerText = data.plan;
                evacuationPlanContainer.appendChild(planElement);
            })
            .catch(error => console.error('Error fetching evacuation plan:', error));
    });
});