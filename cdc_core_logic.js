const CDC_CONFIG = {
    PROJECTS_COUNT: 18,
    MAIN_PROJECT_MAX: 28,
    SUB_PROJECT_MAX: 20,
    MERCHANT_COMMISSION: 0.08,
    REWARD_DIVIDER: 8
};

function checkLevelCap(projectId, currentLevel) {
    const limit = (projectId === 1) ? CDC_CONFIG.MAIN_PROJECT_MAX : CDC_CONFIG.SUB_PROJECT_MAX;
    return currentLevel >= limit;
}

function calculateMerchantPoints(grossSale) {
    const commission = grossSale * CDC_CONFIG.MERCHANT_COMMISSION;
    return commission / CDC_CONFIG.REWARD_DIVIDER;
}

console.log("CDC Core Logic Ready.");

