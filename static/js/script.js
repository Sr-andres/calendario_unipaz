function toggleMenu() {
    var menuContent = document.getElementById('menuContent');
    if (menuContent.style.display === 'block') {
        menuContent.style.display = 'none';
    } else {
        menuContent.style.display = 'block';
    }
}

function showCalendar() {
    var calendar = document.getElementById('calendar');
    calendar.style.display = 'block';
    var menuContent = document.getElementById('menuContent');
    menuContent.style.display = 'none';
}
