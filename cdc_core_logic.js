const CDC_CONFIG = {
    PROJECTS_COUNT: 18,
    MAIN_PROJECT_MAX: 28,
    SUB_PROJECT_MAX: 20,
    MERCHANT_COMMISSION: 0.08,
    REWARD_DIVIDER: 8
};

// Enforces the 28-level feeding and 20-level project limits
function checkLevelCap(projectId, currentLevel) {
    const limit = (projectId === 1) ? CDC_CONFIG.MAIN_PROJECT_MAX : CDC_CONFIG.SUB_PROJECT_MAX;
    return currentLevel >= limit;
}

// Calculates 8% commission and the "Divide by 8" rewards
function calculateMerchantPoints(grossSale) {
    const commission = grossSale * CDC_CONFIG.MERCHANT_COMMISSION;
    const userReward = commission / CDC_CONFIG.REWARD_DIVIDER;
    return {
        merchantFee: commission,
        userPoints: userReward
    };
}

console.log("CDC Core Logic Ready: 18 Projects & Level 28 Feeding Tree Active.");

