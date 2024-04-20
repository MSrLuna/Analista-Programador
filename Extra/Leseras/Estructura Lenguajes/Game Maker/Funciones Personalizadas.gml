function calculateDamage(damage, defense) {
    var calculatedDamage = damage - defense;
    if (calculatedDamage < 0) {
        calculatedDamage = 0;
    }
    return calculatedDamage;
}

var finalDamage = calculateDamage(30, 10);
