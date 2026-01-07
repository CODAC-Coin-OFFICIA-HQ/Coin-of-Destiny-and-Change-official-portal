// Disaster Severity Check - 8% Population Rule
function checkDisasterSeverity(affectedPop, totalPop) {
    let impactPercentage = (affectedPop / totalPop) * 100;

    if (impactPercentage >= 8.0) {
        // TRIGGER GLOBAL SOLIDARITY VOTE (1% Donation)
        console.log("Severe Disaster (8%+): Global Solidarity Vote Unlocked.");
    } else {
        // LOCAL RESILIENCE ONLY (28.88% Fund)
        console.log("Impact below 8%: Using Local L8 Resilience Funds.");
    }
}
